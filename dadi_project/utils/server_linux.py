import os
import time

import paramiko
import stat
import datetime as dt
from dadi_project.utils import my_log

class Operate_Server():
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname  # 服务器IP地址
        self.port = port  # 服务器登录端口号
        self.username = username  # 登录账号
        self.password = password

    def login(self):
        try:
            # 创建SSHClient对象，ssh
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
            # 创建linux连接
            ssh.connect(
                hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))

        except Exception as e:
            print("发生未知错误：%s" % e)
            raise
        return ssh

    def run(self, command, **kwargs):
        ssh = self.login()
        # 执行sh命令并返回执行结果
        result = ssh.exec_command(command)[1].read().decode('utf-8')
        print(" shell命令[%s]执行结果：%s" % (command, result))
        # 登出服务器
        ssh.close()
        print("登出服务器[%s]" % self.hostname)
        return result


    def getRemoteFiles(self, remoteDir):
        ssh = self.login()
        tran = ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        # 加载sftp服务器文件对象(根目录)
        filesAttr = sftp.listdir_attr(remoteDir)
        try:
            # foreach遍历
            for fileAttr in filesAttr:
                # 判断是否为目录
                if stat.S_ISDIR(fileAttr.st_mode):
                    # 1.当是文件夹时
                    # 计算子文件夹在ftp服务器上的路径
                    son_remoteDir = remoteDir + '/' + fileAttr.filename
                    # 生成器, 迭代调用函数自身
                    yield from self.getRemoteFiles(son_remoteDir)
                else:
                    # 2.当是文件时
                    # 生成器, 添加"路径+文件名"到迭代器"
                    yield remoteDir + '/' + fileAttr.filename
        except Exception as e:
            print('getAllFilePath exception:', e)

    def getLocalFiles(self, localDir):

        global files
        if not os.path.exists(localDir):
            print(f"本地路径{localDir}不存在！")
        else:
            pass
        # 加载本地路径文件对象(根目录)
        for root, dirs, files in os.walk(localDir):
            print('root_dir:', root)
            print('sub_dirs:', dirs)
            print('files:', files)
        return files

    # 远程目录remoteDir文件下载保存到本地目录localDir
    def download_files(self, remoteDir, localDir):
        ssh = self.login()
        tran = ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        # 记录下载开始时间
        dt_start = dt.datetime.now()
        print('................. {} 开始下载!..................\n'.format(dt_start))

        # 判断输入的本地目录是否存在
        #    if not os.path.exists(localDir):
        #    # 若本地目录不存在,则创建该目录
        #    os.makedirs(localDir)

        # 实例化生成器, 获取sftp指定目录下的所有文件路径
        files = self.getRemoteFiles(remoteDir)
        # foreach遍历
        for file in files:
            # 要下载的远程文件, 本地时路径+文件名
            remoteFileName = file
            ###获取文件的全路径
            get_son_remote_dir = '/'.join(remoteFileName.split('/')[0:-1])
            # # 定义下载保存到本地时的路径+全路径+文件名
            # localFileName = os.path.join(localDir+get_son_remote_dir, file.split('/')[-1])
            localFileName = os.path.join(localDir, file.split('/')[-1])
            if not os.path.exists(localDir):
                # 若本地目录不存在,则创建该目录
                os.makedirs(localDir)
            try:
                # 下载文件, 本地已有同名文件则覆盖
                sftp.get(remoteFileName, localFileName)
                print('sftp服务器文件 {} 下载成功!\n该文件保存本地位置是 {} !\n'.format(
                    remoteFileName, localFileName))
            except Exception as e:
                print('%s下载出错!:\n' % (remoteFileName), e)
                # 下载失败, 关闭连接
                sftp.close()

        # 下载成功, 关闭连接

        # 记录下载结束时间
        dt_end = dt.datetime.now()
        print('..................... {} 下载完成!..................'.format(dt_end))
        # 记录下载时长
        dt_long = dt_end - dt_start
        print('................ 本次下载共用时间 {} !...............\n'.format(dt_long))

    def put_file(self, local_path, server_path, **kwargs):
        """
        :command: sh命令
        :param kwargs:  传参(private_key: 私钥路径) (password: 密码)
        :return:
        """
        try:
            # 创建SSHClient对象，ssh
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 创建linux连接
            ssh.connect(
                hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))
            # 获取Transport实例
            transport = ssh.get_transport()
            # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
            sftp = paramiko.SFTPClient.from_transport(transport)
            # 将本地 api.py 上传至服务器 /www/test.py。文件上传并重命名为test.py
            sftp.put(local_path, server_path)
            # 登出服务器
            ssh.close()
            print("登出服务器[%s]" % self.hostname)
        except Exception as e:
            print("发生未知错误：%s" % e)
            raise

    def put_files(self, remoteDir, localDir):
        ssh = self.login()
        tran = ssh.get_transport()
        sftp = paramiko.SFTPClient.from_transport(tran)
        # 记录下载开始时间
        dt_start = dt.datetime.now()
        print('................. {} 开始上传!..................\n'.format(dt_start), flush=True)
        #判断目标服务器路径是否存在
        stdin, stdout, stderr = ssh.exec_command(f'ls {remoteDir}')
        if stdout.readline() != '':
            print("exist")
            result = ssh.exec_command(f'cd {"/".join(remoteDir.split("/")[:-2])};rm -rf {remoteDir.split("/")[-2]};mkdir {remoteDir.split("/")[-2]}')
            time.sleep(1)
            print(result)
        else:
            print("not exist")
            result = ssh.exec_command(f'cd {"/".join(remoteDir.split("/")[:-2])};mkdir {remoteDir.split("/")[-2]}')
            time.sleep(1)
            print(result)

        # 实例化生成器, 获取sftp指定目录下的所有文件路径
        files = self.getLocalFiles(localDir)
        # foreach遍历
        for file in files:
            # 要上传的远程文件路径, 路径+文件名
            remoteFileName = remoteDir + file
            # 要上传的本地文件路径, 路径+文件名
            localFileName = localDir + file
            try:
                # 上传文件
                sftp.put(localFileName, remoteFileName)
                print('本地文件 {} 上传成功!\n该文件保存服务器位置是 {} !\n'.format(
                    localFileName, remoteFileName))
            except Exception as e:
                print('%s上传出错!:\n' % (localFileName), e)
                # 下载失败, 关闭连接
                sftp.close()

        # 下载成功, 关闭连接

        # 记录下载结束时间
        dt_end = dt.datetime.now()
        print('..................... {} 上传完成!..................'.format(dt_end))
        # 记录下载时长
        dt_long = dt_end - dt_start
        print('................ 本次上传共用时间 {} !...............\n'.format(dt_long))

    def get_file(self, local_path, server_path, **kwargs):
        """
        :command: sh命令
        :param kwargs:  传参(private_key: 私钥路径) (password: 密码)
        :return:
        """
        try:
            # 创建SSHClient对象，ssh
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 创建linux连接
            ssh.connect(
                hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))
            # 获取Transport实例
            transport = ssh.get_transport()
            print(transport)
            # 创建sftp对象，SFTPClient是定义怎么传输文件、怎么交互文件
            sftp = paramiko.SFTPClient.from_transport(transport)
            # 将服务器 /www/test.py 下载到本地 aaa.py。文件下载并重命名为aaa.py
            sftp.get(server_path, local_path)
            # 登出服务器
            ssh.close()
            print("登出服务器[%s]" % self.hostname)
        except Exception as e:
            print("发生未知错误：%s" % e)
            raise



if __name__ == "__main__":
    log = my_log.Log()
    # 通过密码登录
    # Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password="ccicall").run(command="cd /ccicall/Applog/task-data/")
    # local_path = r'E:\Pythonprojects\untitled\dadi_project\APPLY_787_20390801'
    # server_path = '/ccicall/sftp/cuishoufile/20390801/APPLY_787_20390801'
    # Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password='ccicall').get_file(local_path,server_path)
    localDir = os.path.dirname(__file__) + r"\20390801\\"[:-1]
    xx_remoteDir = '/ccicall/sftp/cuishoufile/20390801/'
    cs_remoteDir = '/tomcat/apps/server/ccmsbatchfile/input/host1/20390801/'
    log.info("开始运行!")
    testpath = '/ccicall/sftp/cuishoufile/20390801/20390801/'
    # Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password='ccicall').download_files(xx_remoteDir, localDir)
    Operate_Server(hostname="10.1.11.201", port=22, username="tomcat", password='ccic_2019').put_files(cs_remoteDir, localDir)


    # 通过密钥认证登录
    # Operate_Server(hostname="IP", port=22, username="用户").run(command="pwd", private_key="私钥路径")


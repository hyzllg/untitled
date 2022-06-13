import os

import paramiko

class Operate_Server():
    def __init__(self, hostname, port, username, password):
        self.hostname = hostname  # 服务器IP地址
        self.port = port  # 服务器登录端口号
        self.username = username  # 登录账号
        self.password = password

    def run(self, command, **kwargs):
        """
        :command: sh命令
        :param kwargs:  传参(private_key: 私钥路径) (password: 密码)
        :return:
        """
        try:
            # 创建SSHClient对象，ssh
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #创建linux连接
            ssh.connect(
                hostname=self.hostname, port=self.port, username=self.username, password=self.password)
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))

            # 执行sh命令并返回执行结果
            result = ssh.exec_command(command)[1].read().decode('utf-8')
            print(" shell命令[%s]执行结果：%s" % (command, result))

            # 登出服务器
            ssh.close()
            print("登出服务器[%s]" % self.hostname)
        except Exception as e:
            print("发生未知错误：%s" % e)
            raise
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
    # 通过密码登录
    # Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password="ccicall").run(command="cd /ccicall/Applog/task-data/")
    # local_path = os.path.dirname(__file__) + r"\20390801\\"[:-1]
    # server_path = '/ccicall/sftp/cuishoufile/20390801/'
    local_path = os.path.dirname(__file__) + r'\APPLY_787_20390801'
    server_path = '/ccicall/sftp/cuishoufile/20390801/APPLY_787_20390801'
    Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password='ccicall').get_file(local_path,server_path)

    # 通过密钥认证登录
    # Operate_Server(hostname="IP", port=22, username="用户").run(command="pwd", private_key="私钥路径")


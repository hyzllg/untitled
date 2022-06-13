import paramiko
import os
import stat
import datetime as dt
from dadi_project.utils import my_log

def getRemoteFiles(remoteDir,sftp):
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
                yield from getRemoteFiles(son_remoteDir,sftp)
            else:
                # 2.当是文件时
                # 生成器, 添加"路径+文件名"到迭代器"
                yield remoteDir + '/' + fileAttr.filename
    except Exception as e:
        print('getAllFilePath exception:', e)

def getLocalFiles(localDir):

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
def download_files(remoteDir,localDir,sftp):
    # 记录下载开始时间
    dt_start = dt.datetime.now()
    print('................. {} 开始下载!..................\n'.format(dt_start))

    # 判断输入的本地目录是否存在
    #    if not os.path.exists(localDir):
    #    # 若本地目录不存在,则创建该目录
    #    os.makedirs(localDir)

    # 实例化生成器, 获取sftp指定目录下的所有文件路径
    files = getRemoteFiles(remoteDir,sftp)
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

# 远程目录remoteDir文件下载保存到本地目录localDir
def put_file(remoteDir,localDir,sftp):
    # 记录下载开始时间
    dt_start = dt.datetime.now()
    print('................. {} 开始上传!..................\n'.format(dt_start), flush=True)

    # 实例化生成器, 获取sftp指定目录下的所有文件路径
    files = getLocalFiles(localDir)
    # foreach遍历
    for file in files:
        #要上传的远程文件路径, 路径+文件名
        remoteFileName = remoteDir + file
        #要上传的本地文件路径, 路径+文件名
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


def getConnect():
    log = my_log.Log()
    xx_ssh = paramiko.SSHClient()
    xx_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
    cs_ssh = paramiko.SSHClient()
    cs_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
    try:
        log.info("连接sftp服务器！")
        xx_ssh.connect('10.1.12.42', 22, 'weblog10', 'weblog10')
        xx_tran = xx_ssh.get_transport()
        xx_sftp=paramiko.SFTPClient.from_transport(xx_tran)
        cs_ssh.connect('10.1.11.201', 22, 'tomcat', 'ccic_2019')
        cs_tran = cs_ssh.get_transport()
        cs_sftp=paramiko.SFTPClient.from_transport(cs_tran)

        stdin, stdout, stderr = cs_ssh.exec_command('ls DIR')
        if stdout.readline() != '':
            print("exist")
        else:
            print("not exist")
        # localDir = os.path.dirname(__file__) + r"\20390801\\"[:-1]
        # xx_remoteDir = '/ccicall/sftp/cuishoufile/20390801/'
        # cs_remoteDir = '/tomcat/apps/server/ccmsbatchfile/input/host1/20390801/'
        # log.info("开始下载文件")
        # download_files(xx_remoteDir,localDir,xx_sftp)
        # # put_files(cs_remoteDir,localDir,cs_sftp)

        print("************************************")
        #print("connect close")
    # except AuthenticationException as e:
    #     print('主机%s密码错误' %(hostname))
    except Exception as e:
        print('未知错误:',e)
    finally:
        xx_sftp.close()
        xx_ssh.close()
        cs_sftp.close()
        cs_ssh.close()
        #print("关闭")


if __name__ == '__main__':
    getConnect()






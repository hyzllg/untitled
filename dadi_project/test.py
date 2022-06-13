import paramiko


class Operate_Server():
    def __init__(self, hostname, port, username):
        self.hostname = hostname  # 服务器IP地址
        self.port = port  # 服务器登录端口号
        self.username = username  # 登录账号

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

            # 通过密钥调用connect函数建立Linux连接
            if "private_key" in kwargs.keys():
                private_key = paramiko.RSAKey.from_private_key_file(kwargs["private_key"])
                ssh.connect(
                    hostname=self.hostname, port=self.port, username=self.username, pkey=private_key)
            # 通过密码调用connect函数建立Linux连接
            if "password" in kwargs.keys():
                ssh.connect(
                    hostname=self.hostname, port=self.port, username=self.username, password=kwargs["password"])
            print(" 账号[{0}]成功登录服务器[{1}]".format(self.username, self.hostname))

            # 执行sh命令并返回执行结果
            result = ssh.exec_command(command)[1].read().decode('utf-8')
            print(" shell命令[%s]执行结果：%s" % (command, result))

            # 登出服务器
            ssh.close()
            print(" 登出服务器[%s]" % self.hostname)
        except Exception as e:
            print("发生未知错误：%s" % e)
            raise


if __name__ == "__main__":
    # 通过密码登录
    Operate_Server(hostname="10.1.12.42", port=22, username="ccicall").run(command="cd /ccicall/Applog/task-data/;sh UpdateALOverStage.sh 0992,PBLG202231170234000328,2022/12/12", password="ccicall")

    # 通过密钥认证登录
    # Operate_Server(hostname="IP", port=22, username="用户").run(command="pwd", private_key="私钥路径")


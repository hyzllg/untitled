import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# 创建一个带附件的邮件实例
message=MIMEMultipart()
# 邮件的其他属性
message['From'] = '<自己的163邮箱>'
message['Subject'] = Header(u'邮件标题发送成功', 'utf8').encode()
message['To'] = u'<对方的邮箱>'
# 邮件正文内容
attr2 = MIMEText('备份详情请查看附件日志', 'plain', 'utf-8')
message.attach(attr2)
# #构造附件txt附件1
# attr1=MIMEText(open(r'D:\j\run1.txt','rb').read(),'base64','utf-8')
# attr1["content_Type"]='application/octet-stream'
# attr1["Content-Disposition"] = 'attachment; filename="run1.txt"'
# message.attach(attr1)
server = smtplib.SMTP('smtp.163.com', 25)
server.login('自己的163邮箱', '自己的163邮箱授权码')
server.sendmail('自己的邮箱', ['对方的邮箱'],message.as_string())
print("邮件发送成功")
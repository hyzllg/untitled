import easygui


def input_validation():
	while True:
		msg='输入信息'
		title='信息搜集'
		fields=['环境','产品','笔数']
		response=easygui.multenterbox(msg, title, fields, values = ['sit','7014', '1'])
		if response[0].upper() not in ['SIT', 'UAT', 'DEV']:
			easygui.msgbox(msg = "只支持环境\nsit\nuat\ndev", title = '所选环境不支持！',ok_button = '继续选择', image = None, root = None)
			continue
		elif response[1] not in ['7014', '7015', '7016', '7017', '7018']:
			easygui.msgbox(msg = "只支持产品\n7014\n7015\n7016\n7017\n7018", title ='所选产品不支持！', ok_button = '继续选择', image = None, root = None)
			continue
		elif response[2].isdigit() is False:
			easygui.msgbox(msg = "笔数必须是整数", title = 'ERROR', ok_button ='继续选择', image = None, root = None)
			continue    	
		break
	return response
input_validation()		


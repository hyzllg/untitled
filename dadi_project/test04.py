from dadi_project.utils import generate_customer_info

idNo = generate_customer_info.customer().idNo()
name = generate_customer_info.customer().name()
phone = generate_customer_info.customer().phone()

bankcard = generate_customer_info.customer().bankcard()
print(
    f'''
    身份证号：{idNo}
    姓名：{name}
    手机号：{phone}
    银行卡号：{bankcard}
    '''
)
import random
import time
import Collect


def data(loanNo,productid,datetime0,datatime3,payamt):#productid
    '''
    533000004000001'--甜橙
    533010003000001'--还呗
    533000007000001'--拍拍贷
    533010015000001'--零花保
    '''
    number ={
        7014:"533000004000001",
        7011:"533010015000001",
        7017:"533010003000001",
        7018:"533000007000001"
    }
    a = str(random.randint(1, 10000))
    b = time.strftime("%Y%m%d%H%M%S")
    serialno = b + '00000000000000' + a
    a = Collect.sql_cha(Collect.zwSIT_ORACLE,"select a.customername,a.accountno,af.result_seq_no,a.putoutno from acct_loan a inner join acct_fund_apply af on a.apply_no = af.apply_no where serialno = '{loanNo}'".format(loanNo))[0]
    data = f"{serialno}{number[productid]}533030001000001533020001000001{a[0]}{a[1]}{a[2]}{a[3]}805{datetime0}{payamt[2]}{payamt[3]}{payamt[4]}{payamt[5]}{datatime3}FINAL_CLAIM"
    return  data



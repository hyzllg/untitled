import datetime
import random
import time
import winreg
import cx_Oracle
import Collect

class CLAIM_RESULT:



    def __init__(self, environment,loanNo):
        self.environment = environment
        self.loanNo = loanNo



    #计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    def Caltime(self,date1,date2):
        #%Y/%m/%d为日期格式，其中的/可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        #date1=time.strptime(date1,"%Y/%m/%d %H:%M:%S")
        #date2=time.strptime(date2,"%Y/%m/%d %H:%M:%S")
        date1=time.strptime(date1,"%Y/%m/%d")
        date2=time.strptime(date2,"%Y/%m/%d")
        #根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        #date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        #date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date1=datetime.datetime(date1[0],date1[1],date1[2])
        date2=datetime.datetime(date2[0],date2[1],date2[2])
        #返回两个变量相差的值，就是相差天数
        # 理赔日到上期还款日的天数int整型
        # abs(n)将负数转换成正数
        return abs((date2-date1).days)

    def get_date(self, date, time_interval):#字符串时间，天数负数代表前多少天，正数代表后多少天
        start_date = datetime.datetime.strptime(date, "%Y/%m/%d") #将字符串转换成时间格式
        now_date = datetime.timedelta(days=time_interval)
        a = start_date + now_date
        fu = a.strftime('%Y/%m/%d')#时间转回字符串格式
        return  fu

    def datatime_cap(self, datatime):
        datatime = datatime.replace(r"/", "")
        return datatime

    def sql_update_acct_loan(self, setting,v,vv,n):
        try:
            conn = cx_Oracle.connect(setting[0], setting[1], setting[2])
            cursor = conn.cursor()
            my_sql_c = "update acct_loan set overduedays = '80',normalbalance = :v ,overduebalance = :vv where serialno = :n"
            cursor.execute(my_sql_c, {'v': v,'vv': vv, 'n': n})
            conn.commit()  # 这里一定要commit才行，要不然数据是不会插入的
            conn.close()

        except cx_Oracle.DatabaseError:
            return print("无效的SQL语句")




    def Payamt(self,datetime1):
        #未还本金
        a = Collect.sql_cha(self.environment,"select sum(paycorpusamt),sum(actualpaycorpusamt) from acct_payment_schedule s  where s.objectno = '{}'".format(self.loanNo))
        corpusamt = a[0][0] - a[0][1]
        #逾期本金
        #先查一下最早逾期期次
        n = Collect.sql_cha(self.environment,f"select seqid from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and status = '12'")[0][0]
        a = Collect.sql_cha(self.environment,f"select sum(paycorpusamt),sum(actualpaycorpusamt) from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and seqid in ('{n}','{n+1}','{n+2}')")
        yq_corpusamt = a[0][0] - a[0][1]
        #正常本金
        zc_corpusamt = corpusamt - yq_corpusamt

        #利息 正常本金(1683.86)*利率0.062/360*18 + 逾期期数未还利息
        a = Collect.sql_cha(self.environment,f"select sum(payinteamt),sum(actualpayinteamt) from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and seqid in ('{n}','{n+1}','{n+2}')")
        #逾期整期未还利息
        yq_inteamt = a[0][0] - a[0][1]
        #理赔日前不足整期利息
        datetime2 = Collect.sql_cha(self.environment,f"select paydate from acct_payment_schedule s  where s.objectno = '{self.loanNo}' and seqid = '{n+2}'")[0][0]
        days = self.Caltime(datetime1,datetime2)
        payinteamt = round(zc_corpusamt * 0.062/360 * days + yq_inteamt,2)

        #罚息
        a = Collect.sql_cha(self.environment,f"select sum(payfineamt),sum(actualfineamt) from acct_payment_schedule s  where s.objectno =  '{self.loanNo}'and seqid in ('{n}','{n+1}','{n+2}')")
        fineamt = a[0][0] - a[0][1]

        #本金 利息 罚息 合计
        return zc_corpusamt,yq_corpusamt,corpusamt,payinteamt,fineamt,round((corpusamt+payinteamt+fineamt),2)

    def data(self,productid,datetime0,datatime3,payamt,TASK_ID):#productid
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
        b = time.strftime("%Y%m%d%H%M%S")
        serialno = b + '00000000000000' + str(random.randint(1000, 10000))
        a = Collect.sql_cha(self.environment,"select a.customername,a.accountno,af.result_seq_no,a.putoutno from acct_loan a inner join acct_fund_apply af on a.apply_no = af.apply_no where serialno = '{}'".format(self.loanNo))[0]
        data = f"{serialno}{number[productid]}533030001000001533020001000001{a[0]}{a[1]}{a[2]}{a[3]}805{self.datatime_cap(datetime0)}{payamt[2]}{payamt[3]}{payamt[4]}{payamt[5]}{self.datatime_cap(datatime3)}FINAL_CLAIM"
        ID = "46010001130" + str(random.randint(1000, 10000))
        sql = f"insert into acct_file_task_detail (ID, TASK_ID, ROW_NUM, LINE_CONTENT, DIFF_COLUMNS, PROCESS_STATUS, CREATE_USER, CREATE_TIME, UPDATE_USER, UPDATE_TIME, DIFF_MY_VALUES, ERROR_MESSAGE, BIZ_NO)values ({ID}, '{TASK_ID}', 1, '{data}', null, 2, 'system', to_date('03-10-2028', 'dd-mm-yyyy'), 'system', to_date('03-10-2028', 'dd-mm-yyyy'), null, null, '{a[3]}')"
        return  data,sql

    def insert_data_acct_file_task_detail(self, statement,setting):
        try:
            conn = Collect.cx_Oracle.connect(setting[0], setting[1], setting[2])
            cursor = conn.cursor()
            cursor.execute(statement)
            conn.commit()  # 这里一定要commit才行，要不然数据是不会插入的
            print("data插入acct_file_task_detail表成功！")
            conn.close()


        except Collect.cx_Oracle.DatabaseError:
            return print("无效的SQL语句")

    def insert_data_acct_file_task(self,loan_numbers,setting,task_id,datatime):
        try:
            conn = Collect.cx_Oracle.connect(setting[0], setting[1], setting[2])
            statement = f"insert into acct_file_task (ID, BUSINESS_DATE, FUND_CODE, PRODUCT_CODE, ORG_ID, REQUEST_ID, FILE_CODE, FILE_PATH, FILE_NAME, FILE_SIZE, FILE_ROWS, STATUS, ERROR_CODE, ERROR_MESSAGE, CREATE_TIME, UPDATE_TIME, NEXT_STEP, ERROR_ROWS, PROCESS_TYPE) values ('{task_id}', '{datatime}', '787', null, null, '202103081124', 'ClaimApply', '/DBBX_KCXB_CLAIM/20281003/', 'INS_CLAIM_RESULT_DBBX_KCXB_20281002', null, '{loan_numbers}', 1, null, null, to_date('03-10-2028 09:52:14', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-10-2028 09:52:15', 'dd-mm-yyyy hh24:mi:ss'), null, 0, 1)"
            cursor = conn.cursor()
            cursor.execute(statement)
            conn.commit()  # 这里一定要commit才行，要不然数据是不会插入的
            print("data插入acct_file_task表成功！")
            conn.close()


        except Collect.cx_Oracle.DatabaseError:
            return print("无效的SQL语句")

def productid(environment,loanNo):
    sql = f"select businesstype from ACCT_PAYMENT_SCHEDULE where objectno = '{loanNo}'"
    productid = Collect.sql_cha(environment,sql)[0][0]
    return int(productid)

def environments(environment):
    if environment == 1:
        environment = Collect.zwSIT_ORACLE
    elif environment == 2:
        environment = Collect.zwUAT_ORACLE
    else:
        print("环境选择错误，1是sit环境，2是uat环境！")
    return environment

def main(loanNo,a):
    print("运行中……")
    #借据笔数
    loan_numbers = len(loanNo)
    #环境
    environment = environments(a)
    #TASK_ID
    TASK_ID = "46010001130" + str(random.randint(1000, 10000))
    tab = True
    for loanNo in loanNo:

        CLAIM_RESULTS = CLAIM_RESULT(environment,loanNo)
        #datetime0最早逾期期次还款日，datatime3理赔日
        #最早逾期期次还款日
        datetime0 = Collect.sql_cha(environment,f"select paydate from acct_payment_schedule s  where s.objectno = '{loanNo}'and status = '12'")[0][0]
        #理赔日
        datatime3 = CLAIM_RESULTS.get_date(datetime0,80)
        print(f"索赔日：{CLAIM_RESULTS.datatime_cap(datatime3)}")
        #各科目金额（正常本金，逾期本金，本金，利息，罚息，总和）
        payamt = CLAIM_RESULTS.Payamt(datatime3)
        #更新借据表中的逾期金额，正常金额
        CLAIM_RESULTS.sql_update_acct_loan(environment,payamt[0],payamt[1],loanNo)
        #生成申请文件数据
        datas = CLAIM_RESULTS.data(productid(environment,loanNo),datetime0,datatime3,payamt,TASK_ID)
        datatime4 = CLAIM_RESULTS.datatime_cap(datatime3)
        #data插入acct_file_task_detail
        CLAIM_RESULTS.insert_data_acct_file_task_detail(datas[1],environment)
        if tab:
            #更改acct_file_task表数据
            CLAIM_RESULTS.insert_data_acct_file_task(loan_numbers,environment,TASK_ID,CLAIM_RESULTS.get_date(datatime3,-1))
            tab = False
        print(f"acct_file_task_detail表TASK_ID:{TASK_ID}")
        #生成理赔申请文件，路径是桌面
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        with open(winreg.QueryValueEx(key, "Desktop")[0] + f"\INS_CLAIM_REQUEST_DBBX_KCXB_{CLAIM_RESULTS.datatime_cap(CLAIM_RESULTS.get_date(datatime3,-1))}",mode="a") as h:
            h.write(datas[0] + '\n')

        # with open(os.path.join(os.path.expanduser("~"), 'Desktop') + f"\CLAIM_RESULT_DBBX_KCXB_{datatime4}",mode="w") as h:
        #     h.write(datas[0])
    print("理赔申请文件生成成功！在桌面")

if __name__ == '__main__':
    start = time.time()
    #借据号
    loanNo = ['787-502807223301439865','787-502807223301439885','787-502807223301440705']
    #第一个参数是借据号list格式，第二个参数是环境，1代表sit环境，2代表uat环境
    main(loanNo,1)
    end = time.time()
    print(f"运行时间：{end - start}")

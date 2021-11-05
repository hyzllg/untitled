import datetime
import random
import sys
import time
import yaml
import os

from utils import database_manipulation,my_log


class CLAIM_RESULT:

    def __init__(self, environment, loanNo, zwzj_oracle):
        self.environment = environment
        self.loanNo = loanNo
        self.zwzj_oracle = zwzj_oracle

    # 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    def Caltime(self, date1, date2):
        # %Y/%m/%d为日期格式，其中的/可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        # date1=time.strptime(date1,"%Y/%m/%d %H:%M:%S")
        # date2=time.strptime(date2,"%Y/%m/%d %H:%M:%S")
        date1 = time.strptime(date1, "%Y/%m/%d")
        date2 = time.strptime(date2, "%Y/%m/%d")
        # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date1 = datetime.datetime(date1[0], date1[1], date1[2])
        date2 = datetime.datetime(date2[0], date2[1], date2[2])
        # 返回两个变量相差的值，就是相差天数
        # 理赔日到上期还款日的天数int整型
        # abs(n)将负数转换成正数
        return abs((date2 - date1).days)

    def get_date(self, date, time_interval):  # 字符串时间，天数负数代表前多少天，正数代表后多少天
        start_date = datetime.datetime.strptime(date, "%Y/%m/%d")  # 将字符串转换成时间格式
        now_date = datetime.timedelta(days=time_interval)
        a = start_date + now_date
        fu = a.strftime('%Y/%m/%d')  # 时间转回字符串格式
        return fu

    def datatime_cap(self, datatime):
        datatime = datatime.replace(r"/", "")
        return datatime

    def sql_update_acct_loan(self, zc_corpusamt, yq_corpusamt, lonano):
        my_sql_c = "update acct_loan set overduedays = '80',normalbalance = '{}' ,overduebalance = '{}' where serialno = '{}'".format(zc_corpusamt,yq_corpusamt,lonano)
        self.zwzj_oracle.insert_update_data(my_sql_c)

    def Payamt(self, datetime1,day):
        # 未还本金
        a = self.zwzj_oracle.query_data(
                            "select sum(paycorpusamt),sum(actualpaycorpusamt) from acct_payment_schedule s  where s.objectno = '{}'".format(
                                self.loanNo))
        corpusamt = a[0][0] - a[0][1]
        # 逾期本金
        # 先查一下最早逾期期次
        n = self.zwzj_oracle.query_data(
                            f"select seqid from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and status = '12'")[
            0][0]
        a = self.zwzj_oracle.query_data(
                            f"select sum(paycorpusamt),sum(actualpaycorpusamt) from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and seqid in ('{n}','{n + 1}','{n + 2}')")
        yq_corpusamt = a[0][0] - a[0][1]
        # 正常本金
        zc_corpusamt = corpusamt - yq_corpusamt

        # 利息 正常本金(1683.86)*利率0.062/360*18 + 逾期期数未还利息
        a = self.zwzj_oracle.query_data(
                            f"select sum(payinteamt),sum(actualpayinteamt) from acct_payment_schedule s  where s.objectno = '{self.loanNo}'and seqid in ('{n}','{n + 1}','{n + 2}')")
        # 逾期整期未还利息
        yq_inteamt = a[0][0] - a[0][1]
        # 理赔日前不足整期利息
        datetime2 = self.zwzj_oracle.query_data(
                                    f"select paydate from acct_payment_schedule s  where s.objectno = '{self.loanNo}' and seqid = '{n + 2}'")[
            0][0]
        #贷款利率
        loanrate = self.zwzj_oracle.query_data("select LOANRATE from acct_loan where serialno = '%s'" % self.loanNo)[0][0]
        days = self.Caltime(datetime1, datetime2) + (day - 80)
        payinteamt = round(zc_corpusamt * loanrate / 360 * days + yq_inteamt, 2)

        # 罚息
        a = self.zwzj_oracle.query_data(
                            f"select sum(payfineamt),sum(actualfineamt) from acct_payment_schedule s  where s.objectno =  '{self.loanNo}'and seqid in ('{n}','{n + 1}','{n + 2}')")
        fineamt = a[0][0] - a[0][1]

        # 本金 利息 罚息 合计
        return zc_corpusamt, yq_corpusamt, corpusamt, payinteamt, fineamt, round((corpusamt + payinteamt + fineamt), 2)

    def data(self, productid, datetime0, datatime3, payamt, TASK_ID):  # productid
        '''
        533000004000001'--甜橙
        533010003000001'--还呗
        533000007000001'--拍拍贷
        533010015000001'--零花保
        '''

        number = {
            7014: "533000001000001",
            7015: "533000004000001",
            7017: "533010003000001",
            7018: "533000006000001"
        }
        b = time.strftime("%Y%m%d%H%M%S")
        serialno = b + '00000000000000' + str(random.randint(1000, 10000))
        a = self.zwzj_oracle.query_data(
                            "select a.customername,a.accountno,af.result_seq_no,a.putoutno from acct_loan a inner join acct_fund_apply af on a.apply_no = af.apply_no where serialno = '{}'".format(
                                self.loanNo))[0]
        data = f"{serialno}{number[productid]}533030001000001533020001000001{a[0]}{a[1]}{a[2]}{a[3]}805{self.datatime_cap(datetime0)}{payamt[2]}{payamt[3]}{payamt[4]}{payamt[5]}{self.datatime_cap(datatime3)}FINAL_CLAIM"
        ID = "46010001130" + str(random.randint(1000, 10000))
        sql = f"insert into acct_file_task_detail (ID, TASK_ID, ROW_NUM, LINE_CONTENT, DIFF_COLUMNS, PROCESS_STATUS, CREATE_USER, CREATE_TIME, UPDATE_USER, UPDATE_TIME, DIFF_MY_VALUES, ERROR_MESSAGE, BIZ_NO)values ({ID}, '{TASK_ID}', 1, '{data}', null, 2, 'system', to_date('03-10-2028', 'dd-mm-yyyy'), 'system', to_date('03-10-2028', 'dd-mm-yyyy'), null, null, '{a[3]}')"
        return data, sql

    def insert_data_acct_file_task_detail(self, statement):
        self.zwzj_oracle.insert_update_data(statement)

    def insert_data_acct_file_task(self, loan_numbers, task_id, datatime):
        statement = f"insert into acct_file_task (ID, BUSINESS_DATE, FUND_CODE, PRODUCT_CODE, ORG_ID, REQUEST_ID, FILE_CODE, FILE_PATH, FILE_NAME, FILE_SIZE, FILE_ROWS, STATUS, ERROR_CODE, ERROR_MESSAGE, CREATE_TIME, UPDATE_TIME, NEXT_STEP, ERROR_ROWS, PROCESS_TYPE) values ('{task_id}', '{datatime}', '787', null, null, '202103081124', 'ClaimApply', '/DBBX_KCXB_CLAIM/20281003/', 'INS_CLAIM_RESULT_DBBX_KCXB_20281002', null, '{loan_numbers}', 1, null, null, to_date('03-10-2028 09:52:14', 'dd-mm-yyyy hh24:mi:ss'), to_date('03-10-2028 09:52:15', 'dd-mm-yyyy hh24:mi:ss'), null, 0, 1)"
        self.zwzj_oracle.insert_update_data(statement)


def productid(zwzj_oracle, loanNo):
    sql = f"select businesstype from ACCT_PAYMENT_SCHEDULE where objectno = '{loanNo}'"
    productid = zwzj_oracle.query_data(sql)[0][0]
    return int(productid)


def get_db_config(environment):
    db = lambda path : yaml.load(open(path,encoding='utf-8'),Loader=yaml.SafeLoader)
    if environment == "sit":
        environment = db('../conf/Config.yaml')["xxhx_oracle"]["xxhx_sit_oracle"]
    elif environment == "uat":
        environment = db('../conf/Config.yaml')["xxhx_oracle"]["xxhx_uat_oracle"]
    else:
        print("环境选择错误，sit/uat！")
    return environment


def data():
    with open("../datas/CLAIM_RESULT_DATAS.yaml", encoding="utf-8") as f:
        datas = yaml.load(f, Loader=yaml.SafeLoader)  # 手动指定加载程序yaml.SafeLoader
    return datas


def main(environment,loanNo,day):
    log = my_log.Log()
    log.info("------开始执行------")
    # 借据笔数
    loan_numbers = len(loanNo)
    # 环境
    db_config = get_db_config(environment)
    # 数据库操作类
    zwzj_oracle = database_manipulation.Oracle_Class(db_config[0],db_config[1],db_config[2])
    # TASK_ID
    TASK_ID = "46010001130" + str(random.randint(1000, 10000))
    tab = True
    for loanNo in loanNo:

        CLAIM_RESULTS = CLAIM_RESULT(environment, loanNo, zwzj_oracle)
        # datetime0最早逾期期次还款日，datatime3理赔日
        # 最早逾期期次还款日
        try:
            datetime0 = zwzj_oracle.query_data(
                                        f"select paydate from acct_payment_schedule s  where s.objectno = '{loanNo}'and status = '12'")[
                0][0]
        except IndexError:
            log.error(f"借据需为逾期状态！{loanNo}")
            sys.exit()
        # 理赔日
        datatime3 = CLAIM_RESULTS.get_date(datetime0, day)
        # 各科目金额（正常本金，逾期本金，本金，利息，罚息，总和）
        payamt = CLAIM_RESULTS.Payamt(datatime3,day)
        log.info(
            f"借据号：{loanNo}，正常本金：{payamt[0]}，逾期本金：{payamt[1]}，本金：{payamt[2]}，利息：{payamt[3]}，罚息：{payamt[4]}，总和：{payamt[5]}")
        # 更新借据表中的逾期金额，正常金额
        log.info(f"更新acct_loan表逾期金额（{payamt[0]}）和正常金额（{payamt[1]}）")
        CLAIM_RESULTS.sql_update_acct_loan(payamt[0], payamt[1], loanNo)
        log.info("------更新成功------")
        # 生成申请文件数据
        datas = CLAIM_RESULTS.data(productid(zwzj_oracle, loanNo), datetime0, datatime3, payamt, TASK_ID)
        # datatime4 = CLAIM_RESULTS.datatime_cap(datatime3)
        # data插入acct_file_task_detail
        log.info("将数据插入acct_file_task_detail表")
        CLAIM_RESULTS.insert_data_acct_file_task_detail(datas[1])
        log.info("------插入成功------")
        if tab:
            # 更改acct_file_task表数据
            CLAIM_RESULTS.insert_data_acct_file_task(loan_numbers, TASK_ID, CLAIM_RESULTS.get_date(datatime3, -1))
            tab = False
        log.info(f"TASK_ID:{TASK_ID}")
        log.info(f"索赔日：{CLAIM_RESULTS.datatime_cap(datatime3)}")
        # 生成理赔申请文件，当前目录
        path = os.path.dirname(__file__)
        #微众文件
        with open(path + f"/INS_CLAIM_REQUEST_DBBX_KCXB_{CLAIM_RESULTS.datatime_cap(CLAIM_RESULTS.get_date(datatime3, -1))}",
                  mode="a") as h:
            h.write(datas[0] + '\n')
        #交行文件
        # with open(winreg.QueryValueEx(key, "Desktop")[
        #               0] + f"\CLAIM_RESULT_DBBX_KCXB_{CLAIM_RESULTS.datatime_cap(CLAIM_RESULTS.get_date(datatime3, -1))}",
        #           mode="a") as h:
        #     h.write(datas[0] + '\n')

        # with open(os.path.join(os.path.expanduser("~"), 'Desktop') + f"\CLAIM_RESULT_DBBX_KCXB_{datatime4}",mode="w") as h:
        #     h.write(datas[0])
    # 关闭数据库连接
    zwzj_oracle.close_all()
    log.info("理赔申请文件生成成功")


if __name__ == '__main__':
    datas = data()
    main(datas["environment"],datas["loanNo"],datas["day"])

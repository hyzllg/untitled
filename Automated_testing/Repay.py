import random
import time
import datetime
import requests
import cx_Oracle
import json
import Collect

import yaml
from past.builtins import raw_input








class Collects:


    # 计算两个日期相差天数，自定义函数名，和两个日期的变量名。
    def Caltime(self,date1, date2):
        # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
        # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        date1 = time.strptime(date1, "%Y/%m/%d")
        date2 = time.strptime(date2, "%Y/%m/%d")
        # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
        # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
        # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
        date1 = datetime.datetime(date1[0], date1[1], date1[2])
        date2 = datetime.datetime(date2[0], date2[1], date2[2])
        # 返回两个变量相差的值，就是相差天数
        return date2 - date1

    #查该数据账务数据库还款计划的更新时间
    def acct_payment_schedule_update_time(self,zw_cursor,loanNo,Period):
        sql = "select updated_date from ACCT_PAYMENT_SCHEDULE where objectno = '{}' and seqid = '{}'".format(loanNo, Period)
        a = Collect.sql_cha(zw_cursor,sql)
        c = str(list(a[0])[0])[0:10]
        c = c.replace("-", "")
        return c

    #同步微众最新还款计划
    def webankRepayPlanQueryTask(self):
        url = "http://10.1.14.191:26275/task/run/0006/webankRepayPlanQueryTask"
        data = {
            "cooperate": "787"
        }

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********同步微众还款计划接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(url, data=json.dumps(data), headers=headers)
        requit = re.json()
        print(f"响应报文：{requit}")


    #将2020/01/01更新成20200101格式
    def pay_time(self,time):
        a = time
        a = a.replace("/","")
        return a


    #判断改数据的还款计划是否是最新，如不是会去同步最新的还款计划
    def ifnow_update_time(self,zw_cursor,Period,loanNo,b,Pay_time):
        if Period[1] == "12" and int(b) != int(Pay_time):
            Collects().webankRepayPlanQueryTask()
            time.sleep(30)
            qqq = 0
            while qqq >= 8:
                if int(Collects().acct_payment_schedule_update_time(zw_cursor,loanNo,Period)) != int(Pay_time):
                    time.sleep(5)
                    break
                else:
                    print("还款计划未更新到最新！")

                qqq += 1
            if qqq >= 8:
                raw_input("Press <enter>")

class Set_time:
    def __init__(self, time,setting):
        self.time = time
        self.setting = setting
    def set_zw_time(self):
        url = r"http://10.1.14.191:26275/sys/setDate"
        params = {"date":"20210119"}
        params["date"] = self.time
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********改账务系统时间！**********"
        print(a)
        print(f"请求报文：{params}")
        re = requests.get(url, params=params, headers=headers)
        requit = re.json()
        print(f"请求报文：{requit}")
    def set_hx_time(self):
        b = self.time
        a = "**********改线上核心系统时间！**********"
        print(a)
        Collect.sql_update(self.setting,b,b)




class TC_repqy:
    def __init__(self,paytime,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor):
        self.paytime = paytime
        self.channelCustId = channelCustId
        self.loanNo = loanNo
        self.repayReqNo = repayReqNo
        self.Period = Period
        self.url = url
        self.repayType = repayType
        self.hx_cursor = hx_cursor
        self.zw_cursor = zw_cursor

    def ADVANCE_SETTLE_TRIAL(self):
        data = {
                "loanNo":"20190321151134175175",
                "channelCustId":"20190830002"
                }
        data["loanNo"] = self.loanNo
        data["channelCustId"] = self.channelCustId
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********甜橙提前结清接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "ADVANCE_SETTLE_TRIAL", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["body"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("甜橙提前结清接口！")
                repayAmt = requit["data"]["body"]["result"]["repayAmt"]
            else:
                print("甜橙提前结清接口失败！")
                print("{} {}".format(requit["data"]["body"]["errorCode"],requit["data"]["body"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit,repayAmt

    def PAYMENT_NOTICE(self,repayAmt):
        data = {
                "loanNo":"20190321151134175175",
                "channelCustId":"20190830002",
                "repayPeriod":1,
                "operateType":"00",
                "repayAmt":"11.11",
                "repayReqNo":"361706411",
                "repayType":"00",
                "transTime": "2021/06/02 16:46:59",
                "repayTime": "2021/06/02 16:46:59"
}
        data["loanNo"] = self.loanNo
        #核心查channelCustId
        data["channelCustId"] = self.channelCustId
        data["repayPeriod"] = self.Period
        data["repayAmt"] = repayAmt
        data["repayReqNo"] = self.repayReqNo
        data["repayType"] = self.repayType
        data["transTime"] = "{} 13:14:00".format(self.paytime)
        data["repayTime"] = "{} 13:14:00".format(self.paytime)

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********甜橙还款通知接口接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "PAYMENT_NOTICE", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["body"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("甜橙还款通知接口成功！")
            else:
                print("甜橙还款通知接口失败！")
                print("{} {}".format(requit["data"]["body"]["errorCode"],requit["data"]["body"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")


    def pay(self):
        # 判断该借据是否逾期
        acct_loan_type = Collect.sql_cha(self.zw_cursor,"select loanstatus From acct_loan a where a.serialno = '{}'".format(self.loanNo))[0][0]
        if self.repayType == "01":
            repayAmt = self.ADVANCE_SETTLE_TRIAL()
            self.PAYMENT_NOTICE(repayAmt[-1])
        elif self.repayType == "00":
            if acct_loan_type == "0":
                print("借据为正常状态！")
                # 查询借据最远未还期次信息
                normal_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                #判断是否是还款日，如不是则不能做还款
                if int(Collects().pay_time(normal_ACCT_PAYMENT_SCHEDULE[2])) == int(Collects().pay_time(self.paytime)):
                    repayamt = round(normal_ACCT_PAYMENT_SCHEDULE[3]+normal_ACCT_PAYMENT_SCHEDULE[4]+normal_ACCT_PAYMENT_SCHEDULE[5]+normal_ACCT_PAYMENT_SCHEDULE[6]+normal_ACCT_PAYMENT_SCHEDULE[7],2)
                    print(f"还款金额：{repayamt}")
                    self.PAYMENT_NOTICE(repayamt)
                else:
                    print("不能做提前还当期操作！")

            elif acct_loan_type == "1":
                print("借据为逾期状态！")
                overdue = []
                overdueamt = 0
                overdue_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor ,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                overdueamt = round(overdue_ACCT_PAYMENT_SCHEDULE[3] + overdue_ACCT_PAYMENT_SCHEDULE[4] + overdue_ACCT_PAYMENT_SCHEDULE[5] + overdue_ACCT_PAYMENT_SCHEDULE[6] + overdue_ACCT_PAYMENT_SCHEDULE[7],2)
                print(f"还款金额：{overdueamt}")
                self.PAYMENT_NOTICE(overdueamt)



            elif acct_loan_type in ["10","20","30"]:
                print("借据为结清状态！")
        else:
            print("还款类型有误！")


class PP_repqy:
    def __init__(self,paytime,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor):
        self.paytime = paytime
        self.channelCustId = channelCustId
        self.loanNo = loanNo
        self.repayReqNo = repayReqNo
        self.Period = Period
        self.repayType = repayType
        self.url = url
        self.hx_cursor =hx_cursor
        self.zw_cursor = zw_cursor

    def ADVANCE_SETTLE_TRIAL(self):
        data = {
                "loanNo":"20190321151134175175",
                "channelCustId":"20190830002"
                }
        data["loanNo"] = self.loanNo
        data["channelCustId"] = self.channelCustId
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********拍拍提前结清试算接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "ADVANCE_SETTLE_TRIAL", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("拍拍提前结清试算接口成功！")
                repayAmt = requit["data"]["result"]["repayAmt"]

            else:
                print("拍拍提前结清试算接口失败！")
                print("{} {}".format(requit["data"]["errorCode"],requit["data"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit,repayAmt

    def PAYMENT_NOTICE(self,repayAmt):
        data = {
                "channelCustId":"",
                "repayReqNo":"202002202002200222",
                "loanNo":"202002202002200220",
                "repayPeriod":"3",
                "repayAmt":1.66,
                "repayType":"00",
                "operateType":"00",
                "payChannel":"01",
                "transTime":"2021/02/02 10:00:00",
                "repayTime":"2021/02/02 10:00:00",
                "adRepayAmt":0,
                "adRepayChannel":"01"
}
        data["loanNo"] = self.loanNo
        #核心查channelCustId
        data["channelCustId"] = self.channelCustId
        data["repayPeriod"] = self.Period
        data["repayAmt"] = repayAmt
        data["repayReqNo"] = self.repayReqNo
        data["repayType"] = self.repayType
        data["transTime"] = "{} 13:14:00".format(self.paytime)
        data["repayTime"] = "{} 13:14:00".format(self.paytime)

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********拍拍还款通知接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "PAYMENT_NOTICE", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("拍拍还款通知接口成功！")
            else:
                print("拍拍还款通知接口失败！")
                print("{} {}".format(requit["data"]["errorCode"],requit["data"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit

    def pay(self):
        # 判断该借据是否逾期
        acct_loan_type = Collect.sql_cha(self.zw_cursor,"select loanstatus From acct_loan a where a.serialno = '{}'".format(self.loanNo))[0][0]
        if self.repayType == "01":
            repayAmt = self.ADVANCE_SETTLE_TRIAL()
            self.PAYMENT_NOTICE(repayAmt[-1])
        elif self.repayType == "00":
            if acct_loan_type == "0":
                print("借据为正常状态！")
                # 查询借据最远未还期次信息
                normal_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                #判断是否是还款日，如不是则不能做还款
                if int(Collects().pay_time(normal_ACCT_PAYMENT_SCHEDULE[2])) == int(Collects().pay_time(self.paytime)):
                    repayamt = round(normal_ACCT_PAYMENT_SCHEDULE[3]+normal_ACCT_PAYMENT_SCHEDULE[4]+normal_ACCT_PAYMENT_SCHEDULE[5]+normal_ACCT_PAYMENT_SCHEDULE[6]+normal_ACCT_PAYMENT_SCHEDULE[7],2)
                    print(f"还款金额：{repayamt}")
                    self.PAYMENT_NOTICE(repayamt)
                else:
                    print("不能做提前还当期操作！")

            elif acct_loan_type == "1":
                print("借据为逾期状态！")
                overdue = []
                overdueamt = 0
                overdue_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor ,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                overdueamt = round(overdue_ACCT_PAYMENT_SCHEDULE[3] + overdue_ACCT_PAYMENT_SCHEDULE[4] + overdue_ACCT_PAYMENT_SCHEDULE[5] + overdue_ACCT_PAYMENT_SCHEDULE[6] + overdue_ACCT_PAYMENT_SCHEDULE[7],2)
                print(f"还款金额：{overdueamt}")
                self.PAYMENT_NOTICE(overdueamt)



            elif acct_loan_type in ["10","20","30"]:
                print("借据为结清状态！")
        else:
            print("还款类型有误！")


class HB_repqy:
    def __init__(self,paytime,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor):
        self.paytime = paytime
        self.loanNo = loanNo
        self.repayReqNo = repayReqNo
        self.Period = Period
        self.repayType = repayType
        self.url = url
        self.hx_cursor = hx_cursor
        self.zw_cursor = zw_cursor

    def ADVANCE_SETTLE_TRIAL(self):
        data = {
                "loanNo":"20190321151134175175",
                "channelCustId":""
                }
        data["loanNo"] = self.loanNo
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********还呗提前结清接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "ADVANCE_SETTLE_TRIAL", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            print(requit)
            if requit["data"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("还呗提前结清试算接口成功！")
                repayAmt = requit["data"]["result"]["repayAmt"]

            else:
                print("还呗提前结清接口失败！")
                print("{} {}".format(requit["data"]["errorCode"],requit["data"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit,repayAmt

    def PAYMENT_NOTICE(self,repayAmt):
        data = {
                    "channelCustId":"",
                    "repayReqNo":"202002202002200222",
                    "loanNo":"202002202002200220",
                    "repayPeriod":"3",
                    "coupon":0,
                    "repayAmt":1.66,
                    "repayType":"00",
                    "operateType":"00",
                    "payChannel":"01",
                    "payReqNo":"",
                    "transTime":"2020/10/20 13:14:00",
                    "repayTime":"2020/10/20 13:14:15"
                }
        data["loanNo"] = self.loanNo
        #核心查channelCustId
        data["repayPeriod"] = self.Period
        data["repayAmt"] = repayAmt
        data["repayReqNo"] = self.repayReqNo
        data["repayType"] = self.repayType
        data["transTime"] = "{} 13:14:00".format(self.paytime)
        data["repayTime"] = "{} 13:14:00".format(self.paytime)

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********还呗还款通知接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "PAYMENT_NOTICE", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("还呗还款通知接口成功！")
            else:
                print("还呗还款通知接口失败！")
                print("{} {}".format(requit["data"]["errorCode"],requit["data"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit

    def pay(self):
        # 判断该借据是否逾期
        acct_loan_type = Collect.sql_cha(self.zw_cursor,"select loanstatus From acct_loan a where a.serialno = '{}'".format(self.loanNo))[0][0]
        if self.repayType == "01":
            repayAmt = self.ADVANCE_SETTLE_TRIAL()
            self.PAYMENT_NOTICE(repayAmt[-1])
        elif self.repayType == "00":
            if acct_loan_type == "0":
                print("借据为正常状态！")
                # 查询借据最远未还期次信息
                normal_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                #判断是否是还款日，如不是则不能做还款
                if int(Collects().pay_time(normal_ACCT_PAYMENT_SCHEDULE[2])) == int(Collects().pay_time(self.paytime)):
                    repayamt = round(normal_ACCT_PAYMENT_SCHEDULE[3]+normal_ACCT_PAYMENT_SCHEDULE[4]+normal_ACCT_PAYMENT_SCHEDULE[5]+normal_ACCT_PAYMENT_SCHEDULE[6]+normal_ACCT_PAYMENT_SCHEDULE[7],2)
                    print(f"还款金额：{repayamt}")
                    self.PAYMENT_NOTICE(repayamt)
                else:
                    print("不能做提前还当期操作！")

            elif acct_loan_type == "1":
                print("借据为逾期状态！")
                overdue = []
                overdueamt = 0
                overdue_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor ,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                overdueamt = round(overdue_ACCT_PAYMENT_SCHEDULE[3] + overdue_ACCT_PAYMENT_SCHEDULE[4] + overdue_ACCT_PAYMENT_SCHEDULE[5] + overdue_ACCT_PAYMENT_SCHEDULE[6] + overdue_ACCT_PAYMENT_SCHEDULE[7],2)
                print(f"还款金额：{overdueamt}")
                self.PAYMENT_NOTICE(overdueamt)



            elif acct_loan_type in ["10","20","30"]:
                print("借据为结清状态！")
        else:
            print("还款类型有误！")


class QY_repqy:
    def __init__(self,paytime,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor):
        self.paytime = paytime
        self.channelCustId = channelCustId
        self.loanNo = loanNo
        self.repayReqNo = repayReqNo
        self.Period = Period
        self.repayType = repayType
        self.url = url
        self.hx_cursor = hx_cursor
        self.zw_cursor = zw_cursor

    def PAYMENT_NOTICE(self,repayAmt,principal,interest):
        data = {
                "channelCustId":"",
                "repayReqNo":"202002202002200222",
                "loanNo":"202002202002200220",
                "repayType":"00",
                "repayPeriod":"1",
                "repayAmt":0.00,
                "principal":0.00,
                "interest":0.00,
                "penInterest":0.00,
                "operateType":"00",
                "fullPayFlag":"01",
                "payChannel":"01",
                "payReqNo":"",
                "couponAmount":0,
                "redReduceAmount":0
            }
        data["loanNo"] = self.loanNo
        # data["channelCustId"] = self.channelCustId
        data["repayPeriod"] = self.Period
        data["repayAmt"] = repayAmt
        data["repayReqNo"] = self.repayReqNo
        data["repayType"] = self.repayType
        data["principal"] = principal
        data["interest"] = interest

        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "10.1.14.106:27405",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
        }
        a = "**********360还款通知接口！**********"
        print(a)
        print(f"请求报文：{data}")
        re = requests.post(self.url + "PAYMENT_NOTICE", data=json.dumps(data), headers=headers)
        requit = re.json()
        if re.status_code == 200 and requit["result"] == True:
            requit["data"] = eval(requit["data"])
            if requit["data"]["status"] == '01':
                print(f"响应报文：{requit}")
                print("360还款通知接口成功！")
            else:
                print("360还款通知接口失败！")
                print("{} {}".format(requit["data"]["errorCode"],requit["data"]["errorMsg"]))
        else:
            print("msg:{}".format(requit["msg"]))
            raw_input("Press <enter>")
        return a, requit

    def pay(self):
        # 判断该借据是否逾期
        acct_loan_type = Collect.sql_cha(self.zw_cursor,"select loanstatus From acct_loan a where a.serialno = '{}'".format(self.loanNo))[0][0]
        # 未还本金
        principal = round(sum(Collect.sql_cha(self.zw_cursor,"select normalbalance,overduebalance from acct_loan where serialno = '{}'".format(self.loanNo))[0]), 2)

        if self.repayType == "01":

            if acct_loan_type == "0":
                lon_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.intedate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                #天数
                days = Collects().Caltime(lon_ACCT_PAYMENT_SCHEDULE[3],self.paytime).days
                #息费
                interest = round((lon_ACCT_PAYMENT_SCHEDULE[5] + lon_ACCT_PAYMENT_SCHEDULE[8]) / 30 * days,2)
                repayamt = round(principal+interest,2)
                print(f"还款金额：{repayamt}")
                self.PAYMENT_NOTICE(repayamt,principal,interest)
            elif acct_loan_type == "1":
                amt = 0
                overdue_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and a.status = '12'".format(
                                                                                          self.loanNo))
                for i in overdue_ACCT_PAYMENT_SCHEDULE:
                    a = round(i[4]+i[5]+i[6]+i[7],2)
                    amt += a

                a = Collect.sql_cha(self.zw_cursor,"select a.seqid,a.status,a.paydate,a.intedate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 from ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status = '11'".format(self.loanNo))
                #天数
                days = Collects().Caltime(a[3],self.paytime).days
                interest = round((a[5]+a[8]) / 30 * days + amt,2)
                repayamt = round(interest+principal,2)
                print(f"还款金额：{repayamt}")
                self.PAYMENT_NOTICE(repayamt,principal,interest)




        elif self.repayType == "00":
            if acct_loan_type == "0":
                print("借据为正常状态！")
                # 查询借据最远未还期次信息
                normal_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))
                #判断是否是还款日，如不是则不能做还款
                if int(Collects().pay_time(normal_ACCT_PAYMENT_SCHEDULE[2])) == int(Collects().pay_time(self.paytime)):

                    repayamt = round(normal_ACCT_PAYMENT_SCHEDULE[3]+normal_ACCT_PAYMENT_SCHEDULE[4]+normal_ACCT_PAYMENT_SCHEDULE[5]+normal_ACCT_PAYMENT_SCHEDULE[6]+normal_ACCT_PAYMENT_SCHEDULE[7],2)
                    principal = round(normal_ACCT_PAYMENT_SCHEDULE[3],2)
                    interest = round(normal_ACCT_PAYMENT_SCHEDULE[4]+normal_ACCT_PAYMENT_SCHEDULE[5]+normal_ACCT_PAYMENT_SCHEDULE[6]+normal_ACCT_PAYMENT_SCHEDULE[7],2)
                    print(f"还款金额:{repayamt}")
                    self.PAYMENT_NOTICE(repayamt,principal,interest)
                else:
                    print("不能做提前还当期操作！")

            elif acct_loan_type == "1":
                print("借据为逾期状态！")
                overdue = []
                overdueamt = 0
                overdue_ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(self.zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(self.loanNo))[0]
                overdueamt = round(overdue_ACCT_PAYMENT_SCHEDULE[3] + overdue_ACCT_PAYMENT_SCHEDULE[4] + overdue_ACCT_PAYMENT_SCHEDULE[5] + overdue_ACCT_PAYMENT_SCHEDULE[6] + overdue_ACCT_PAYMENT_SCHEDULE[7],2)
                principal = round(overdue_ACCT_PAYMENT_SCHEDULE[3],2)
                interest = round(overdue_ACCT_PAYMENT_SCHEDULE[4]+overdue_ACCT_PAYMENT_SCHEDULE[5]+overdue_ACCT_PAYMENT_SCHEDULE[6]+overdue_ACCT_PAYMENT_SCHEDULE[7],2)
                print(f"还款金额：{overdueamt}")
                # for i in a:
                #     list(i)
                #     overdue.append(i)
                # for i in overdue:
                #     a = i[3]+i[4]+i[5]+i[6]+i[7]
                #     overdueamt += a
                self.PAYMENT_NOTICE(overdueamt,principal,interest)



            elif acct_loan_type in ["10","20","30"]:
                print("借据为结清状态！")
        else:
            print("还款类型有误！")

def datas():
    with open("Repay.yaml", encoding="utf-8") as f:
        datas = yaml.load(f, Loader=yaml.SafeLoader)
        return  datas

def channelCust(hx_cursor,loanNo):
    data = Collect.sql_cha(hx_cursor,"select channelcustid from channel_apply_info where creditreqno = (select creditreqno from putout_approve where relativeobjectno = '{}')".format(
                                               loanNo))[0][0]
    return data

def main():
    print("------开始执行------")

    data = datas()
    environment = data["environment"]
    loanNo = data["loanNo"]
    Pay_time = data["Pay_time"]
    repayType = data["repayType"]
    #测试环境及数据库配置
    hx_ORACLE = data[environment]["oracle"]["hx_oracle"]
    hx_conn = cx_Oracle.connect(hx_ORACLE[0], hx_ORACLE[1], hx_ORACLE[2])
    hx_cursor = hx_conn.cursor()
    zw_ORACLE = data[environment]["oracle"]["zw_oracle"]
    zw_conn = cx_Oracle.connect(zw_ORACLE[0], zw_ORACLE[1], zw_ORACLE[2])
    zw_cursor = zw_conn.cursor()


    prodect = Collect.sql_cha(hx_cursor,"select a.productid from acct_loan a where a.serialno = '{}'".format(loanNo))[0][0]
    url = data[environment]["url"][int(prodect)]
    #channelCustId
    channelCustId = channelCust(hx_cursor,loanNo)
    #repayReqNo
    repayReqNo = Collect.creditReqNo()
    # 查询借据最远未还期次信息
    ACCT_PAYMENT_SCHEDULE = Collect.sql_cha(zw_cursor,"SELECT a.seqid,a.status,a.paydate,a.paycorpusamt,a.payinteamt,a.payfineamt,a.paycompdinteamt,a.payfeeamt1 FROM ACCT_PAYMENT_SCHEDULE a where objectno = '{}' and status in (11,12)".format(loanNo))[0]
    # print(ACCT_PAYMENT_SCHEDULE)
    Period = ACCT_PAYMENT_SCHEDULE[0]
    Paydate = ACCT_PAYMENT_SCHEDULE[2]
    # 改系统时间
    Set_time(Pay_time,hx_ORACLE).set_zw_time()
    Set_time(Pay_time,hx_ORACLE).set_hx_time()
    #判断还款计划是否是最新
    # b = Collects().acct_payment_schedule_update_time(zw_cursor,loanNo,Period)
    # Collects().ifnow_update_time(zw_cursor,ACCT_PAYMENT_SCHEDULE,loanNo,b,Collects().pay_time(Pay_time))


    if prodect == "7014":
        hyzllg = TC_repqy(Pay_time,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor)
        hyzllg.pay()
    elif prodect == "7018":
        hyzllg = PP_repqy(Pay_time,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor)
        hyzllg.pay()
    elif prodect == "7017":
        hyzllg = HB_repqy(Pay_time,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor)
        hyzllg.pay()
    elif prodect == "7015":
        hyzllg = QY_repqy(Pay_time,channelCustId,loanNo,repayReqNo,Period,repayType,url,hx_cursor,zw_cursor)
        hyzllg.pay()

if __name__ == '__main__':
    main()





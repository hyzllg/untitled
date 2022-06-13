import json
import os
import re
import yaml
import requests
import dadi_project.utils.database_manipulation
import dadi_project.utils.my_log
import dadi_project.utils.server_linux
from dadi_project.utils import server_linux,database_manipulation,my_log


class Collection_File:

    def __init__(self, connect, ser_conf, policyno, datetime, url_conf):
        self.connect = connect
        self.policyno = policyno
        self.datetime = datetime
        self.ser_conf = ser_conf
        self.url_conf = url_conf


    def oracle_update(self):
        print("更新数据库信息！")
        if isinstance(self.policyno,list):
            for i in self.policyno:
                sqls = [f"UPDATE BUSINESS_APPLY ba SET ba.LOANSERIALNO = (SELECT al.SERIALNO FROM ACCT_LOAN al WHERE al.PUTOUTNO = ba.POLICYNO )WHERE ba.POLICYNO in('{i}')",
                f"update prpjp p set p.updatetime = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where p.policyno = '{i}'",
                f"update business_intfgl bi set bi.intf_process_date = sysdate where attribute6 = '{i}'",
                f"update acct_loan al set al.customerid = (select customerid from business_apply where policyno=al.putoutno) where putoutno = '{i}'",
                f"update acct_loan al set al.updated_date = sysdate where putoutno = '{i}'",
                f"update acct_payment_schedule a set a.updated_date = sysdate where objectno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update acct_recovery_loss a set a.updated_date = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where serialno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update acct_transaction a set a.updated_date = sysdate where a.relativeserialno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update acct_back_bill a set a.updated_date = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where objectno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update acct_back_detail a set a.updated_date = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where loanserialno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update customer_info set updated_date = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where customerid in (select al.customerid from acct_loan al where al.putoutno in ('{i}'))",
                f"update customer_work set modifytime = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where customerid in (select al.customerid from acct_loan al where al.putoutno in ('{i}'))",
                f"update ind_info a set a.modifytime = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where customerid in (select al.customerid from acct_loan al where al.putoutno in ('{i}'))",
                f"update ACCT_PAYMENT_SCHEDULE_claim a set a.updated_date = sysdate where objectno = (select serialno from acct_loan where putoutno = '{i}')",
                f"update CLAIMAMTINFO a set a.updatetime = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where lnsacct = (select serialno from acct_loan where putoutno = '{i}')",
                f"update cuishou_tel a set a.updatedate = to_char(sysdate,'yyyy/MM/dd hh24:mi:ss') where customerid in (select al.customerid from acct_loan al where al.putoutno in ('{i}'))",
                f"update CUSTOMER_LINK a set a.updatetime = sysdate where customerid in (select al.customerid from acct_loan al where al.putoutno in ('{i}'))"]
                print(sqls)
                for con in sqls:
                    self.connect.insert_update_data(con)
        else:
            print("保单号必须是列表形式！")
    def UpdateAL(self):
        for i in self.policyno:
            Cooperate = self.connect.query_data(f"select cooperate from acct_loan where putoutno = '{i}'")[0][0]
            server_linux.Operate_Server(hostname=self.ser_conf[0], port=self.ser_conf[1], username=self.ser_conf[2], password=self.ser_conf[3]).run(
                command = f"cd /ccicall/Applog/task-data/;sh UpdateALOverStage.sh {Cooperate},{i},{self.datetime}")

    def res_CollectionFile(self):
        if len(self.policyno) == 1:
            da = self.connect.query_data(f"select cooperate,serialno from acct_loan where putoutno in '{self.policyno[0]}'")
        else:
            da= self.connect.query_data(f"select cooperate,serialno from acct_loan where putoutno in {tuple(self.policyno)}")
        datas = {}
        for i in da:
            try:
                datas[i[0]].append(i[1])
            except:
                datas[i[0]] = []
                datas[i[0]].append(i[1])
                continue
        for Cooperate in datas.keys():

            data = {
            "Cooperate": Cooperate,
            "LoanNo": datas[Cooperate],
            "Date": re.sub('/','',self.datetime)
                                }
            print(self.url_conf['CollectionFile'])
            print(data)
            result = requests.post(self.url_conf['CollectionFile'],data=json.dumps(data))
            print(result.json())

    # def xx_get_files(self,remoteDir,localDir):
    #     server_linux.Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password='ccicall').download_files(
    #         remoteDir, localDir)
    # def cs_put_files(self,remoteDir,localDir):
    #     server_linux.Operate_Server(hostname="10.1.12.42", port=22, username="ccicall", password='ccicall').download_files(
    #         remoteDir, localDir)




def get_conf(oracle_cf,environment,xx_server_cf,cs_server_cf,url_cf):

    if environment == "SIT":
        oracle_conf = oracle_cf['xxhx_sit_oracle']
        url_conf = url_cf['sit_url']
        cs_server_cf = cs_server_cf['cs_sit_server']
    elif environment == "UAT":
        oracle_conf = oracle_cf['xxhx_uat_oracle']
        url_conf = url_cf['uat_url']
        cs_server_cf = cs_server_cf['cs_uat_server']
    else:
        raise ValueError("异常")
    return oracle_conf,xx_server_cf['lhx_server'],cs_server_cf,url_conf

def main(environment,policyno,datetime):
    log = my_log.Log()
    get_yaml_data = lambda path: yaml.load(open(path, encoding='utf-8'), Loader=yaml.SafeLoader)
    path = os.path.dirname(os.path.dirname(__file__))
    url_cf = get_yaml_data(f'{path}/conf/url_res/api_lhx_url.yaml')
    oracle_cf = get_yaml_data(f'{path}/conf/oracle/xxhx_oracle.yaml')
    xx_server_cf = get_yaml_data(f'{path}/conf/server/lhx_server.yaml')
    cs_server_cf = get_yaml_data(f'{path}/conf/server/cs_server.yaml')
    #主机文件保存位置
    # 获取数据库配置
    conf = get_conf(oracle_cf, environment,xx_server_cf,cs_server_cf,url_cf)
    or_connect = database_manipulation.Oracle_Class(conf[0][0], conf[0][1], conf[0][2])
    xx_ser_conf = conf[1]
    cs_ser_conf = conf[2]
    url_conf = conf[3]
    hyz = Collection_File(or_connect,xx_ser_conf,policyno,datetime,url_conf)
    hyz.oracle_update()
    hyz.UpdateAL()
    hyz.res_CollectionFile()
    #下载主机文件
    localDir = os.path.dirname(__file__) + fr'\{re.sub("/","",datetime)}\\'[:-1]
    xx_remoteDir = f'/ccicall/sftp/cuishoufile/{re.sub("/","",datetime)}/'
    cs_remoteDir = f'/tomcat/apps/server/ccmsbatchfile/input/host1/{re.sub("/","",datetime)}/'
    log.info("******开始下载主机文件******")
    server_linux.Operate_Server(hostname=xx_ser_conf[0], port=xx_ser_conf[1], username=xx_ser_conf[2], password=xx_ser_conf[3]).download_files(
        xx_remoteDir, localDir)
    #上传主机文件到催收服务器
    log.info("******开始上传主机文件******")
    server_linux.Operate_Server(hostname=cs_ser_conf[0], port=cs_ser_conf[1], username=cs_ser_conf[2], password=cs_ser_conf[3]).put_files(
        cs_remoteDir, localDir)


if __name__ == '__main__':
    environment = 'SIT'
    policyno = ["PBLG202231171845000442"]
    datetime = '2022/05/18'
    main(environment.upper(),policyno,datetime)

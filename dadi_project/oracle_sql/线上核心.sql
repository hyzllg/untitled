--改系统时间
select * from system_setup;
update system_setup set businessdate = '2022/05/11',batchdate = '2022/05/11' where systemid = '1';
--标准查码值
SELECT * FROM CODE_LIBRARY where codeNo='EducateLevelCode';  --学历
SELECT * FROM CODE_LIBRARY where codeNo='MarryStatus';  --婚姻状况
SELECT * FROM CODE_LIBRARY where codeNo='RealNameStatus';  --获客渠道
select * from code_library c where c.codeno in('ShowState');
SELECT * FROM CODE_LIBRARY where codeNo='LoanStatus';  --贷款状态
--住宅区域码表
select * from CODE_AREA;
--基础产品管理
select * from PRODUCT_TERM_INFO pt where pt.productid = '7018' and term = '6';
--拍拍贷客户等级上下限
select t.itemno , t.attribute1 , t.attribute2 from code_library t  where codeno ='PaiPaiDai';
--还呗折后利率
select t.itemno , t.attribute1 , t.attribute2  from code_library t  where codeno ='HuanbeiArte';
--甜橙定制信息
select * from ORANGE_PARTNER_INFO where creditreqno = '20210929886881001';
--拍拍特有信息
select * from PPDAI_CHANNEL_DETAIL;
--360定制信息
select CUSTGRADE from FINANCE360_CHANNEL_DETAIL where creditreqno = '2021102319050979012';
--服务节点异常后落库记录
select * from exception_log_count where SERVICENAME = 'QueryCreditInfoOcr';
--理赔知会短信发送后落库记录
-- select * from TASK_EXECUTION_STATISTICS;
--改当日送线下报收付费
select * from offlinerecord where bacthno = '20210926000001_03';
-- --额度平台在途件（在途后再次申请，报错时查）
-- select * from loan_credit_records where id_card='320681198909240017' and status='0';
-- --额度状态表
-- select * from loan_limit where id_card='410102199007183213';
--渠道信息
select * from channel_apply_info where creditreqno ='2020120410404386556';
select * from channel_apply_info where customerid ='320000000005694' ;
select ca.channelcustid,ca.creditreqno,pa.channelputoutsno from channel_apply_info ca,putout_approve pa where ca.creditreqno = pa.creditreqno and ca.customerid = '320000001248250'
--授信信息
select * from business_apply where customerid ='320000001242026';
--支用信息
select * from putout_approve where serialno = '20211027000004001';
select * from putout_approve where CUSTOMERID = '320000001248791';
--联系人信息
select * from CUSTOMER_TEL where customerid = '320000000666413' and serialno like '20210917%';
select * from customer_tel where applyno='20210917000000002';
--实名流水
select *from customer_realname where regid ='320000000031323';
select *from customer_realname_log where regid ='20201202000002005';
--核心流程节点配置
select * from  queue_model where modelno ='BizApplyPay';
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202202090000000005'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20220420000000004'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc for update;
select count(*) from queue_task where runstatus = 'ST';
select * from PUTOUT_APPROVE;
select * from PUTOUT_APPROVE_LOG;
-- select * from queue_task where ITEM = 'CapitalPutoutQuery';
--批单表
select * from INSURANCEPOLICY_CHANGE_RECODE where policyno = 'PBLG202031170359000178';
--缩期还款计划
select * from acct_payment_schedule where objectno = '787-330000197502085197';
--不缩期还款计划
select * from acct_payment_schedule_not where objectno = '787-503905313301880886';
select * from acct_payment_schedule_not where finishdate is not null;

--还款通知
select * from loan_batch_notice where billno='787-330000197502085197' for update;--787-503903293301877867 \ 787-503903283301877660 320000000660821
select * from loan_batch_notice where repaystatus = '02' and subproduct = '7014'; 
select REPAYSTATUS from ALL_REPAY_SERIAL;
select * from REPAY_SERIAL;
--还款记录
select * from loan_batch_info where objectno='787-503903283301877660' --for update;
select * from loan_batch_info where objectno='20062-W210923004201302';
--对公还款
select * from CORP_ACCOUNT_RECORD
--扣款记录
select * from loan_batch_cutpayment where billno='787-503903283301877660';
--查还款交易类型
SELECT operatetype FROM loan_batch_notice where billno in ('787-503403193301772087','');
--总欠记录
select * from CLAIM_PAYMENT_SCHEDULE where OBJECTNO = '787-503005073301597532';
--清数据
delete from customer_info c where c.certid = '412702199810032718';
delete from customer_info c where c.customerid = '320000000014432';
delete from CUSTOMER_BANK_CARD where customerid = '320000000014432';
delete from CHANNEL_APPLY_INFO where customerid ='320000000014432';
delete from CHANNEL_APPLY_INFO where idno = '412702199810032718';
delete from customer_realname c where c.certid = '412702199810032718';
delete from customer_realname_log c where c.certid = '412702199810032718';
delete from business_apply where customerid = '320000001228058';
delete from ORANGE_PARTNER_INFO where customerid = '320000000014432';
delete from INSURE_SERIAL where idno = '412702199810032718';
delete from putout_approve where customerid ='320000000014432';
delete from BUSINESS_INSURANCEPOLICYINFO where customerid ='320000000014432';
delete from acct_loan where customerid = '320000000014432';
delete FROM PFA_INSURANCEPOLICYINFO where CHANNELPUTOUTAPPROVENO='320000000014432';

-------风控相关-------
--四要素成功落库
select * from CUSTOMER_BANK_CARD where PUTOUTAPPROVENO = '20211110000000008';
select * from CUSTOMER_BANK_CARD where CUSTOMERID = '320000001253325';
update customer_bank_card set updatetime = '2022/04/17' where serialno = '20220418000000012';
delete CUSTOMER_BANK_CARD where CUSTOMERID = '320000001234146';

--四要素是否调用
select * from customer_auth where certid='65322420090421440X';
select * from CUSTOMER_AUTH where customerid = '320000001253323';
select * from CUSTOMER_AUTH where APPLYSERIALNO = '20211112000000001';
select * from CUSTOMER_AUTH where phase = '1';
select * from CUSTOMER_AUTH where result = '2';
select ba.SERIALNO,ca.* from CUSTOMER_AUTH ca left join BUSINESS_APPLY ba on ca.SERIALNO=ba.SERIALNO left join CHANNEL_APPLY_INFO cai on ba.CHANNELAPPLYNO=cai.SERIALNO
where cai.SERIALNO = '202111100000000012';
--四要素是否复用
select * from third_relative where customerid = '320000001233903' and OBJECTNO = '20211110000000008';
select * from third_relative where phase = '1';
--三要素结果落库
select * from PHONETHREE_VERITY_RESULT where applyno = '202111150000000001';


--OCR识别
select * from ocr_operate_record where customerid = '320000000034108';
--人脸照片
select * from IMAGE_LIST where CUSTOMERID = '20200826000002008';
--黑瞳复用
select * from third_relative where customerid = '320000000670153';
--黑瞳调用
select * from HEITONG_RESULT WHERE customerid = '320000001232004';
--黑瞳高危
select * from heitong_high_risk where OBJECT_NO = '20211028000002007';
select * from trans_log where applyno = '20211022000002004' and Servicename = 'HeiTongAntiFraudService';
--ilog5,ilog9人行数据落库
select * from ED_ILOG_PBOC_DATA where REPORTNO = '2021102610021207445' and serialno = '20211026000004011';
--ilog规则集结果
SELECT * FROM ILOG_RULES_RESULT c WHERE c.applyno = '202204260000000001';
--法院限高调用记录
select * from COURT_HEIGHT_LIMIT where object_no = '202108040000006005';
--北冥接口
select * from brain_personspecial where customerid = '320000000662522';
--认证项结果落表
--公安网 公安简项
select * from NCIICLIST where idcard ='340506199207219515'  order by update_time desc;
select * from NCIICLIST where SERIALNO IN ('A03842BF82B4478E864D4C00F39CF080','C32A1A581A194B0183BB9D67D11CDCC2');
--核身结果落表
select *from FACEID_LIVENESS where customerid ='20201202000002005';
--互金信息
select * from ILOG_HJ_INFO WHERE APPLY_NO ='202103190000000004';
--对应的ILOG_HJ_INFO的主键
select * from ILOG_HJ_INFO_query WHERE HJ_SERIALNO ='20210319000000009';
--百融
select * from BRAIN_RULESPECIALLIST  where customerid= '320000000670361' or applyno = '20210318000002011'  order by create_time desc;
select * from BRAIN_SPECIALLIST where customerid= '320000000670361' or applyno = '20210318000002011'  order by create_time desc;
--北溟
select * from BRAIN_PERSONSPECIAL where applyno = '202104160000000002'  order by querytime desc;
--关联影像
insert into image_list (SERIALNO, IMGID, BUSINESSNO, IMGTYPE, IMGTYPENAME, VALIDFLAG, PICNAME, PICCLASS, PICDETAILS, PICPATH, THUMBNAILPATH, CREATE_DATE, UPDATE_DATE, BUSINESSDATE, APPLYNO, REALNAMEKEYNO, PICORDER, SIGNLOANNO, IMAGESTAGE, CHANNELAPPLYNO, CUSTOMERID, BILLNO)
values ('DF3B02E6AD474039B54A61114D824465', '3256765', '322000000001435', '|UWB438|', '|人脸识别图片|', '1', null, null, null, null, null, to_date('22-03-2021 00:00:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-03-2021 00:00:00', 'dd-mm-yyyy hh24:mi:ss'), '20210322', '', null, null, null, null, '202106100000000009', null, null);


--测还呗产品影像时改拉取远程路径
select * from code_library cl where cl.codeno ='ImagetPayApply';
update code_library set attribute2 = '/sftp/ccic/income/upload/image' where codeno ='ImagetPayApply';
update code_library set attribute2 = '/ccicall/cfs/test/file' where codeno ='ImagetPayApply';
--更新customer_info表liveaddress
update customer_info set liveaddress = '北京市市辖区东城区' where customerid = '320000001236128';
select liveaddress from CUSTOMER_INFO where CUSTOMERID = '320000000050412' for update;
update customer_info set liveaddress = '河北省石家庄市裕华区体育南大街379号11栋3单元403号' where CUSTOMERID = '320000000050436';
--查channelcustid
select ca.CHANNELCUSTID from CHANNEL_APPLY_INFO ca join BUSINESS_APPLY ba on ca.serialno=ba.CHANNELAPPLYNO join PUTOUT_APPROVE pa on
    ba.serialno=pa.OBJECTNO where ba.SERIALNO = '20211108000004004';

select liveaddress from CUSTOMER_INFO where customerid = '320000001233778';
--调用比例
select * from THIRD_INTERFACE_PROPORTION where PRODUCTID = '7014' and INTERFACECODE in ('11001','9001') and KIND = 'SJSM';
select * from THIRD_INTERFACE_PROPORTION where PRODUCTID = '7018' and INTERFACECODE in ('9002','1001') and KIND = 'YHKJQ';
--昨日理赔数据/应发理赔短信数
select * from claim_prepare_info cpi where cpi.confirmdate = to_char(sysdate-1,'yyyy/MM/dd')
and cpi.status = '1';
select * from push_message_info where phoneno = '16610282450';
--已发短信数
select cpi.confirmdate,pmi.*  from claim_prepare_info cpi
inner join push_message_info pmi
on cpi.billno = pmi.billno and cpi.confirmdate = to_char(sysdate-1,'yyyy/MM/dd')
and pmi.messagetype in ('gd604','gd607') and to_char(to_date(pmi.sendtime,
'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd')=to_char(sysdate,'yyyy-mm-dd');
select confirmdate from claim_prepare_info where confirmdate like '2021/11/1%';
select * from TASK_EXECUTION_STATISTICS;
--理赔后知会统计发邮件
select
   al.policyno,
   '线上' productType,
   confirmdate,
   case when pmi.billno is not null then '是' else '否' end isSend,
   pmi.sendtime,
   pmi.messagetype,
   pmi.billno
from
   claim_prepare_info cpi inner join acct_loan al
   on cpi.billNO = al.serialno and cpi.status = '1' and cpi.confirmdate = to_char(sysdate-1,'yyyy/MM/dd')
   inner join CLAIM_PAYMENT_SCHEDULE cps
   on al.serialno = cps.Objectno
   left join push_message_info pmi
   on cpi.billNO = pmi.billno and pmi.messagetype in ('gd604','gd607')
   and substr(pmi.sendtime,1,10) = to_char(sysdate,'yyyy/MM/dd');

select LIVEADDRESS from CUSTOMER_INFO where CUSTOMERID = '320000000036319';
select * from CODE_AREA where AREACODE = '110000';



--对公还款中间表
select * from CORP_ACCOUNT_INFO where billno = '20062-W210706000021148';
--对公还款记录表
select * from CORP_ACCOUNT_RECORD where billno = '787-503208153301694830';
select * from CORP_ACCOUNT_RECORD where repaydate = '2032/12/15';

-- delete from CORP_ACCOUNT_RECORD where billno = '787-502601153300599526';



select ROWNUM, PA.CHANNELPUTOUTSNO,                          --{#翼支付订单号}
											CPS.PERIODNO,				                              --{#还款期数}
											CASE WHEN CAR.REPAYTYPE = '100' THEN 'TY'				  --{#催收减免：对应提前清贷}
	 										WHEN CAR.REPAYTYPE =  '7' AND CPS.FINISHDATE IS NOT NULl
	 										THEN 'Y'					 							  --{#该期结清}
	 										WHEN CAR.REPAYTYPE =  '7' AND CPS.FINISHDATE IS  NULl
	 									    THEN 'N'												  --{#该期未结清}
											END  settled ,											  --{#该期是否还清}
											(CAR.BALANCE +CAR.INTEREST +CAR.PENALTY
											+CAR.COMP + CAR.FEEAMT)*100  sumpay,			          --{#当期还款总金额（分）}
											CAR.BALANCE *100,							     	      --{#当期本金（分）}
											(CAR.INTEREST+CAR.COMP)*100,							  --{#当期利息（分））含复利}
											CAR.PENALTY*100,									      --{#当期罚息（分）}
											CAR.FEEAMT*100,									          --{#当期保费（分）}
											0，0，     											 	  --{#当期应还提前结清违约金、担保费：固定为0}
											NVL(CPS.ACTUALOVERDUEFINE,0)							  --{#当期实际还款滞纳金：总欠表}
									  from CORP_ACCOUNT_RECORD CAR LEFT JOIN                          --{#table：理赔后对公还款记录表 为主表}
									  CLAIM_PAYMENT_SCHEDULE  CPS									  --{#table：总欠表}
									  ON CAR.BILLNO = CPS.OBJECTNO
									  LEFT JOIN ACCT_LOAN AL										  --{#table：借据表：关联取到保单号}
			 						  ON CAR.BILLNO = AL.SERIALNO
									  LEFT JOIN PUTOUT_APPROVE PA									  --{#table：提现记录表：通过保单号与借据表关联，取到最终翼支付订单号}
			  						  ON  AL.POLICYNO =PA.POLICYNO
									  WHERE  CAR.batch_date='2035/01/02'							  --{#where：D-1日账务传输的记录}
									  AND EXISTS
											(SELECT 1 FROM ACCT_LOAN al where						  --{#where：区分甜橙产品编号：7014}
 											al.SERIALNO = CAR.BILLNO AND al.PRODUCTID ='7014')


select * from queue_model where modelno in ('BizApplyORANGE');
select * from queue_model where modelno in ('BizApplyBCM');

select ci.WORKUNIT,ci.* from customer_info ci where ci.customerid = '320000001237433';
select ci.WORKUNIT,ci.CREATE_DATE from customer_info ci order by CREATE_DATE desc;

select * from queue_task where MODELNO = 'ReconciliationCheck';

--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202204260000002001'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20220523000000004'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc --for update;

--同盾
select * from TD_RESULT_MSG where customerid = '320000000040618';
select * from IP_INFO order by create_time desc;
select * from IP_INFO where applyno = '202112200000002004';
select * from IP_INFO where ip = '192.168.1.2' and applyno = '20210108000002003';
--百融自然人
select * from BRAIN_PERSONSPECIAL where applyno = '20211216000004002';
--百融规则
select * from BRAIN_RULESPECIALLIST where customerid='320000000040618';
--百融特殊名单
select * from BRAIN_SPECIALLIST where customerid='320000000040618';
--冰鉴
select * from ICE_WARNING_FIREEYES where customerid = '320000000040618';

select * from acct_loan where serialno = '787-503701143301829446';

select * from CODE_TEMP where ITEMDESCRIBE = '7014';
select * from FLOW_OBJECT FO where FO.ObjectType='jbo.sys.CODE_TEMP';
select * from FLOW_OBJECT FO where FO.ObjectType='jbo.sys.CODE_TEMP' and FO.ObjectNo=O.SERIALNO and FO.ApplyType=:ApplyType and FO.PhaseType=:PhaseType  and FO.UserID=:UserID and ITEMDESCRIBE = :productId

select * from customer_info where customerid is not null;

select * from BUSINESS_APPLY where serialno = '20211224000000006';




select * from acct_loan where serialno = '787-503701143301829446';
select * from ALL_REPAY_SERIAL where serialno = '20211208000000008';

select * from BANK_BALANCE_INFO ;



update acct_loan a set a.loanstatus='1',a.finishdate ='2037/08/02' where a.serialno = '787-503701143301829446';

insert into CLAIM_PREPARE_INFO (SERIALNO, BILLNO, OVERDUEDAYS, OVERDUEBALANCE, OVERDUEINTEREST, OVERDUEFINE, OVERDUECOMPOUND, INTEREST, NORMALBALANCE, CLAIMAMT, ACTUALCLAIMAMT, STATUS, REMARK, CLAIMPLANDATE, CREATE_DATE, UPDATE_DATE, CONFIRMDATE, PAYTYPE, INPUTDATE, PAYASSUREFEEAMT, PAYREBACKASSUREFEEAMT, PAYPREASSUREFEEAMT)
values ('20220110001000001', '787-503701143301829446', 80, 1984.31, 1.50, 0.00, 0.00, 96.79, 0.00, 4061.82, null, '0', '', '', to_date('10-10-2021 17:03:19', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-10-2021 11:06:37', 'dd-mm-yyyy hh24:mi:ss'), '2037/08/02', '理赔', '2037/08/02', null, null, null);

{"fundCode":"787","bizNo":"PBLG202131171845015146","claimDate":"2037/08/02 14:47:46","paytype":"6","paycredere":6107.39,"loanStatus":"91","seqId":12,
"createTime":"2037/08/02 18:13:06","updateTime":"2037/08/02 15:00:51","bizSeqNo":"31040619506765008800000007241800","claimLock":1,"isCanClaim":true,
"claimStatus":"91","claimDesc":"理赔成功"}


select * from CHANNEL_APPLY_INFO where IDNO  ='542426199107058290';


SELECT * FROM CUSTOMER_BLACKLIST CB where CB.STATUS='1' and serialno = '909361A6097F48BB83BBCEBA3F864881' for update;
	

SELECT * FROM CUSTOMER_BLACKLIST CB where CB.STATUS='0' and CB.Customername in ( '曹贝辰','陈顺','燕好飞') for update;
SELECT * FROM CODE_LIBRARY where codeNo='BlackListStatus';

SELECT * FROM CUSTOMER_BLACKLIST CB where CB.STATUS='0' and customername = '巴萍' for update;
select * from customer_blacklist where serialno = '2d01a4e165174b048dbe91213e859258';
select * from customer_blacklist where serialno = 'f586e463cfdd4abab4957af3fb7d5b55';
SELECT CB.SERIALNO FROM CUSTOMER_BLACKLIST CB where CB.STATUS='1' AND CB.INVALDATE = to_char(sysdate,'yyyy/MM/dd')
select * from UPLOAD_TASK;

select * from CUSTOMER_WHITELIST where customername = '测试';

--在image_list里找这两种类型的文件，把businessno改成现跑的渠道流水号，把SIGNLOANNO改成你们现跑的体现流水号
SELECT * FROM IMAGE_LIST O ,BUSINESS_INSURANCEPOLICYINFO BI WHERE O.SIGNLOANNO = BI.PUTOUTAPPROVENO  and IMGTYPE in 
( '|UWB438|','|UWB401|','|UWB401|') and O.businessno = '322000000001568';

select * from IMAGE_LIST il where il.businessno = '322000000001568' and IMGTYPE in 
( '|UWB438|','|UWB401|','|UWB401|') for update;

select * from IMAGE_LIST il where il.serialno in ('d3ef10a0d2de4f7782fc89f98d81f7fb','0d3bcef83a714d0ba78ec41eb60eaa95','80f6bfbd50a94e4782603c9e61e198be') for update;

update IMAGE_LIST O set businessno = '202203290000002006', SIGNLOANNO = '20220329000000002' where IMGTYPE in 
( '|UWB438|','|UWB401|','|UWB401|') and businessno = '2021091700001';

select * from channel_apply_info where serialno = '202203290000002006';

select * from queue_model where item = 'H5ResultQuery';
select * from channel_apply_info where customerid ='320000000005694' ;
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202204270000002007'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc --for update;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20220518000000013'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc --for update;
update queue_task set runstatus = 'G' where modelno = 'PushMessage' and item = 'PushMessageInError' and runstatus = 'ST';
select * from trans_log where customerid = '320000000054722' and servicename = 'BmDataCommon';
select * from trans_log where customerid = '320000000054722' and servicename = 'BigDataIlogService';
select * from trans_log where customerid = '320000000056738' and servicename = 'CreateInsureOrange'; --查对应节点报文


SELECT * FROM IMAGE_LIST O ,BUSINESS_INSURANCEPOLICYINFO BI WHERE O.SIGNLOANNO = BI.PUTOUTAPPROVENO  and IMGTYPE in ( '|UWB438|';

SELECT * FROM IMAGE_LIST O ,BUSINESS_INSURANCEPOLICYINFO BI WHERE O.SIGNLOANNO = BI.PUTOUTAPPROVENO  and IMGTYPE in 
( '|UWB438|','|UWB401|','|UWB401|') and businesstype = '7014';



SELECT qt.rowid,qt.* FROM queue_task qt where qt.customerid = '320000000030836' and qt.modelno = 'PutoutApproveHB' for update;


select * from IMAGE_LIST il where il.customerid = '320000001253323'-- for update;
update image_list set imgtype = '|UWB401|',imgtypename = '身份证正面' where customerid = '320000001253341' and imgtype = '|UWB004|' and SIGNLOANNO is not null;
update image_list set imgtype = '|UWB401|',imgtypename = '身份证反面' where customerid = '320000001253341' and imgtype = '|UWB441|' and SIGNLOANNO is not null;
update image_list set imgtype = '|UWB438|',imgtypename = '人脸识别图片' where customerid = '320000001253341' and imgtype = '|UWB407|'and SIGNLOANNO is not null;


select liveaddress from customer_info where CERTID = '430724199511302802';

select * from INSURED_MANEGEMENT where insuredcode = 'HBBank001';
update INSURED_MANEGEMENT set insuredname = '河北银行股份有限公司' where insuredcode = 'HBBank001';


                       SELECT SERIALNO,LOANSTATUS as STATUS,POLICYNO,DDPRODUCTID,CAPITALCODE
                    	      FROM ACCT_LOAN
                    	     WHERE LOANSTATUS IN ('0','1') and serialno like '031502%' --for update
                           
                        update acct_loan set capitalcode = '031502' where LOANSTATUS IN ('0','1') and serialno like '031502%'
                        update acct_loan set capitalcode = 'HBBank' where LOANSTATUS IN ('0','1') and serialno like '031502%'
                        
                        --031502-BHB903624826610319365
                        update acct_loan set capitalcode = 'HBBank' where LOANSTATUS IN ('0','1') and serialno like '031502-BHB903624826610319365'
                        

                           
                                                  SELECT SERIALNO,LOANSTATUS as STATUS,POLICYNO,DDPRODUCTID,CAPITALCODE
                    	      FROM ACCT_LOAN
                    	     WHERE LOANSTATUS IN ('0','1') 
                           
select * from queue_task qm where qm.objectno = '20220407000002007'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc --for update;


select * from acct_loan where serialno = '031502-BHB907250663771406337';
select * from acct_payment_schedule where objectno = '031502-BHB907250663771406337';



select * from business_trans_record where customerid = '320000001248791';

select * from CAPITAL_RATE_INFO where capitalcode = 'HBBank';
update channel_apply_info set IDADDRESS = '河北省石家庄市裕华区体育南大街379号11栋3单元403号' where IDNO = '230402199209206869'



SELECT SERIALNO,LOANSTATUS as STATUS,POLICYNO,DDPRODUCTID,'031502' as CAPITALCODE FROM ACCT_LOAN WHERE 
CAPITALCODE = 'HBBank' and 
LOANSTATUS IN ('0','1') and 
SERIALNO like '031502-%'; 

select * from channel_apply_info where customerid ='320000000015285' ;
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202205070000002008'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc for update;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20220518000000003'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc --for update;


select * from CL_INFO where customerid = '320000000005694' --for update;

 select o.* FROM ACCT_PAYMENT_SCHEDULE O WHERE EXISTS(
SELECT 1 FROM ACCT_LOAN AL WHERE AL.SERIALNO = O.OBJECTNO
--AND AL.CUSTOMERID = '320000001250209'
AND AL.create_time >= to_date('2020/04/25', 'yyyy/MM/dd')
AND AL.create_time <= to_date('2022/04/25', 'yyyy/MM/dd') 
 ) AND O.ACTUALPAYDATE > O.PAYDATE;
 
select * from acct_loan where customerid = '320000000015285' for update;
update acct_loan set customerid = '320000001250357' where customerid = '320000000005501';
update acct_loan set loanstatus = '0' where customerid = '320000000015285';
SELECT * FROM CODE_LIBRARY where codeNo='LoanStatus';  --贷款状态
select intransitLoanCount from channel_apply_info where serialno = '202204270000002012';--intransitLoanCount
select intransitLoanCount from putout_approve where serialno = '20220427000000004';
SELECT * FROM ILOG_RULES_RESULT c WHERE c.applyno = '20220427000000004';--ilog规则集
SELECT * FROM ILOG_RULES_RESULT c WHERE c.signloanno = '20220427000000004';--ilog规则集

select * from ILOG_RULES_LOAN_DETAIL where objectno = '62C6B1FD7C7746C9B6AA84E18F6E06A4';

select * from acct_payment_schedule where objectno = '787-502903153301549941' for update;--787-502811012980162502、787-502811012980162504、787-502811012980162506
select * from acct_payment_schedule where objectno = '20200710145457826826' for update;--20200710144014793793、20200710144411794794、20200710145457826826

SELECT AL.Overduedays,AL.* FROM ACCT_LOAN AL WHERE
AL.CUSTOMERID = '320000001250209'
AND to_date(AL.putoutdate,'yyyy/MM/dd') >= to_date('2020/04/25', 'yyyy/MM/dd')


select al.serialno,al.loanstatus,al.overduedays,al.* from acct_loan al where al.serialno in
('787-503904153301878649','787-503904153301878650','787-503904153301878159',
'787-503904153301878642','787-503904153301878203','787-503904153301878640','787-503904153301878644') for update nowait;



SELECT * FROM   CLAIM_PREPARE_INFO CP, acct_loan al where al.serialno = cp.billno 
and cp.status = '0' and al.capitalcode = '787' order by cp.serialno desc;

select * from CLAIM_PREPARE_INFO where billno = '787-503811223301870136' for update;
select * from acct_loan where serialno  = '787-503811223301870136' for update;
update ACCT_LOAN al set al.loanstatus = '1' where al.serialno in (
'787-503811223301870136'  
);
update CLAIM_PREPARE_INFO cp set cp.status = '0' where cp.billno in (
'787-503811223301870136' 
);

update CallBack_interface_info set status = '00' where serial_no = '20220511000000001';


SELECT SERIALNO,LOANSTATUS as STATUS,POLICYNO,DDPRODUCTID,CAPITALCODE
FROM ACCT_LOAN al
WHERE CAPITALCODE = '787'
and LOANSTATUS IN ('0','1')
and al.serialno in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
);


update ACCT_LOAN al set al.loanstatus = '1' where al.serialno in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
);
select * from acct_loan where serialno in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
);
update CLAIM_PREPARE_INFO cp set cp.status = '0' where cp.billno in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
);
select * from CLAIM_PREPARE_INFO where billno in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
);

select * from CLAIM_PAYMENT_SCHEDULE where OBJECTNO in (
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
) for update;
--甜橙理赔回调记录
select * from CallBack_interface_info;
update CallBack_interface_info set status = '00';

SELECT * FROM queue_model qm where qm.modelno = 'OrangeCallbackList' ;

select * from  queue_task  qt where qt.modelno = 'OrangeCallbackList' for update;


select * from channel_apply_info where intransitloancount is not null;
select * from putout_approve where intransitloancount is not null;

);

select * from SECONDCREDIT_THIRD_RECORD



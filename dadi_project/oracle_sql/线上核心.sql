--改系统时间
select * from system_setup;
update system_setup set businessdate = '2021/01/19',batchdate = '2021/01/19' where systemid = '1';
--标准查码值
SELECT * FROM CODE_LIBRARY where codeNo='EducateLevelCode';  --学历
SELECT * FROM CODE_LIBRARY where codeNo='MarryStatus';  --婚姻状况
SELECT * FROM CODE_LIBRARY where codeNo='RealNameStatus';  --获客渠道
select * from code_library c where c.codeno in('ShowState');
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
select * from channel_apply_info where customerid ='320000001234265' ;
--授信信息
select * from business_apply where customerid ='320000001228058';
--支用信息
select * from putout_approve where serialno = '20211027000004001';
select * from putout_approve where CUSTOMERID = '320000001232785';
--设备信息
select * from CHANNEL_DEVICE_INFO where creditreqno = '2021091511112690919';--320000000033936
--联系人信息
select * from CUSTOMER_TEL where customerid = '320000000666413' and serialno like '20210917%';
select * from customer_tel where applyno='20210917000000002';
--实名流水
select *from customer_realname where regid ='320000000662825';
select *from customer_realname_log where regid ='20201202000002005';
--核心流程节点配置
select * from  queue_model where modelno ='BizApplyPay';
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202111170000000001'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20211116000002001'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc;
select * from queue_task where ITEM = 'CapitalPutoutQuery';
--批单表
select * from INSURANCEPOLICY_CHANGE_RECODE where policyno = 'PBLG202031170359000178';
--缩期还款计划
select * from acct_payment_schedule where objectno = '787-503302173301732221';
--不缩期还款计划
select * from acct_payment_schedule_not where objectno = '787-503302173301732221';
--还款通知
select * from loan_batch_notice where billno='787-503502243301802038';
--还款记录
select * from loan_batch_info where objectno='20062-W210923004201302';
select * from loan_batch_info where objectno='20062-W210923004201302';
--扣款记录
select * from loan_batch_cutpayment where billno='787-502805153301143206';
--查还款交易类型
SELECT operatetype FROM loan_batch_notice where billno in ('787-503403193301772087','');
--总欠记录
select * from CLAIM_PAYMENT_SCHEDULE;
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
select * from CUSTOMER_BANK_CARD where CUSTOMERID = '320000000675368';
delete CUSTOMER_BANK_CARD where CUSTOMERID = '320000001234146';

--四要素是否调用
select * from customer_auth where certid='65322420090421440X';
select * from CUSTOMER_AUTH where customerid = '320000000036838';
select * from CUSTOMER_AUTH where APPLYSERIALNO = '20211112000000001';
select * from CUSTOMER_AUTH where RESULT = '2';

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
SELECT * FROM ILOG_RULES_RESULT c WHERE c.applyno = '20200722000000006';
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
update customer_info set liveaddress = '北京市市辖区东城区' where customerid = '320000001234265';
update customer_info set liveaddress = '河北省石家庄市裕华区体育南大街379号11栋3单元403号' where CERTID = '320000001231136';
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
select * from CORP_ACCOUNT_INFO where billno = '787-503005073301597532';
--对公还款记录表
select * from CORP_ACCOUNT_RECORD where billno = '787-503005073301597532';


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
									  WHERE  CAR.batch_date='2030/08/28'							  --{#where：D-1日账务传输的记录}
									  AND EXISTS
											(SELECT 1 FROM ACCT_LOAN al where						  --{#where：区分甜橙产品编号：7014}
 											al.SERIALNO = CAR.BILLNO AND al.PRODUCTID ='7014')
--改系统时间
select * from system_setup;
update system_setup set businessdate = '2021/01/19',batchdate = '2021/01/19' where systemid = '1';
--标准查码值
SELECT * FROM CODE_LIBRARY where codeNo='EducateLevelCode';  --学历
SELECT * FROM CODE_LIBRARY where codeNo='MarryStatus';  --婚姻状况
SELECT * FROM CODE_LIBRARY where codeNo='RealNameStatus';  --获客渠道
select * from code_library c where c.codeno in('ShowState');
--基础产品管理
select * from PRODUCT_TERM_INFO pt where pt.productid = '7018' and term = '6';
--改当日送线下报收付费
select * from offlinerecord where bacthno = '20210926000001_03';
select * from offlinerecord where bacthno like '202201%';
SELECT
	*
FROM
	OFFLINERECORD
WHERE
	SERIALNO LIKE '20210926%';--额度平台在途件（在途后再次申请，报错时查）
select * from loan_credit_records where id_card='320681198909240017' and status='0';
--额度状态表
select * from loan_limit where id_card='410102199007183213';
--渠道信息
select * from channel_apply_info where creditreqno ='2020120410404386556';
select * from channel_apply_info where customerid ='320000001232477' ;
select * from BAODAI_INSURANCEPOLICYINFO WHERE INSURANCENO= '2020120213533888889';
--授信信息
select * from business_apply where customerid ='320000001228058';
--支用信息
select * from putout_approve where serialno = '20211027000004001';
select * from putout_approve where CUSTOMERID = '320000001232785';
--设备信息
select * from CHANNEL_DEVICE_INFO where creditreqno = '2021091511112690919';--320000000033936
--
select * from CHANNEL_APPLY_INFO where customerid = '320000000033936';

--联系人信息
select * from CUSTOMER_TEL where customerid = '320000000666413' and serialno like '20210917%';
select * from customer_tel where applyno='20210917000000002';
--实名流水
select *from customer_realname where regid ='320000000662825';
select *from customer_realname_log where regid ='20201202000002005';
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202110270000006006'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc;

select * from queue_model where modelno = 'PutoutApproveOrange';
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20211028000014005'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc;
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
--拍拍贷客户等级上下限
select t.itemno , t.attribute1 , t.attribute2 from code_library t  where codeno ='PaiPaiDai';
--还呗折后利率
select t.itemno , t.attribute1 , t.attribute2  from code_library t  where codeno ='HuanbeiArte';
--批单表
select * from INSURANCEPOLICY_CHANGE_RECODE where policyno = 'PBLG202031170359000178';
--缩期还款计划
select * from acct_payment_schedule where objectno = '787-503302173301732221';
--不缩期还款计划
select * from acct_payment_schedule_not where objectno = '787-503302173301732221';
--还款通知
select * from loan_batch_notice where billno='20062-W210923004201302';
--还款记录
select * from loan_batch_info where objectno='20062-W210923004201302';
select * from loan_batch_info where objectno='20062-W210923004201302';
--扣款记录
select * from loan_batch_cutpayment where billno='787-502805153301143206';
--四要素成功落库
select * from CUSTOMER_BANK_CARD where customerid = '320000001232085';
--四要素是否调用
select * from customer_auth  where certid='620122199410061093';
select * from customer_auth  where certid in (select idno from CHANNEL_APPLY_INFO where customerid = '320000001220588');

;

--四要素是否复用
select * from third_relative where customerid = '320000001232002';
--调三要素
select * from PHONETHREE_VERITY_RESULT  where servicecode='12001' and responsecode = '0';
--OCR识别
select * from ocr_operate_record where customerid = '320000000034108';
--人脸照片
select * from IMAGE_LIST where CUSTOMERID = '20200826000002008';
--黑瞳复用
select * from third_relative where customerid = '320000000670153';
--黑瞳调用
select * from HEITONG_RESULT WHERE customerid = '320000001232004';
select * from heitong_high_risk where OBJECT_NO = '20211028000002007';
select * from heitong_high_risk where CUSTOMERID = '320000000034080';
select * from trans_log where applyno = '20211022000002004' and Servicename = 'HeiTongAntiFraudService';
--ilog5,ilog9人行数据落库
select baoXianQueryNumLast6 from ED_ILOG_PBOC_DATA where REPORTNO = '2021102610021207445' and serialno = '20211026000004011';
--ilog规则集结果
SELECT * FROM ILOG_RULES_RESULT c WHERE c.applyno = '20200722000000006';
SELECT * FROM ILOG_RULES_RESULT c WHERE c.customerid = '320000001219556';
--法院限高调用记录
select * from COURT_HEIGHT_LIMIT where object_no = '202108040000006005';
select * from business_apply where customerid = '320000001222407';
--北冥接口
select * from brain_personspecial where customerid = '320000000662522';
--拍拍特有信息
select * from PPDAI_CHANNEL_DETAIL;
--认证项结果落表
--公安网 公安简项
select * from NCIICLIST where idcard ='340506199207219515'  order by update_time desc;
select * from NCIICLIST where SERIALNO IN ('A03842BF82B4478E864D4C00F39CF080','C32A1A581A194B0183BB9D67D11CDCC2');
--四要素
select * from CUSTOMER_AUTH where customerid ='320000001227397'order by update_time desc;
--三要素
select * from PHONETHREE_VERITY_RESULT where customerid ='320000000659068' order by update_time desc;
--核身结果落表
select *from FACEID_LIVENESS where customerid ='20201202000002005';
--影像
select *from image_list  where customerid ='20201202000002004';
--核心流程节点配置
select * from  queue_model where modelno ='BizApplyPay';
--互金信息
select * from ILOG_HJ_INFO WHERE APPLY_NO ='202103190000000004';
--对应的ILOG_HJ_INFO的主键
select * from ILOG_HJ_INFO_query WHERE HJ_SERIALNO ='20210319000000009';
--百融
select * from BRAIN_RULESPECIALLIST  where customerid= '320000000670361' or applyno = '20210318000002011'  order by create_time desc;
select * from BRAIN_SPECIALLIST where customerid= '320000000670361' or applyno = '20210318000002011'  order by create_time desc;
--北溟
select * from BRAIN_PERSONSPECIAL where applyno = '202104160000000002'  order by querytime desc;
select * from HEITONG_RESULT WHERE objectno = '20210318000002009';   --黑瞳调用
--黑瞳高危
select * from heitong_high_risk where object_no = '20211026000000001';
select * from trans_log where applyno = '202107130000000001' and servicename = 'SfptHighRiskService';
--关联影像
insert into image_list (SERIALNO, IMGID, BUSINESSNO, IMGTYPE, IMGTYPENAME, VALIDFLAG, PICNAME, PICCLASS, PICDETAILS, PICPATH, THUMBNAILPATH, CREATE_DATE, UPDATE_DATE, BUSINESSDATE, APPLYNO, REALNAMEKEYNO, PICORDER, SIGNLOANNO, IMAGESTAGE, CHANNELAPPLYNO, CUSTOMERID, BILLNO)
values ('DF3B02E6AD474039B54A61114D824465', '3256765', '322000000001435', '|UWB438|', '|人脸识别图片|', '1', null, null, null, null, null, to_date('22-03-2021 00:00:00', 'dd-mm-yyyy hh24:mi:ss'), to_date('22-03-2021 00:00:00', 'dd-mm-yyyy hh24:mi:ss'), '20210322', '', null, null, null, null, '202106100000000009', null, null);
--甜橙定制信息
select * from ORANGE_PARTNER_INFO where creditreqno = '20210929886881001';
select * from ORANGE_PARTNER_INFO where objectno = '20210902000000002';
--360定制信息
select CUSTGRADE from FINANCE360_CHANNEL_DETAIL where creditreqno = '2021102319050979012';

select * from acct_payment_schedule aps where
      aps.objectno = '301-204601310350999048200000406001' for update nowait ;--paipai 还款计划表修改还款时间
select * from claim_prepare_info where  billno = '20062-W210702000021114' order by create_date desc; --预理赔表修改理赔时间

select * from customer_info where customerid = '320000001217594' ;
select overduedays from Acct_Loan where customerid = '320000001217594'; --借据表改逾期时间

--查还款交易类型
SELECT operatetype FROM loan_batch_notice where billno in ('787-503403193301772087','');

select * from queue_task qm where qm.objectno = '20210927000002003'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc;
--理赔客户数
select * from claim_payment_schedule where OBJECTNO in ('20062-W210923004201302','787-503101172980222334');

--征信上报数
select * from push_message_info where messagetype in ('gd604','gd607') and sendtime like '2021/10/12%';

--预理赔
select cpi.confirmdate,cpi.* from claim_prepare_info cpi where cpi.billno = '20062-W210923004201302';
select cpi.confirmdate,cpi.* from claim_prepare_info cpi where cpi.billno = '787-503101172980222334';


select count(1) as claimNums from claim_payment_schedule cps where  cps.PAYDATE=to_char(sysdate-1,'yyyy/MM/dd');
select * from push_message_info where to_char(to_date(sendtime,'yyyy-mm-dd hh24:mi:ss'),'yyyy-mm-dd')=to_char(sysdate,'yyyy-mm-dd')and MESSAGETYPE in ('gd604','gd607');

select * from push_message_info pm where  pm.sendtime=to_char(sysdate,'yyyy/MM/dd') and (pm.messagetype='gd604'or pm.messagetype='gd607');

select * from SECONDCREDIT_THIRD_RECORD where reportno is not null order by create_date desc;

--理赔客户数
select * from claim_payment_schedule where OBJECTNO in ('20062-W210712000021245','787-503008283301607572');
--征信上报数
select * from push_message_info where messagetype in ('gd604','gd607') and sendtime like '2021/10/12%';
--预理赔
select cpi.confirmdate,cpi.* from claim_prepare_info cpi where cpi.billno = '20062-W210712000021245';
select cpi.confirmdate,cpi.* from claim_prepare_info cpi where cpi.billno = '787-503008283301607572';


select NORMALBALANCE as 正常本金,OVERDUEBALANCE as 逾期本金 from acct_loan where serialno = '20062-W210923004201302';

select * from CHANNEL_APPLY_INFO where CUSTOMERID = '320000000034073';

SELECT * FROM queue_task where objectno ='20211026000000001' and  objecttype ='jbo.app.PUTOUT_APPROVE' order by runtime;

select CUSTGRDE from PPDAI_CHANNEL_DETAIL where creditreqno = '2021102617252950601';
select custgrade from CHANNEL_APPLY_INFO where CUSTOMERID = '320000000034076';
select * from CHANNEL_APPLY_INFO where CUSTOMERID = '320000000006586';

--测还呗产品影像时改拉取远程路径
select * from code_library cl where cl.codeno ='ImagetPayApply';
update code_library set attribute2 = '/sftp/ccic/income/upload/image' where codeno ='ImagetPayApply';
update code_library set attribute2 = '/ccicall/cfs/test/file' where codeno ='ImagetPayApply';



select * from PUTOUT_APPROVE where CUSTOMERID = '320000000033928';

select * from CHANNEL_APPLY_INFO where CUSTOMERID = '320000000034080';
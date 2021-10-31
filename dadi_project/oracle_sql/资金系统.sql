--标准查码值
SELECT * FROM CODE_LIBRARY where codeNo='repay_way';
--线上核心资金路由配置比例
select * from business_config aa where aa.catalog_code='WEIGHT_RANDOM' and aa.product_code ='7014';
select * from business_config aa where aa.product_code ='7014';
--资方放款状态
select * from ACCT_FUND_APPLY where apply_no = '20211013000000001';
select * from ACCT_FUND_APPLY where apply_no = '20210928000000004';
--借据
select * from acct_loan where serialno = '20062-W2021092915414699797';
update ACCT_PAYMENT_SCHEDULE a set a.fineintedate = '',a.FINEINTEBASE = '',a.PAYFINEAMT = '' where objectno = '20062-W2021092915414699797';

--还款流水
select t.result_code,t.*,t.rowid from acct_transaction t where t.relativeserialno like '787-502404203300211517' order by created_date desc;
select a.result_code,a.* from acct_transaction a where a.relativeserialno='20062-W210923004201302';
-- 还款明细表
select * from ACCT_BACK_DETAIL where loanserialno = '787-503208153301694830';
-- 还款单据表
select * from ACCT_BACK_BILL;
--还款借据表
select * from acct_loan where serialno = '787-503208293301702761';
--还款计划表
select * from ACCT_PAYMENT_SCHEDULE where objectno = '20062-W2021092915414699797';
select * from ACCT_PAYMENT_SCHEDULE where objectno = '787-503407243301792589';
--账务还款记录表
select * from acct_back_detail t where t.LOANSERIALNO='787-502805153301143206';
select * from acct_back_detail t where t.LOANSERIALNO='787-502711152980095447';
--还款记录表
select * from acct_back_bill abb where abb.OBJECTNO='787-502805153301143206' ;
select * from acct_back_bill abb where abb.OBJECTNO='787-502711152980095447';
--总欠记录
select * from acct_recovery_loss a  where a.serialno = '20062-W210923004201302';
--文件
--LoanDetail    借据信息
--RepayPlan     还款计划
--PremiumDetail 保费明细
--RepayDetail   还款记录
--CollectRecords催收记录
select * from acct_file_task where fund_code = '301' and file_code in ('PremiumDetail','RepayDetail');
select * from acct_file_task where id = '460100002819875';
select * from acct_file_task_detail where task_id in ('460100002819875') ;
select * from acct_file_task_detail where task_id in ('460100000211065','460100000211067') ;
-- 查微众订单号
select afa.result_seq_no from acct_fund_apply afa where afa.apply_no in(
select al.apply_no from acct_loan al where al.serialno in (
'787-502903203301551902'));
--同步微众还款计划不成功时执行
update acct_loan al set al.ifstopfineinte = '1' where serialno = '20062-W2021092915414699797';
update ACCT_PAYMENT_SCHEDULE a set a.fineintedate = '' where objectno = '787-503006283301603072';
update acct_loan a set a.ifstopfineinte = '1' where a.ifstopfineinte = '3' and a.businesstype = '7018';
select * from acct_loan where ifstopfineinte = '1' and businesstype = '7018';
--不缩期的还款计划表
select * from acct_payment_schedule where objectno = '787-503003053301592115' ;


update ACCT_PAYMENT_SCHEDULE set status = '12' where seqid = '1' and objectno in
('787-503207243301693188');
--文件解析任务
select * from acct_file_task where fund_code = '787' and file_code = 'ClaimApply' and business_date = '2032/11/09' order by business_date desc;

--龙江计息


select * from acct_loan where serialno in (
'787-503208153301694830',
'787-503208153301694547',
'787-503208153301694826',
'787-503208153301694545',
'787-503208153301694551',
'787-503208153301694557',
'787-503208153301694553',
'787-503208153301694554',
'787-503208153301694820',
'787-503208153301694822',
'787-503208153301694549',
'787-503208153301694544',
'787-503208153301694556'
);

select * from prpjp pr where pr.policyno = 'PBLG202131170359022516';
select * from prpjp pr where pr.batno = '20210720000001_7015_LJ';



--标准查码值
SELECT * FROM CODE_LIBRARY where codeNo='repay_way';
--线上核心资金路由配置比例
select * from business_config aa where aa.catalog_code='WEIGHT_RANDOM' and aa.product_code ='7014';
select * from business_config aa where aa.product_code ='7014';
--资方放款状态
select * from ACCT_FUND_APPLY where apply_no = '20220208000002003';
select * from ACCT_FUND_APPLY where RESULT_CODE = '22';
--借据
select LOANSTATUS from acct_loan where serialno = '787-503701143301829446';
update ACCT_PAYMENT_SCHEDULE a set a.fineintedate = '',a.FINEINTEBASE = '',a.PAYFINEAMT = '' where objectno = '20062-W2021092915414699797';

--还款流水
select t.result_code,t.*,t.rowid from acct_transaction t where t.relativeserialno like '787-502404203300211517' order by created_date desc;
select a.result_code,a.* from acct_transaction a where a.relativeserialno='787-503208153301694820';
select * from acct_transaction where SEQ_IDS = '99';
-- 还款明细表
select * from ACCT_BACK_DETAIL where loanserialno = '787-503708063301837525';

select * from prpjp where policyno = 'PBLG202131171845014785' order by updatetime desc; --实收
select *from kafka_payment_notify where bill_serialno = '460100024479785' order by create_time desc;--查看kfk推送结果
-- 还款单据表
select * from ACCT_BACK_BILL;
--还款借据表
select * from acct_loan where serialno = '787-503410233301796085';
select a.LOANSTATUS,a.* from acct_loan a where a.serialno in ('787-503410243301796403','787-503410233301796085');
select sysdate,add_months(sysdate,+1)+80 from dual;
update acct_loan a set a.loanstatus='91',a.finishdate ='2035/02/12' where a.serialno = '787-503410233301796085';
--还款计划表
select * from ACCT_PAYMENT_SCHEDULE where objectno = '787-503701143301829446';
select * from ACCT_PAYMENT_SCHEDULE_CLAIM where objectno = '787-503208153301694545';
select * from ACCT_PAYMENT_SCHEDULE_CLAIM where BUSINESSTYPE = '7018';
--账务还款记录表
select * from acct_back_detail t where t.LOANSERIALNO='787-503701143301829446';
select * from acct_back_detail t where t.LOANSERIALNO='787-502711152980095447';
--还款记录表
select * from acct_back_bill abb where abb.OBJECTNO='787-503701143301829446' ;
select * from acct_back_bill abb where abb.OBJECTNO='787-502711152980095447';
--总欠记录
select * from acct_recovery_loss a  where a.serialno = '787-502601153300599524';
--文件
--LoanDetail    借据信息
--RepayPlan     还款计划
--PremiumDetail 保费明细
--RepayDetail   还款记录
--CollectRecords催收记录
select * from acct_file_task where fund_code = '301' and file_code in ('PremiumDetail','RepayDetail');
select * from acct_file_task where id = '460100024482385';
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



select LOANRATE from acct_loan where serialno = '20062-W210525000020784';
select al.finishdate,al.startdate,al.finaldate,al.* from acct_loan al where al.putoutno = 'PBLG202131171845014406'for update nowait;--借据表
select bi.businesstype,bi.* from acct_back_bill bi where bi.objectno = '787-503208153301694826'  order by CREATED_DATE desc for update nowait;--还款单据表
select * from acct_back_detail where loanserialno = '20062-W210923004201302'; --还款明细表
select * from acct_payment_schedule where objectno = '787-503005073301597532';--还款计划
select tr.pay_status,tr.result_code,tr.* from acct_transaction tr
where tr.relativeserialno='20062-W210923004201302' order by updated_date desc;    --还款流水表

--收付费
select * from business_intfgl where attribute13 = 'PBLG202131170429001804';  --应收
select * from prpjp where policyno = 'PBLG202131171845014406' order by updatetime desc; --实收
select * from prpjp where policyno = 'PBLG202131170429001804' order by updatetime desc; --实收
select * from payment_notify where certino like 'R%';

select *from kafka_payment_notify order by create_time desc;--查看kfk推送结果
select * from kafka_payment_notify where bill_serialno = '460100024479785' order by create_time desc;--查看kfk推送结果
select * from kafka_payment_notify where ACCTLOAN_NO = '787-503208153301694826' order by create_time desc;--查看kfk推送结果
select al.startdate,al.finaldate,al.* from acct_loan al where al.serialno = '20062-W210923004201302'for update nowait;--借据表
--
select * from kafka_payment_notify where SERVICE_NAME = 'SendPrpjpDataService' and CERTI_NO like 'R%';

select s.updated_date,s.serialno,'','100',s.MITCORPUSAMT,s.MITINTEAMT,s. MITFINEAMT,s.MITCOMPDINTEAMT,s.REDPREMIUMAMOUNT, s.REDLATEFEEAMOUNT,'0.00',
to_char(to_date(s.updated_date,'yyyy/MM/dd HH24:mi:ss'),'yyyy/mm/dd') ,to_char(to_date(s.updated_date,'yyyy/MM/dd HH24:mi:ss'),'hh24:mi:ss')
 from ACCT_RECOVERY_LOSS s where s.REDATOTAL >0;
select * from acct_recovery_loss where redatotal > 0
                                   and serialno = '787-502601153300599526';

select * from ACCT_RECOVERY_LOSS where serialno = '787-503701143301829446';

 --查询是否 有生成过
delete  from ACCT_FILE_TASK t where t.file_code in ('PublicAndReductionFileUploadToAcct','xx','xx','xx');

select * from ACCT_FILE_TASK t where t.file_code in ('PublicAndReductionFileUploadToAcct','xx','xx','xx') /*and t.status = '1'*/
/*and t.business_date in ('2032/11/09'  ,'xxx')
order by t.file_code,t.business_date desc*/
;
select * from ACCT_FILE_TASK where id = '460100024498421';
insert into acct_recovery_loss (SERIALNO, OVERDUEFINEBEGINDATE, PAYCREDERE, ACTUALCREDERE, PAYOVERDUEFINE, ACTUALOVERDUEFINE, PAYFEEAMT1, ACTUALPAYFEEAMT1, OVERDUEFINECALCDATE, PAYOVERDUEFINEBASE, FINISHDATE, CREDEREFINISHDATE, BATCHSTATUS, RECOVERYLOSSDAYS, INPUTDATE, STATE, ANSHUOBATCHID, LUFAXBATCHID, CONFIRMDATE, CONFIRMFLAG, CONFIRMUSER, BUSINESSTYPE, OVERDUEDAYS, CONFIRMDATE1, CONFIRMUSER1, CREATED_DATE, UPDATED_DATE, PAYCORPUSAMT, ACTUALPAYCORPUSAMT, PAYINTEAMT, ACTUALPAYINTEAMT, PAYFINEAMT, ACTUALFINEAMT, PAYCOMPDINTEAMT, ACTUALCOMPDINTEAMT, PAYFEEAMT2, ACTUALPAYFEEAMT2, REMARK, ORGACCOUNTSERIALNO, CONTRACTSERIALNO, BASERIALNO, PREINTEAMT, BALANCETAILAMT, STOPPAYOVERDUEFINE, TRANSRISKIDF, TRANSRESON, REDPREMIUMAMOUNT, REDAFTERPREMIUMAMOUNT, REDCOMPENSATIONAMOUNT, REDAFTERCOMPENSATIONAMOUNT, REDLATEFEEAMOUNT, REDAFTERLATEFEEAMOUNT, TOTALRECOVERYPREMIUM, COMPENSATIONAMOUNT, LATEFEEAMOUNT, REDATOTAL, REDAFTERRECOVERYTOTAL, REDUCTIONDATE, MITCORPUSAMT, MITINTEAMT, MITFINEAMT, MITCOMPDINTEAMT)
values ('787-503410233301796085', '2034/11/11', 1000, null, 0.00, null, 118.8, null, '2034/11/11', 0.00000000, null, '2034/11/11', '0', 0, '2034/11/11', null, null, null, null, '1', null, '7015', 81, null, null, '2034/11/11 06:41:34', '2034/11/11 14:28:33', 6000.00, null, 102.39, null, 5.00, null, 0.000000, null, 0.000000, null, null, null, '37881516000192', '2015121700000369', 0.000000, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);


select LOANSTATUS from acct_loan where serialno = '787-503701143301829446';




select a.loanstatus from acct_loan a where a.serialno = '20062-W202201071114385568247';
select sysdate,add_months(sysdate,+1)+80 from dual;
update acct_loan a set a.loanstatus='91',a.finishdate ='2022/04/28' where a.serialno = '20062-W202201071114385568247';



insert into acct_recovery_loss (SERIALNO, OVERDUEFINEBEGINDATE, PAYCREDERE, ACTUALCREDERE, PAYOVERDUEFINE, ACTUALOVERDUEFINE, PAYFEEAMT1, ACTUALPAYFEEAMT1, OVERDUEFINECALCDATE, PAYOVERDUEFINEBASE, FINISHDATE, CREDEREFINISHDATE, BATCHSTATUS, RECOVERYLOSSDAYS, INPUTDATE, STATE, ANSHUOBATCHID, LUFAXBATCHID, CONFIRMDATE, CONFIRMFLAG, CONFIRMUSER, BUSINESSTYPE, OVERDUEDAYS, CONFIRMDATE1, CONFIRMUSER1, CREATED_DATE, UPDATED_DATE, PAYCORPUSAMT, ACTUALPAYCORPUSAMT, PAYINTEAMT, ACTUALPAYINTEAMT, PAYFINEAMT, ACTUALFINEAMT, PAYCOMPDINTEAMT, ACTUALCOMPDINTEAMT, PAYFEEAMT2, ACTUALPAYFEEAMT2, REMARK, ORGACCOUNTSERIALNO, CONTRACTSERIALNO, BASERIALNO, PREINTEAMT, BALANCETAILAMT, STOPPAYOVERDUEFINE, TRANSRISKIDF, TRANSRESON, REDPREMIUMAMOUNT, REDAFTERPREMIUMAMOUNT, REDCOMPENSATIONAMOUNT, REDAFTERCOMPENSATIONAMOUNT, REDLATEFEEAMOUNT, REDAFTERLATEFEEAMOUNT, TOTALRECOVERYPREMIUM, COMPENSATIONAMOUNT, LATEFEEAMOUNT, REDATOTAL, REDAFTERRECOVERYTOTAL, REDUCTIONDATE, MITCORPUSAMT, MITINTEAMT, MITFINEAMT, MITCOMPDINTEAMT)
values ('787-503701143301829446', '2037/08/02', 6142.92, null, 0.00, null, 286.89, null, '2037/08/02', 0.00000000, null, '2037/08/02', '0', 0, '2034/11/11', null, null, null, null, '1', null, '7018', 80, null, null, '2034/11/11 06:41:34', '2034/11/11 14:28:33', 6046.13, null, 96.79, null, 0.00, null, 0.000000, null, 0.000000, null, null, null, '37881516000192', '2015121700000369', 0.000000, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null);



update acct_loan a set a.loanstatus='1',a.finishdate ='2037/08/02' where a.serialno = '787-503701143301829446';

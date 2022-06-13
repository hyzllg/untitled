select * from system_setup;
update system_setup set businessdate = '2029/12/27',batchdate = '2029/12/27' where systemid = '1';
--授信流程节点（渠道申请流水号）
select * from queue_task qm where qm.objectno = '202205160000000018'
and qm.objecttype = 'jbo.channel51.CHANNEL_APPLY_INFO' order by runtime,create_date desc;
--支用流程节点（借款流水号）
select * from queue_task qm where qm.objectno = '20220516000006001'
and qm.objecttype = 'jbo.app.PUTOUT_APPROVE' order by runtime,create_date desc --for update;
--黑瞳复用
select * from third_relative where customerid = '320000001252545';
--黑瞳调用
select * from HEITONG_RESULT WHERE customerid = '320000001252784';
--黑瞳高危
select * from heitong_high_risk where customerid = '320000001252781';
select * from heitong_high_risk where OBJECT_NO = '20220513000000002';
select * from trans_log where applyno = '202205130000000007' and Servicename = 'HeiTongAntiFraudService';
select * from trans_log where customerid = '320000001252540';
select * from trans_log where servicename like '%AntiFraud%';
select * from queue_model where item = 'AntiFraudCommon';
--ilog规则集结果
SELECT * FROM ILOG_RULES_RESULT c WHERE c.applyno = '202205130000000003';
SELECT * FROM ILOG_RULES_RESULT c WHERE c.customerid = '320000001252537';

select * from BUSINESS_INSURANCEPOLICYINFO
select * from channel_apply_info where customerid = '320000001250737';
select * from acct_loan where serialno = '787-503904153301878159' for update;
select * from acct_payment_schedule where objectno = '787-503904153301878159' for update;
select * from loan_batch_notice where billno='787-503904153301878159' for update;


(
'787-503011153301619141',
'787-502405013300211806',
'787-502405013300211804',
'787-502901152980168910',
'787-502811012980162506',
'787-502811012980162614'  
)

select * from acct_payment_schedule_not where objectno = '787-502811012980162639' --for update;

             SELECT SERIALNO,LOANSTATUS as STATUS,POLICYNO,DDPRODUCTID,CAPITALCODE
                FROM ACCT_LOAN AL
               WHERE CAPITALCODE = '787'
               AND AL.DDPRODUCTID in ('7015','7018')
               AND LOANSTATUS = '7' and serialno = '787-503904283301878839'
               
               
update customer_info set liveaddress = '北京市市辖区东城区' where CERTID = '130324199302155110';
update customer_info set liveaddress = '北京市市辖区东城区' where CERTID = '33032719891121443X'
select liveaddress from customer_info where certid in ('130324199302155110','33032719891121443X') ;
select cooperate,serialno from acct_loan where putoutno in( 'PBLG202231171845000509');

select * from acct_loan a  join (select cooperate from acct_loan where putoutno in( 'PBLG202231171845000509') group by cooperate) b on a.cooperate=b.cooperate;








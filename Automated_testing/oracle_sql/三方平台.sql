--国政通
select * from GDTP_LOG_EX_PLATFORM_GZT;
select * from GDTP_GZT_DISHONEST_REQ;
select * from GDTP_GZT_DISHONEST_RES;
--三方公安分数
select * from GDTP_GAW_COMPARE_REQ;
select * from GDTP_GAW_COMPARE_RES ;
select * from gdtp_log_ex_platform_rule;
select * from GDTP_LOG_EX_PLATFORM_GAW;

--百融自然人
select * from GDTP_LOG_EX_PLATFORM_BAIRONG ;--日志表
select * from GDTP_BR_BERFOR_LOAN_REQ ;--请求表
select * from GDTP_BR_BERFOR_LOAN_RES ;--返回表
--黑瞳高危
select * from GDTP_LOG_EX_PLATFORM_HEITONG where apply_no = '202107130000000001';
select * from GDTP_HEITONG_HIGH_RISK_REQ where id_number = '210803199509207358';
select * from GDTP_HEITONG_HIGH_RISK_RES where serial_no = '6F3566FE-F664-4ECE-A81A-0D6FB68BD0EF';

--三方挡板
select * from GDTP_CONF_BAFFLE_INFO;

--法院限高
select * from GDTP_LOG_EX_PLATFORM_BAIRONG where serial_no = 'E2DFF49B-BC96-4DB2-A904-8F9F3373089A';
select * from GDTP_BR_EXECUTION_LIMIT_REQ where serial_no = '365A7822-D933-46A5-89EF-750B5748BB20';
select * from GDTP_BR_EXECUTION_LIMIT_RES where serial_no = '365A7822-D933-46A5-89EF-750B5748BB20';
select * from GDTP_BR_EXECUTION_LIMIT_XG_RES where serial_no = '8232D8E2-BF63-47CA-897B-613656AA5552';
select * from GDTP_BR_EXECUTION_LIMIT_SX_RES where serial_no = '8232D8E2-BF63-47CA-897B-613656AA5552';

--手机实名认证
select * from GDTP_LOG_EX_PLATFORM_LT  where serial_no = '72D34273-C3EF-42B4-89D4-401C9B004879';
select * from GDTP_LT_PHONE_AUTH_RES where serial_no = '20325EF5-D4C9-494C-8FF2-308570E52CA3';
select * from GDTP_LT_PHONE_AUTH_RES where serial_no = '20325EF5-D4C9-494C-8FF2-308570E52CA3';

--四要素
select * from GDTP_LOG_EX_PLATFORM_ZCX;
select * from GDTP_ZCX_BANK_CARD_REQ;
select * from GDTP_ZCX_BANK_CARD_RES;


--调用比例
select * from GDTP_XSHX_RULE_CONFIG where product_id = '7015';
--interface_type 1=三要素，6=四要素
select * from GDTP_XSHX_RULE_CONFIG_ITEM where serial_no in (select serial_no from GDTP_XSHX_RULE_CONFIG where product_id = '7014' and interface_type = '6');

select * from GDTP_XSHX_RULE_CONFIG where product_id = '7014' and interface_type = '1'
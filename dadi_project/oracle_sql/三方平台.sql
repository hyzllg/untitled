--����ͨ
select * from GDTP_LOG_EX_PLATFORM_GZT;
select * from GDTP_GZT_DISHONEST_REQ;
select * from GDTP_GZT_DISHONEST_RES;
--������������
select * from GDTP_GAW_COMPARE_REQ;
select * from GDTP_GAW_COMPARE_RES ;
select * from gdtp_log_ex_platform_rule;
select * from GDTP_LOG_EX_PLATFORM_GAW;

--������Ȼ��
select * from GDTP_LOG_EX_PLATFORM_BAIRONG ;--��־��
select * from GDTP_BR_BERFOR_LOAN_REQ ;--�����
select * from GDTP_BR_BERFOR_LOAN_RES ;--���ر�
--��ͫ��Σ
select * from GDTP_LOG_EX_PLATFORM_HEITONG where apply_no = '202107130000000001';
select * from GDTP_HEITONG_HIGH_RISK_REQ where id_number = '210803199509207358';
select * from GDTP_HEITONG_HIGH_RISK_RES where serial_no = '6F3566FE-F664-4ECE-A81A-0D6FB68BD0EF';

--��������
select * from GDTP_CONF_BAFFLE_INFO where INTERFACE_NAME in ('�ֻ�ʵ��','���п���Ҫ��','����ƽ̨-��������-�����ѯ�ӿ�');

select * from GDTP_CONF_BAFFLE_INFO where interface_name = '������ʵ������' for update;

select * from Gdtp_Nifa_Amount_Res
select * from Gdtp_Nifa_Credit_res

--��Ժ�޸�
select * from GDTP_LOG_EX_PLATFORM_BAIRONG where serial_no = 'E2DFF49B-BC96-4DB2-A904-8F9F3373089A';
select * from GDTP_BR_EXECUTION_LIMIT_REQ where serial_no = '365A7822-D933-46A5-89EF-750B5748BB20';
select * from GDTP_BR_EXECUTION_LIMIT_RES where serial_no = '365A7822-D933-46A5-89EF-750B5748BB20';
select * from GDTP_BR_EXECUTION_LIMIT_XG_RES where serial_no = '8232D8E2-BF63-47CA-897B-613656AA5552';
select * from GDTP_BR_EXECUTION_LIMIT_SX_RES where serial_no = '8232D8E2-BF63-47CA-897B-613656AA5552';

--�ֻ�ʵ����֤
--��ͨ
select * from GDTP_LOG_EX_PLATFORM_LT  where serial_no = '72D34273-C3EF-42B4-89D4-401C9B004879';
select * from GDTP_LT_PHONE_AUTH_RES where serial_no = '20325EF5-D4C9-494C-8FF2-308570E52CA3';
select * from GDTP_LT_PHONE_AUTH_RES where serial_no = '20325EF5-D4C9-494C-8FF2-308570E52CA3';
--����
select * from GDTP_LOG_EX_PLATFORM_BAIHANG where SERIAL_NO = '86AABE22-B5E3-403E-B479-CB1852C8FA96';
select * from GDTP_BAIHANG_PHONE_REQ where SERIAL_NO = '86AABE22-B5E3-403E-B479-CB1852C8FA96';
select * from GDTP_BAIHANG_PHONE_RES where SERIAL_NO = '86AABE22-B5E3-403E-B479-CB1852C8FA96';

--��Ҫ��
--�г���
select * from GDTP_LOG_EX_PLATFORM_ZCX where SERIAL_NO = 'E5054FEC-9015-45F6-B841-673993FB96AA';
select * from GDTP_ZCX_BANK_CARD_REQ;
select * from GDTP_ZCX_BANK_CARD_RES;
--����
select * from GDTP_LOG_EX_PLATFORM_BAIHANG;
select * from GDTP_BAIHANG_BANK_CARD_REQ where SERIAL_NO = '31BC94B0-0E08-46C6-BA9A-8E987A2DE82B';
select * from GDTP_BAIHANG_BANK_CARD_RES where SERIAL_NO = '31BC94B0-0E08-46C6-BA9A-8E987A2DE82B';

--ilog5,ilog9���ű�������ӹ�
select * from GDTP_XSFK_ILOG5_RES_EXTEND;
select * from GDTP_XSFK_ILOG9_RES_EXTEND;


--���ñ���
select * from GDTP_XSHX_RULE_CONFIG where prod uct_id = '7015';
--interface_type 1=��Ҫ�أ�6=��Ҫ��
select * from GDTP_XSHX_RULE_CONFIG_ITEM where serial_no in (select serial_no
from GDTP_XSHX_RULE_CONFIG where product_id = '7018' and interface_type = '6');

select * from GDTP_XSHX_RULE_CONFIG where product_id = '7014' and interface_type = '1'

--����
select * from GDTP_LOG_EX_PLATFORM_NIFA where to_char(create_time,'yyyy-mm-dd hh24:mi:ss') like '2022-03-17 11:%';
select * from Gdtp_Nifa_Amount_Req;
select * from Gdtp_Nifa_Amount_Res;
select * from Gdtp_Nifa_Credit_Info_Res;
select * from gdtp_nifa_amount_res;

import Collect



loanNo = "787-502807273301494658"
ACCT_PAYMENT_SCHEDULE = list(Collect.sql_cha(Collect.zwSIT_ORACLE,
                                             "select paycorpusamt，actualpaycorpusamt,payinteamt,actualpayinteamt,payfineamt,actualfineamt,paycompdinteamt,actualcompdinteamt,payfeeamt1,actualpayfeeamt1 from ACCT_PAYMENT_SCHEDULE where objectno = '{}'".format(
                                                 loanNo)))
for i in ACCT_PAYMENT_SCHEDULE:
    list
print(ACCT_PAYMENT_SCHEDULE)
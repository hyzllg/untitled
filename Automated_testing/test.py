import datetime
import random
import time
import winreg
import cx_Oracle

import Collect



def productid(loanNo):
    sql = f"select businesstype from ACCT_PAYMENT_SCHEDULE where objectno = '{loanNo}'"
    productid = Collect.sql_cha(enumerate,sql)[0][0]
    print(productid)
    return productid

productid('787-502807223301439911')
print(productid())
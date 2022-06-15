from credit_xb.dd_7014 import tc_main
from credit_xb.dd_7015 import main_360
from credit_xb.dd_7017 import hb_main
from credit_xb.dd_7018 import pp_main

def main():
    #环境（sit,uat,dev）
    environment = "sit"
    #走数据笔数
    number = 1
    #放款金额
    repayAmount = 5000
    # 借款金额
    loanAmount = 2000
    # 期数
    periods = "6"
    # 客户类型,0是新用户，1是存量活跃，2是存量静默
    custType = "0"
    # 客户等级
    custGrde = 18
    # 折后利率
    discountRate = 18
    # 资方编码 富邦银行：FBBANK 龙江银行：LJBANK 河北银行: HBBank
    capitalCode = "FBBANK"
    #龙江放款mock，设定放款日期
    # loan_datetime = "2021-09-16"

    #甜橙
    tc_main(number, repayAmount, loanAmount, periods, custType, capitalCode, environment.upper())
    #360
    main_360(environment.upper(), number, loanAmount, periods, custGrde, capitalCode)
    #还呗
    hb_main(environment.upper(), number, loanAmount, periods, custGrde, discountRate)
    #拍拍贷
    pp_main(environment.upper(), number, loanAmount, periods, custGrde)

if __name__ == '__main__':
    main()
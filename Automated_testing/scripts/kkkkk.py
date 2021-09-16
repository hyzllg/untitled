import Collect

# （参数1：apply/query；参数2：流水号；参数3：放款时间，格式y-m-d)
ljreqno = Collect.random_number_reqno()
Collect.update_lj_mock("apply", ljreqno, ljreqno)
Collect.update_lj_mock("query", ljreqno, ljreqno)
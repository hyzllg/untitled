import Collect
import time



ljreqno = Collect.ljReqNo()
Collect.update_lj_mock("apply", ljreqno, time.strftime("%Y-%m-%d"))
Collect.update_lj_mock("query", ljreqno, time.strftime("%Y-%m-%d"))

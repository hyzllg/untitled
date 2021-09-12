import Collect
import time


ljreqno = Collect.random_number_reqno()
Collect.update_lj_mock("apply", ljreqno, time.strftime("%Y-%m-%d"))
Collect.update_lj_mock("query", ljreqno, time.strftime("%Y-%m-%d"))

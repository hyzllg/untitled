import pytest
from page.insure_info_api_test import rd_excle_data
from page.insure_info_api_test import wd_excle_data
from page.insure_info_api_test import InsureInfo_request





class Test_InsureInfo:
    @pytest.mark.parametrize("data",rd_excle_data())
    def test_case_01(self,data):
        result = InsureInfo_request(data)
        wd_excle_data([data[0],result])
        assert result["msg"] == "SUCCESS!" and result["data"]["code"] == "0001" and "不允许为空" in result["data"]["message"]


if __name__ == '__main__':
    pytest.main(["-vs","test_insure_info_case.py::Test_InsureInfo"])

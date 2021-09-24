import pytest
from page.insure_info_api_test import rd_excle_data
from page.insure_info_api_test import InsureInfo_request





class Test_InsureInfo:
    @pytest.mark.parametrize("data",rd_excle_data())
    def test_case_01(self,data):
        result = InsureInfo_request(data)
        print(result)
        assert result["msg"] == "SUCCESS!"


if __name__ == '__main__':
    pytest.main(["-vs","test_insure_info_case.py::Test_InsureInfo"])

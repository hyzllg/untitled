import pytest

class Test_wo:
    def test_01(self,set_global_data,get_global_data):
        set_global_data("1","2")
        assert 1 == get_global_data("1")


def main():
    pytest.main(['-vs', 'ceshi.py::Test_wo::test_01'])
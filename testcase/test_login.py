import pytest

import Pytest.test0312


class Testlogin:
    @pytest.mark.smoke
    # @pytest.mark.skip
    def test001(self):
        result = Pytest.test0312.Mytestcase().test_001(3,26.66)
        assert result == '1.147'

if __name__ == '__main__':
    pytest.main(['-m','smoke'])
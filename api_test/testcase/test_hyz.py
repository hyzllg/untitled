import pytest




@pytest.mark.usefixtures('datas')
class Test_TianCheng:


    #甜橙授信申请接口
    @pytest.mark.run(order=1)
    def test_credit_granting(self,set_global_data):
        hyz = "hyz"
        print('''wowowowo''')
        set_global_data('hyz',hyz)

    #因授信需要时间，顾授信查询接口设置成重跑16此，每次间隔3秒
    @pytest.mark.flaky(reruns=16, reruns_delay=3)  # reruns代表重试次数，reruns_delay代表间隔时间
    @pytest.mark.run(order=2)
    def test_credit_inquiry(self,get_global_data):
        llg = get_global_data('hyz')
        assert llg==1

    @pytest.mark.run(order=3)
    def test_credit_inquiry2(self):
        llg = 32
        assert llg==1


def main():
    pytest.main(['-vs', 'tiancheng.py::Test_TianCheng'])
if __name__ == '__main__':
    main()

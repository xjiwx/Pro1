from src.Common.login import Login
# from selenium import webdriver
# from time import sleep
import pytest
class Test_Login(Login):
    def setup_method(self):
        print('开始')

    @pytest.mark.parametrize('username,password,result', [('17701293276', '123456', '退出')])
    def test_loginSuccess(self,username,password,result):
        result= self.loginsuces(username=username,password=password)
        assert result == result

    @pytest.mark.parametrize('username,password,fault_text',[(None,'admin','手机号不能为空'),
                                                                 ('admin',None,'手机号格式不正确！'),
                                                                 ('17701293276','admin','手机号或密码错误！')
                                                             ]
                             )
    def test_loginFailed(self,username,password,fault_text):
        fault_text = self.loginfailed(username=username,password=password)
        assert fault_text == fault_text


    def teardown_method(self):
        print('结束')

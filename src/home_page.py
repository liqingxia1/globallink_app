import time

from src.start_devices import Mobile
from src.general import logcat as log

class HomePage(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def str_server(self,username, password):
        ''' 启动服务，若未登录，则直接进行登录后启动服务'''
        print(">>>>>>>>>>  【首页】点击启动服务；若未登录，则直接进行登录操作  <<<<<<<<<<")
        Mobile.device.find_element_by_id("btn_home_start_csim").click()
        time.sleep(3)

        if  Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/tv_endtime"):
            print("【首页】启动服务中...")
            time.sleep(10)
            Mobile.general.screenshot("【首页】启动服务10m后")
        else:
            print(">>>>>>>>>>  【首页】启动服务，未登录用户，执行登录操作  <<<<<<<<<<")
            HomePage().user_login(username,password)
            Mobile.general.screenshot("【首页】启动服务失败")


    def user_login(self, username, password):
        '''登录界面  输入用户名与密码,进行登录操作'''
        print(">>>>>>>>>>  【首页】登录，输入用户名与密码，并点击登录按钮  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/et_login_name").send_keys(username)
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/login_pwd_ed").send_keys(password)
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/login_btn").click()
        Mobile.device.wait_activity(".ui.activity.SplashActivity", 10, 1)


    def click_endtime(self):
        '''点击有效期限'''
        print(">>>>>>>>>>  【首页】点击套餐有效期  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/tv_endtime").click()


    def click_home(self):
        '''点击首页'''
        print(">>>>>>>>>>  点击 【首页】  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rb_home").click()

    def check_server_state(self):
        '''检查服务是否启动成功'''
        print(">>>>>>>>>>  【首页】检查服务是否启动成功  <<<<<<<<<<")
        pass




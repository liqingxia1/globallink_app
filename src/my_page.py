import time
from src.general.key_event import KeyEvents
from src.start_devices import Mobile


class MyPage(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __sleep(func):
        def inner(self):
            time.sleep(1)
            return func(self)
        return inner

    @__sleep
    def click_person(self):
        '''点击个人'''
        print(">>>>>>>>>>  点击 【个人】  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rb_my").click()

    @__sleep
    def click_balence(self):
        '''进入余额界面 '''
        print(">>>>>>>>>>  【个人】进入余额界面  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rl_account_balence").click()

    @__sleep
    def click_account(self):
        '''点击我的账户'''
        print(">>>>>>>>>>  【个人】进入我的账户界面  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rl_my_account").click()

    @__sleep
    def click_business(self):
        '''点击业务查询'''
        print(">>>>>>>>>>  【个人】进入业务查询界面  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rl_business_query").click()

    @__sleep
    def click_msg(self):
        '''点击消息'''
        print(">>>>>>>>>>  【个人】进入消息界面  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rl_message_query").click()

    @__sleep
    def click_settings(self):
        '''点击设置'''
        print(">>>>>>>>>>  【个人】进入设置界面  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rl_settings").click()

    @__sleep
    def click_back(self):
        '''点击左上角返回图标'''
        print(">>>>>>>>>>  点击左上角返回图标  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/back_btn").click()

    @__sleep
    def get_login_number(self):
        '''余额 获取登录的账号'''
        print(">>>>>>>>>>  【个人-余额】获取当前登录账户信息  <<<<<<<<<<")
        number = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/et_recharge_num").text
        return number


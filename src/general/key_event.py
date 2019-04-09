from appium.webdriver.connectiontype import ConnectionType
import time
import os


class KeyEvents():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'  # ROBOT_LIBRARY_SCOPE为ROBOT库范围，这个范围有三个等级，分别是TEST CASE、TEST SUITE、GLOBAL三个等级，默认是TEST CASE，每个test case中引用都会实例化一次
    
    def __init__(self, device):
        self.device = device

    # 返回键
    def back(self):
        print(">>>>>>>>>>  【back】  <<<<<<<<<<")
        self.device.keyevent(4)

    # home键
    def home(self):
        print(">>>>>>>>>>  【home】  <<<<<<<<<<")
        self.device.keyevent(3)

    # 菜单键
    def menu(self):
        print(">>>>>>>>>>  【menu】  <<<<<<<<<<")
        self.device.keyevent(82)

    # 电源键
    def power(self):
         print(">>>>>>>>>>  【power】  <<<<<<<<<<")
         self.device.keyevent(26)

    # 音量加
    def volume_up(self):
         print(">>>>>>>>>>  【volume up】  <<<<<<<<<<")
         self.device.keyevent(24)

    # 音量减
    def volume_down(self):
         print(">>>>>>>>>>  【volume down】  <<<<<<<<<<")
         self.device.keyevent(25)

    # 拍照键
    def camera(self):
         print(">>>>>>>>>>  【camera】  <<<<<<<<<<")
         self.device.keyevent(27)

    # 清除
    def clear(self):
        print(">>>>>>>>>>  【clear】  <<<<<<<<<<")
        self.device.clear()

    def sleep(value):
        print(">>>>>>>>>>  【sleep】  <<<<<<<<<<")
        time.sleep(value)

    # 网络切换 开启 wifi
    def set_network_wifi(self):
         print(">>>>>>>>>>  【network WIFI】  <<<<<<<<<<")
         self.device.set_network_connection(ConnectionType.WIFI_ONLY)

    # 网络切换 飞行模式
    def set_network_airplane(self):
         print(">>>>>>>>>>  【network airplane】  <<<<<<<<<<")
         self.device.set_network_connection(ConnectionType.AIRPLANE_MODE)

    # 网络切换 关闭网络连接
    def set_network_none(self):
         print(">>>>>>>>>>  【close network】  <<<<<<<<<<")
         self.device.set_network_connection(ConnectionType.NO_CONNECTION)

    # 截屏
    def screenshot(self, png_name):
        print(">>>>>>>>>>  【screenshot】  <<<<<<<<<<")
        path = os.path.dirname(os.getcwd())
        png_path = os.path.join(path, 'case\error_png\\' + png_name + '.png')
        self.device.get_screenshot_as_file(png_path)


    # # 输入
    # def send_by_id(self,button,value):
    #      print(">>>>>>>>>>  【输入】%s  <<<<<<<<<<", value)
    #      self.device.find_element_by_id(button).send_keys(value)
    #
    # def send_by_classname(self,button,value):
    #      self.device.find_element_by_class_name(button).send_keys(value)
    #
    # def send_by_android(self,value):
    #      self.device.find_element_by_android_uiautomator(value)
    #
    # # 点击id 点击
    # def click_by_id(self, button):
    #      self.device.find_element_by_id(button).click()
    #
    # # 根据classname 点击
    # def click_by_classname(self, button):
    #      self.device.find_element_by_class_name(button).click()



from appium import webdriver
from Config.devices import Devices
from src.general.key_event import KeyEvents

class Mobile():
    device = None
    general = None
    def __init__(self, device_name='nox'):
        self.dev = Devices().get_device(device_name)


    def get_android(self,):
        ''' 根据config.ini配置文件中的信息，启动设备'''
        desired_caps = {
            'platformName': self.dev['platformName'],
            'deviceName': self.dev['deviceName'],
            'platformVersion': self.dev['platformVersion'],
            'appPackage': self.dev['appPackage'],  # APK包名
            'appActivity': self.dev['appActivity'],  # APK的Activity
            'unicodeKeyboard': self.dev['unicodeKeyboard'],  # 输入中文字符的时候appium server去被测试设备安装一个输入法可输入中文
            'newCommandTimeout': self.dev['newCommandTimeout'],  # 设置会话结束时间 appiumsever失效时间
            # 'udid': self.dev['udid']
        }
        Mobile.device = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) # 对应appium对象，固定值
        Mobile.general = KeyEvents(Mobile.device)


    def closeApp(self):
        # 退出当前app
        print(">>>>>>>>>>  【关闭app】  <<<<<<<<<<")
        self.device.quit()


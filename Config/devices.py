class Devices():
    '''
    def __init__ (self, name):
        self.name = name
    '''

    def get_device(self, name):
        self.name = name
        config = {
            'nox': {
                'platformName': 'Android',
                'deviceName': 'shell@msm8952_64',
                'platformVersion': '6.0.1',
                'appPackage': 'com.octopus.cloudshop',
                'appActivity': '.ui.activity.SplashActivity',
                'unicodeKeyboard': True,
                'newCommandTimeout': '6000',
                'udid': ''
                },
            'account':{
                'phonenumber':'13570818004',
                'password':'wq5201314b',
            }
        }
        return config[name]




from src.start_devices import Mobile
from src.home_page import HomePage
from src.my_page import MyPage
from src.shop_page import ShopPage
import time
from src.general import logcat

from src.general import logcat as log



if __name__=='__main__':
    logcat.clearlog()
    Mobile().get_android()
    time.sleep(5)
    home = HomePage()
    # shop = ShopPage()
    # my = MyPage()
    # home.str_server('13570818004','wq5201314b')
    # my.click_person()
    # my.click_balence()
    # if  my.get_login_number() == '13570818004':
    #     print("登录成功")
    # else:
    #     print("登录失败")
    # Mobile.general.back()
    # # my.click_account()
    # # my.click_back()
    # # my.click_business()
    # # my.click_back()
    # # my.click_msg()
    # # my.click_back()
    # # my.click_settings()
    # # my.click_back()
    # # home.click_home()
    # shop.click_shop()
    # # shop.get_shop_list()
    #
    # Mobile().closeApp()
    # logcat.getlog()




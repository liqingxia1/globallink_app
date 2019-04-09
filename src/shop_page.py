import time
from src.start_devices import Mobile

class ShopPage(Mobile):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __sleep(func):
        def inner(self):
            time.sleep(1)
            return func(self)
        return inner

    @__sleep
    def click_shop(self):
        '''点击商城'''
        print(">>>>>>>>>>  【商城】点击商城  <<<<<<<<<<")
        Mobile.device.find_element_by_id("com.octopus.cloudshop:id/rb_shop").click()

    @__sleep
    def get_shop_list(self):
        ''''''
        print(">>>>>>>>>>  【商城】左侧  <<<<<<<<<<")
        print(Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/set_item_first"))
        Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/set_item_first")[0].click()
        ShopPage().get_good_details()
        Mobile.device.keyevent(4)
        Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/set_item_first")[1].click()
        ShopPage().get_good_details()
        Mobile.device.keyevent(4)
        print(">>>>>>>>>>  【商城】获取更多  <<<<<<<<<<")
        print(Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/shop_item_more"))
        Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/shop_item_more")[0].click()
        Mobile.device.keyevent(4)
        Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/shop_item_more")[1].click()

        # Mobile.device.find_elements_by_id("com.octopus.cloudshop:id/set_item_first")[1].click

    @__sleep
    def get_good_details(self):
        '''获取商品详情，存入list中，并返回'''
        part = {}
        part['part_name'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/list_query_tv").text
        part['part_size'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/list_size_tv").text
        part['part_date'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/list_date_tv").text
        part['part_price'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/list_price_tv").text
        part['part_detail'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/mall_detail_tv").text
        part['part_goopoo'] = Mobile.device.find_element_by_id("com.octopus.cloudshop:id/mall_area_tv").text
        print(part)


    def click_banner(self):
        print(">>>>>>>>>>  【商城】点击banner图 <<<<<<<<<<")
        Mobile.device.find_elements_by_class_name("android.widget.ImageView").click()








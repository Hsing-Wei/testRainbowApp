import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class AppiumTest(unittest.TestCase):

    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "B2N"
        caps["appPackage"] = "cn.rainbow.westore"
        caps["appActivity"] = ".ui.LauncherActivity"
        caps["noReset"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def test_case(self):
        if self.driver.find_elements_by_id("bt_close") != []:
            self.driver.find_element_by_id("bt_close").click()
        self.driver.find_element(MobileBy.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.ImageView[3]").click()
        self.driver.find_element_by_id("cn.rainbow.westore:id/tv_search").click()
        self.driver.find_element_by_id("cn.rainbow.westore:id/titlebar_center_title").send_keys("月饼")
        self.driver.press_keycode(66)
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "美心双黄白莲蓉月饼")]').click()
        self.driver.find_element_by_id("cn.rainbow.westore:id/bt_add_cart").click()
        toast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert toast == '添加购物车成功！'

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
import allure
from allure_commons.types import AttachmentType

from pageObjects.LoginPage import LoginClass


class Test_UserLogin:

    @allure.feature('page_title')
    @allure.story("verifying page url")
    @allure.link('https://admin-demo.nopcommerce.com/', name='Nop Commerce Website')
    @allure.issue('ABC-123')
    @allure.title('test_verify_url')
    @allure.description('testing url')
    @allure.severity(allure.severity_level.CRITICAL)

    def test_user_login(self, setup):
        self.driver = setup
        self.lp = LoginClass(self.driver)
        self.lp.Enetr_Email('admin@yourstore.com')
        self.lp.Enter_Password('admin')
        self.lp.Click_Login()

        if self.lp.verify_login_status() == 'pass':
            allure.attach(self.driver.get_screenshot_as_png(), name ="test_user_login_pass",
                          attachment_type=AttachmentType.PNG)
            assert True
            self.lp.Click_Logout()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name ="test_user_login_fail",
                          attachment_type=AttachmentType.PNG)
            assert False


    @allure.severity(allure.severity_level.CRITICAL)
    def test_verify_url(self, setup):
        self.driver = setup
        if self.driver.title == "Your store. Login":
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_pass",
                          attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_fail",
                          attachment_type=AttachmentType.PNG)
            assert False

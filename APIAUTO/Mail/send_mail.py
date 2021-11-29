#encoding=utf-8
import unittest,time,traceback
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_SouhuMailSendMail(self):
        # 设定页面加载限制时间为4秒
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            self.driver.get("http://mail.126.com")
        except TimeoutException:
            print (u'页面加载超过设定时间，超时')
            self.driver.execute_script('window.stop()')
        try:
            # 切换进frame控件
            self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]"))
            #time.sleep(5)
            # 用户名
            userName = self.driver.find_element_by_xpath("//input[@data-placeholder='邮箱帐号或手机号码']")
            userName.send_keys("18801053303@126,com")
            # 密码
            pwd = self.driver.find_element_by_xpath("//input[@data-placeholder='输入密码' and @name='password']")
            pwd.send_keys("123456aa")
            # 登录按钮，回车代替
            pwd.send_keys(Keys.RETURN)
            # 显式等待，确认页面成功登录并跳转到登录成功后的首页
            wait = WebDriverWait(self.driver,10)
            wait.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="写 信"]')))
            time.sleep(2)
            self.driver.find_element_by_xpath('//span[text()="写 信"]').click()
            time.sleep(2)
            # 输入收件人
            receiver = self.driver.find_element_by_xpath("//*[contains(@id,'_mail_emailinput')]//input")
            receiver.send_keys("****")
            # 输入邮件标题
            subject = self.driver.find_element_by_xpath('//*[contains(@id,"subjectInput")]')
            subject.send_keys(u"这是一封测试邮件")
            # 获取邮件正文的富文本框
            iframe = self.driver.find_element_by_xpath("//*[contains(@id,'editor')]//iframe")
            self.driver.switch_to.frame(iframe)
            editBox = self.driver.find_element_by_xpath("/html/body")
            editBox.send_keys(u"邮件正文内容")
            self.driver.switch_to.default_content()
            # 点击发送按钮
            self.driver.find_element_by_xpath("//span[.='发送']").click()
            # 显式等待发送成功元素是否出现在页面上
            wait.until(EC.visibility_of_element_located((By.XPATH,"//*[contains(@id,'succInfo')]")))
            print(u"邮件发送成功")
        except TimeoutException:
            print(u"显式等待页面元素超时")
        except NoSuchElementException:
            print(u"寻找的页面元素不存在",traceback.print_exc())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
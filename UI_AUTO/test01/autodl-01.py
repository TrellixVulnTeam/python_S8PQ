#!C:\Users\张铁瀛\PycharmProjects\API_AUTO
# -*- coding: utf-8 -*-
# @Time : 2022/2/24 18:38
# @Author : ZhangTy
# @File : autodl-01.py
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://test.autodl.com:33443/login')
driver.set_window_size(1867, 864)
time.sleep(3)
print(driver.title)
# driver.find_element(By.CSS_SELECTOR, ".is-success .el-input__inner").send_keys("13522952212")
# driver.find_element(By.CSS_SELECTOR, ".el-form-item:nth-child(2) .el-input__inner").send_keys("123456Aa")
# driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
driver.find_element(By.CLASS_NAME, 'el-input__inner').send_keys("13522952212")
driver.find_element(By.CSS_SELECTOR,
                    '#app > div > div.login-center > div > div.function-component > div.content > form > div:nth-child(2) > div > div > input').send_keys(
    "123456Aa")
driver.find_element(By.CSS_SELECTOR,
                    '#app > div > div.login-center > div > div.function-component > div.content > form > div:nth-child(3) > div > button.el-button.el-button--primary.el-button--large').click()
time.sleep(3)
driver.quit()

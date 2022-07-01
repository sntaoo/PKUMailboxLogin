from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import PhantomJS
import time
import sys
import os

TIMEOUT = 5
TIMESLP = 3
CONFIGCODE = 1


def login(driver, username, password, failed=0):
    if failed == 3:
        raise Exception('邮箱登录失败')

    driver.get('https://mail.pku.edu.cn')

    print('邮箱登陆中...')
    driver.find_element_by_id('username').send_keys(username)
    time.sleep(TIMESLP)
    driver.find_element_by_id('password').send_keys(password)
    time.sleep(TIMESLP)
    driver.find_element_by_id('login_button').click()
    try:
        WebDriverWait(driver, TIMEOUT)
    except:
        login(driver, username, password, failed + 1)
    else:
        print('邮箱登录成功！')


def run(driver, username, password):
    login(driver, username, password)


if __name__ == '__main__':

    if sys.platform == 'darwin':  # macOS
        phantomjs_path = os.path.join('phantomjs', 'phantomjs-darwin')
    elif sys.platform == 'linux':  # linux
        phantomjs_path = os.path.join('phantomjs', 'phantomjs-linux-x86_64')
    else:  # windows
        phantomjs_path = os.path.join('phantomjs', 'phantomjs-windows.exe')

    driver = PhantomJS(executable_path=phantomjs_path)

    user_name = '此处改为学号(只要学号，不要@pku.edu.cn)'  # TODO
    password = '此处改为邮箱登陆密码'  # TODO
    run(driver, user_name, password)

    driver.close()

from unittest import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time


class Base(TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--dns-prefetch-disable")
        options.add_argument("enable-automation")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-site-isolation-trials")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get('https://svburger1.co.il/#/HomePage')
        self.driver.maximize_window()
        time.sleep(3)
        super(Base, self).setUp()


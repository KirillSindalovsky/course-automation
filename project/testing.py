from time import sleep
import random
from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys, ActionChains
from Utilities.base import Base


class SignUp(Base):

    # click on sing up button
    def click_sign_up(self):
        click_sign_up = self.driver.find_element_by_xpath('//*[@href="#/SignUp"]')
        click_sign_up.click()
        sleep(5)

    # click and input string to first name field
    def input_first_name(self):
        input_first_name = self.driver.find_element_by_xpath('//*[@placeholder="Type your first name"]')
        input_first_name.click()
        input_first_name.send_keys('test')
        sleep(5)

    # click and input string to last name field
    def input_last_name(self):
        input_last_name = self.driver.find_element_by_xpath('//*[@placeholder="Type your last name"]')
        input_last_name.click()
        sleep(2)
        input_last_name.send_keys('automation')
        sleep(5)

    # click and input email address
    def input_email_sing_up(self):
        input_email = self.driver.find_element_by_xpath('//*[@placeholder="Enter your email"]')
        input_email.click()
        sleep(2)
        input_email.send_keys('test_automation+{}@svcollege.co.il'.format(random.randint(0, 1000000)))
        sleep(5)

    # click and input password
    def input_pass(self):
        input_pass = self.driver.find_element_by_xpath('//*[@placeholder="Create Password"]')
        input_pass.click()
        sleep(2)
        input_pass.send_keys('123456')
        sleep(5)

    # click and input password conformation
    def input_confirm_pass(self):
        confirm_pass = self.driver.find_element_by_xpath('//*[@placeholder="Confirm Password"]')
        confirm_pass.click()
        sleep(5)
        confirm_pass.send_keys('123456')

    # click on submit button
    def click_submit(self):
        click_submit = self.driver.find_element_by_xpath('//*[@type="submit"]')
        click_submit.click()
        sleep(5)

    def test_sign_up(self):
        self.click_sign_up()
        self.input_first_name()
        self.input_last_name()
        self.input_email_sing_up()
        self.input_pass()
        self.input_confirm_pass()
        self.click_submit()


class LogIn(Base):

    # click on the login button
    def click_login(self):
        click_login = self.driver.find_element_by_xpath('//*[@href="#/SignIn"]')
        click_login.click()
        sleep(5)

    # input email address
    def input_email(self):
        input_email = self.driver.find_element_by_xpath('//*[@placeholder="Enter your email"]')
        input_email.click()
        sleep(2)
        input_email.send_keys('test_automation+123456@tt.it')
        sleep(5)

    # input password
    def input_pass(self):
        input_pass = self.driver.find_element_by_xpath('//*[@placeholder="Enter your password"]')
        input_pass.click()
        sleep(2)
        input_pass.send_keys('123456')
        sleep(5)

    # click on the button sign in
    def click_submit(self):
        click_submit = self.driver.find_element_by_xpath('//*[@type="submit"]')
        click_submit.click()
        sleep(10)

    # input not correct email address
    def input_email_error(self):
        input_email = self.driver.find_element_by_xpath('//*[@placeholder="Enter your email"]')
        input_email.click()
        sleep(2)
        input_email.send_keys('test_automation+123456tt.it')
        sleep(5)

    # accept the alert that pops up after trying to sign in with a "broken" email address
    def accept_the_alert(self):
        try:
            accept_the_alert = ActionChains(self.driver)
            accept_the_alert = accept_the_alert.send_keys(Keys.RETURN)
            accept_the_alert.perform()
            sleep(6)
            print("alert accepted")
        except:
            print("no alert")
            sleep(5)

#   def is_alert_present(self):
#     try:
#         self.driver.switch_to_alert()
#     except NoAlertPresentException:
#         return False

    # select all characters in the email input box and then delete
    def select_text_email_and_delete(self):
        email_text = self.driver.find_element_by_xpath('//*[@placeholder="Enter your email"]')
        email_text.send_keys(Keys.COMMAND, 'a')
        sleep(5)
        email_text.send_keys(Keys.DELETE)
        sleep(5)

    def test_login(self):
        self.click_login()
        self.input_email()
        self.input_pass()
        self.click_submit()

    def test_login_error(self):
        self.click_login()
        self.input_email_error()
        self.input_pass()
        self.click_submit()
        self.accept_the_alert()
        self.select_text_email_and_delete()
        self.input_email()
        self.click_submit()


class OrderItems(LogIn, Base):

    # select random meal
    def select_random_item(self):
        sleep(2)
        cards = self.driver.find_elements_by_css_selector('.productsMain > div > .card')
        rnd_idx = random.randint(0, len(cards) - 1)
        cards[rnd_idx].click()
        sleep(5)

    # get to reserve button and press return
    # cannot click on the button using xpath/css selector the element is being intercepted
    def go_to_reserve_and_press(self):
        sleep(5)
        N = 2
        actions_go_to_reserve = ActionChains(self.driver)
        for _ in range(N):
            actions_go_to_reserve = actions_go_to_reserve.send_keys(Keys.TAB)
        actions_go_to_reserve.perform()
        sleep(6)
        # press return on reserve button
        actions_click_on_reserve = ActionChains(self.driver)
        actions_click_on_reserve = actions_click_on_reserve.send_keys(Keys.RETURN)
        actions_click_on_reserve.perform()
        sleep(5)

    # there's a bug with this feature, able to order more than 2 items and proceed to checkout
    def order_multiple_items(self):
        order_items = self.driver.find_element_by_xpath('//input[@index="0"]')
        order_items.send_keys(Keys.BACKSPACE)
        sleep(2)
        order_items.send_keys('2')
        sleep(5)

    # enter a random coupon
    def add_coupon(self):
        add_coupon = self.driver.find_element_by_xpath('//*[@placeholder="XXX"]')
        add_coupon.click()
        sleep(2)
        add_coupon.send_keys(random.randint(100, 999))
        sleep(5)

    # add table number random from 1 to 99
    def add_table_no(self):
        add_table_no = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div['
                                                         '2]/div/div/div/div[2]/div[3]/div[5]/input')
        add_table_no.send_keys(Keys.BACKSPACE)
        sleep(2)
        add_table_no.send_keys(random.randint(1, 99))

    # click on the send button
    def click_on_send(self):
        click_send = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div['
                                                       '2]/div[4]/div[1]/button')
        click_send.click()
        sleep(10)

    def click_up(self):
        up = self.driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/div/div/div/div['
                                                       '2]/div[4]/div[1]/button')
        up.click()

    def test_order_items(self):
        self.click_login()
        self.input_email()
        self.input_pass()
        self.click_submit()
        self.select_random_item()
        self.go_to_reserve_and_press()
        self.order_multiple_items()
        self.add_coupon()
        self.add_table_no()
        self.click_on_send()

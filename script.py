# import unittest
# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# class PythonLogin(unittest.TestCase):
#
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#
#     def test_in_python_org(self):
#         driver = self.driver
#         driver.get("http://@staging-app-2.sourcebreaker.com/")
#         self.assertIn("SourceBreaker", driver.title)
#         username = driver.find_element_by_xpath("//input[@name='email']")
#         username.send_keys("levchenko.amgrade@gmail.com")
#         password = driver.find_element_by_xpath("//input[@name='password']")
#         password.send_keys("1")
#         loginbutton = driver.find_element_by_xpath("//input[@type='submit']")
#         loginbutton.click()
#         assert "No results found." not in driver.page_source
#         time.sleep(5)
#
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == "__main__":
#     unittest.main()
import time


def decorator(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print("--- {} time ---".format(time.time() - start_time))
        return f(*args, **kwargs)
    return wrapper

@decorator
def example(x):
    print('Called example function and param: ', x)

example(42)

def decorator(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            return function(*args, **kwargs) ** argument
        return wrapper
    return real_decorator


@decorator(2)
def funct_dec(number):
    return number

print(funct_dec(3))

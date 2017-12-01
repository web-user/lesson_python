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


class SchoolMember:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        """display information"""
        return 'Name:"{0}" Age:"{1}"'.format(self.name, self.age)


class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def tell(self):
        return super().tell(), 'Salary: "{0:d}"'.format(self.salary)


class Student(SchoolMember):
    """Represents a studenr"""
    def __init__(self, name, age, marks):
        self.marks = marks
        super().__init__(name, age)

    def tell(self):
        return [super().tell(), 'Marks: {0:d}'.format(self.marks)]

t = Teacher('Mrs, Shriv', 40, 30000)
s = Student('Swaroop', 25, 75)

print(t.tell())

members = [t, s]

for member in members:
    print(member.tell())



class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print('Sorry, minimum balance must be maintained.')
        else:
            BankAccount.withdraw(self, amount)

# class multifilter:
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         return True if pos >= neg else False

#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         return True if pos >= 1 else False

#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         return True if neg == 0 else False

#     def _construct_result(self, iterable, funcs, judge):
#         for elem in iterable:
#             pos = 0
#             neg = 0
#             for f in funcs:
#                 if f(elem):
#                     pos += 1
#                 else:
#                     neg += 1

#             if judge(pos, neg):
#                 self.result_iter.append(elem)

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         # iterable - исходная последовательность
#         # funcs - допускающие функции
#         # judge - решающая функция
#         self.result_iter = []

#         self._construct_result(iterable, funcs, judge)

#     def __iter__(self):
#         return iter(self.result_iter)

# def test():
#     def mul2(x):
#         return x % 2 == 0

#     def mul3(x):
#         return x % 3 == 0

#     def mul5(x):
#         return x % 5 == 0


#     a = [i for i in range(31)] # [0, 1, 2, ... , 30]

#     assert list(multifilter(a, mul2, mul3, mul5)) == [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#     assert list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)) == [0, 6, 10, 12, 15, 18, 20, 24, 30]
#     assert list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)) == [0, 30]

# if __name__ == "__main__":
#     test()

# import json
# import requests
# r = requests.get('https://jsonplaceholder.typicode.com/posts/2')

# v = r.json()
# print(v)
# print(v['title'])

import json
import requests
import re

# url = 'https://jsonplaceholder.typicode.com/users'

# users
# number 1

# params = dict(
#     name='users',
#     destination='1'
# )

# resp = requests.get(url)
# data = resp.json()

# print(data)

# url = 'https://jsonplaceholder.typicode.com/users'

# params = dict(
#     origin='1',
# )

# >>> payload = (('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'))
# >>> r = requests.get("http://httpbin.org/get", params=payload)
# >>> print r.json()['url']


# my_url = 'https://jsonplaceholder.typicode.com/' + 'users/' + '1'

# # yourparams = {'s' : 'value1', 'f': 'value2'}
# test = requests.get(my_url)


# def get_links(chat_string):
#     pattern = '(?:https?:\/\/)?(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)(?:\/[\w\.]*)*\/?' 
#     return re.findall(pattern, chat_string)

# links = test.json()
# print(links['phone'])

# url_post = 'https://jsonplaceholder.typicode.com/posts'


# param_post = {'_page' : '3', '_limit' : '1'}

# get_post = requests.get(url_post, params=param_post)

# res = get_post.json()

# print(res)


class MiniBlog:
    def __init__(self, posts, users):
        self.posts = posts
        self.users = users





# print(json.dumps('https://jsonplaceholder.typicode.com/posts/1'))
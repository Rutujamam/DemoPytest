import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

class Test_001:
    @pytest.mark.group1
    def test_sum_001(self):
        a =5
        b =6
        sum= a + b
        print(sum)
        if sum == 11:
            print("testcase test_sum_001 is passed")
            assert True
        else:
            print("testcase test_sum_001 is failed")
            assert False

    @pytest.mark.skip
    def test_mul_002(self):
        a=5
        b=6
        mul = a*b
        print(mul)
        if mul == 30:
            print("testcase test_mul_002 is passed")
            assert True
        else:
            print("testcase test_mul_002 is failed")
            assert False

    def sum_003(self):
        a=3
        b=5
        sum = a+b
        if sum == 8:
            assert True
        else:
            assert False

    def test_Google(self):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        print(logo)
        if logo == True:
            assert True
        else:
            assert False





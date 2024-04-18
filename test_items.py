""" Run test:
pytest --language=es test_items.py
pytest --language=fr test_items.py
"""

import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_should_present_button_add_to_basket(browser):
    res = False
    try:
        browser.get(link)
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        res=True
    finally:
        assert res, "Expected button w/class name 'btn-add-to-basket'"
        # 10 sec delay for visual confirmation
        time.sleep(10)

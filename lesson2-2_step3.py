from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try: 
    
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    y_element = browser.find_element_by_id("num2")
    x = int(x_element.text)
    y = int(y_element.text)
    c = x+y
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(c))

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 200);")

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_css_selector("#robotCheckbox")
    input2.click()

    input3 = browser.find_element_by_css_selector(".form-check.form-radio-custom>.form-check-input")
    input3.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
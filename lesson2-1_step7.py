from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_elementf = browser.find_element_by_id("treasure")
    x_element = x_elementf.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    input2 = browser.find_element_by_css_selector("#robotCheckbox")
    input2.click()

    input3 = browser.find_element_by_css_selector("#robotsRule")
    input3.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
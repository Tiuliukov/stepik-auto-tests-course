from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
  
    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
  
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    answ = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(answ)
    
    btn_solve = browser.find_element_by_id("solve")
    btn_solve.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


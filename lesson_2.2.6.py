from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try: 
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_id('answer')
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(y)
   
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotCheckbox)
    robotCheckbox.click()
    
    robotsRule = browser.find_element_by_id('robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', robotsRule)
    robotsRule.click()
    
    button = browser.find_element_by_tag_name('button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


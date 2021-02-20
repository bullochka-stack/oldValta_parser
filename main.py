#всего 4844
#242 раз
from selenium import webdriver
import time

PATH = 'C:/Users/TAMER/PycharmProjects/pythonProject1/msedgedriver.exe'
URL = 'http://old.valta.ru/catalog/'


driver = webdriver.Edge(PATH)

page = driver.get(URL)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='form-btn-region']/span").click()
time.sleep(2)

for i in range (0, 2, 1):
    driver.execute_script("window.scrollTo(0, 100)")
    driver.find_element_by_class_name("button-text").click()
    time.sleep(3)

products_links = driver.find_elements_by_class_name("p-lnk")

for i, word in enumerate(products_links):
    products_links[i] = products_links[i].get_attribute("href")
    if (products_links[i] == products_links[i-1]) & (i != 1):
        products_links.remove(i)
        continue
    print(products_links[i])
    print(len(products_links))


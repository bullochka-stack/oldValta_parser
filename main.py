#всего 4844
#242 раз
from selenium import webdriver
import time

PATH = "./msedgedriver.exe"
URL = 'http://old.valta.ru/catalog/'


driver = webdriver.Edge(PATH)

page = driver.get(URL)
time.sleep(3)
driver.find_element_by_xpath("//*[@id='form-btn-region']/span").click()
time.sleep(2)

for i in range(0, 242, 1):
    driver.execute_script("window.scrollTo(0, 100)")
    driver.find_element_by_class_name("button-text").click()
    time.sleep(3)

products_links = driver.find_elements_by_class_name("p-lnk")


for i, word in enumerate(products_links):
    products_links[i] = products_links[i].get_attribute("href")

y = products_links[::2]

with open('url_list.txt', 'a') as file:
    for line in y:
        file.write(f'{line}\n')

print(y)
print(len(y))


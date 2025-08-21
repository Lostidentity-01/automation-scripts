import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

fname = driver.find_element(By.NAME, "firstname")
lname = driver.find_element(By.NAME, "lastname")
male = driver.find_element(By.ID, "sex-0")
female = driver.find_element(By.ID, "sex-1")
exp_1yr = driver.find_element(By.ID, "exp-0")
exp_2yr = driver.find_element(By.ID, "exp-1")
exp_3yr = driver.find_element(By.ID, "exp-2")
exp_4yr = driver.find_element(By.ID, "exp-3")
exp_5yr = driver.find_element(By.ID, "exp-4")
exp_6yr = driver.find_element(By.ID, "exp-5")
exp_7yr = driver.find_element(By.ID, "exp-6")
date = driver.find_element(By.ID, "datepicker")
manual_tester = driver.find_element(By.ID, "profession-0")
auto_tester = driver.find_element(By.ID, "profession-1")
auto_uft = driver.find_element(By.ID, "tool-0")
auto_protractor = driver.find_element(By.ID, "tool-1")
auto_selenium = driver.find_element(By.ID, "tool-2")
continents_options = driver.find_element(By.ID, "continents")

fname.send_keys("<FIRSTNAME>")
lname.send_keys("<LASTNAME>")
male.click()
exp_1yr.click()
date.send_keys("20/08/2025")
driver.execute_script("arguments[0].scrollIntoView();", auto_tester)
auto_tester.click()
driver.execute_script("arguments[0].scrollIntoView();", auto_selenium)
auto_selenium.click()
time.sleep(10)

driver.quit()

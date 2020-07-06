import os
from selenium import webdriver
import datetime
import time

# chromedriver = "C:\\Users\\1\AppData\Local\Google\Chrome\Application\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)

# firefox = os.path.abspath(r"E:\Mozilla Firefox\firefox.exe")
# os.environ["webdriver.firefox.bin"] = firefox
# driver = webdriver.Firefox()
driver = webdriver.Firefox(executable_path='E:\Mozilla Firefox\geckodriver')
driver.maximize_window()

def login(uname, pwd):
  driver.get("https://www.taobao.com")
  if driver.find_element_by_link_text("亲，请登录"):
    driver.find_element_by_link_text("亲，请登录").click()
  input(uname, pwd)
  try:
    input(uname, pwd)
    print("no except")
  except:
    print("throws exception")
  if driver.find_element_by_id("J_SelectAll1"):
    driver.find_element_by_id("J_SelectAll1").click()
  # time.sleep(3)
  now = datetime.datetime.now()
  print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def input(uname,pwd):
  time.sleep(3)
  #密码登录
  # if driver.find_element_by_id("J_Quick2Static"):
  #   driver.find_element_by_id("J_Quick2Static").click()
  # time.sleep(3)
  if driver.find_element_by_name("TPL_username"):
    for i in uname:
      driver.find_element_by_name("TPL_username").send_keys(i)
      time.sleep(0.5)
  time.sleep(1)
  if driver.find_element_by_name("TPL_password"):
    for j in pwd:
      driver.find_element_by_name("TPL_password").send_keys(j)
      time.sleep(0.5)
  time.sleep(3)
  #登录按钮
  if driver.find_element_by_id("J_SubmitStatic"):
    driver.find_element_by_id("J_SubmitStatic").click()
  time.sleep(3)
  driver.get("https://cart.taobao.com/cart.htm")
  time.sleep(2)

def buy(buytime):
  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if now == buytime:
        try:
          if driver.find_element_by_id("J_Go"):
            driver.find_element_by_id("J_Go").click()
          driver.find_element_by_link_text('提交订单').click()
        except:
          time.sleep(1)
    print(now)
    time.sleep(1)
if __name__=="__main__":
  login("wch7932",'wch2wmt')
  buy('2019-11-11 13:00:00')
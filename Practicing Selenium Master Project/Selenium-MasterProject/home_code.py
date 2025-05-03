from selenium import webdriver
from selenium.webdriver.chrome.service import Service #agar humary paas chrome driver directly run nahi ho raha tou hum usko service ke zariye run kareingy

chromedriver_path = 'D:\Visual Studio Codes\SMIT 04 Selenium and it Master Project\Chrome Driver Filles\chromedriver-win64\chromedriver.exe'

ser = Service(chromedriver_path)
ser.start()

driver = webdriver.Chrome(chromedriver_path)
driver.maximize_window()


driver.get('https://www.audible.com/search')

#Getting info from the page
submenu = driver.find_element_by_xpath('//h2[contains(@id, "a-categories")]')
print(submenu.text)
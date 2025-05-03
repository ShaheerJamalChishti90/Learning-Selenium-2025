from selenium import webdriver
from selenium.webdriver.common.by import By

#setting up the webdriver
driver = webdriver.Chrome(executable_path="D:\Visual Studio Codes\SMIT 04 Selenium and it Master Project\Chrome Driver Filles\chromedriver-win64\chromedriver.exe")

#opening the website/webpage (using 365scores website)
driver.get("https://www.365scores.com/en-uk/football/match/premier-league-7/manchester-city-wolves-15-110-7#id=4147368")

# Locate an element using XPath (Locating the Man City)
# element = driver.find_element(By.XPATH, '//div[contains(@class, "ellipsis_container__ciMmU game-center-header-competitor_competitor_name__igII1 bold undefined ellipsis_line_clamp__-H088")]')

# print(element.text)  

driver.quit()  


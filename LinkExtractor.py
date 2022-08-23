from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import time


wb = Workbook()
worksheet = wb.active
page_url = "https://www.booking.com/searchresults.en-gb.html?ss=Nakuru&ssne=Nakuru&ssne_untouched=Nakuru&label=gen173nr-1DCAEoggI46AdIM1gEaHaIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AondkpgGwAIB0gIkOTdlZDhjZjktNmFhZC00MDdjLWE4M2YtN2UwYmM4MjkwOGJh2AIE4AIB&sid=d6e36a4d323b15bf1b13b8c8d8333168&aid=304142&lang=en-gb&sb=1&src_elem=sb&src=searchresults&dest_id=-2258197&dest_type=city&checkin=2022-09-01&checkout=2022-09-02&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(page_url)

for x in range(6):
     time.sleep(30)
     elements = driver.find_elements(By.CLASS_NAME, "d20f4628d0")
     row=0
     for e in elements:
        title_link = e.find_element(By.CLASS_NAME, "e13098a59f")
        title = e.find_element(By.CLASS_NAME, "fcab3ed991 ")
        worksheet.append([title.text, title_link.get_attribute('href')])
     button=driver.find_element(By.CLASS_NAME, "f78c3700d2")
     button.click()
     wb.save("nakuru_links.xlsx")
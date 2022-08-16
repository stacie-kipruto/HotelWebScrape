from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
warnings.filterwarnings('ignore')

workbook = xlsxwriter.Workbook('Hotelsurls.xlsx')
worksheet = workbook.add_worksheet()

page_url = "https://booking.com/searchresults.en-gb.html?label=gen173nr-1FCAEoggI46AdIM1gEaHaIAQGYAQm4ARfIAQzYAQHoAQH4AQuIAgGoAgO4AoCEqpcGwAIB0gIkZTBkYTQwNGEtZTY4My00ZDQ4LTkzNGUtOGE4ZTI5MDY1NjIx2AIG4AIB&sid=5b4a5551ec3b81adf3c882b5a770b551&checkin=2022-08-18&checkout=2022-08-19&dest_id=-2256513&dest_type=city&srpvid=67ec6e9e34eb0158&"
driver = webdriver.Chrome(executable_path="D:\selenium\chromedriver.exe")
driver.get(page_url)

for x in range(5):
     time.sleep(30)
     elements = driver.find_elements(By.CLASS_NAME, "d20f4628d0")
     row=0
     for e in elements:
        title = e.find_element(By.CLASS_NAME, "e13098a59f")
        worksheet.write(row, 0, title.get_attribute('href'))
        row+=1
     button=driver.find_element(By.CLASS_NAME, "f78c3700d2")
     button.click()
workbook.close()

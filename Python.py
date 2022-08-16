from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
#import numpy as np
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter
import warnings
warnings.filterwarnings('ignore')

#to get the webpage
page_url = "https://www.booking.com/hotel/ke/tune.en-gb.html?aid=304142&label=gen173nr-1DCAEoggI46AdIM1gEaHaIAQGYAQm4ARfIAQzYAQPoAQGIAgGoAgO4AsiOs5cGwAIB0gIkMGIxYmJiN2YtY2FjZS00ZjM0LTk3MTYtOWQ4MTJiMDNiYzBl2AIE4AIB&sid=d6e36a4d323b15bf1b13b8c8d8333168&all_sr_blocks=176566710_265986161_2_41_0;checkin=2022-08-18;checkout=2022-08-19;dest_id=-2258072;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=176566710_265986161_2_41_0;hpos=1;matching_block_id=176566710_265986161_2_41_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=176566710_265986161_2_41_0__7140;srepoch=1659721462;srpvid=2f777cba183d0314;type=total;ucfs=1&#hotelTmpl"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(page_url)

# babe note we have changed from find_elements to find_element
location = driver.find_element(By.CLASS_NAME, "hp_address_subtitle").text
#title = driver.find_elements(By.CLASS_NAME, "pp-header__title").text

#Get list of first row in every room type(notice if you want list you use find_elements)
roomtypes=driver.find_elements(By.XPATH, "//td[@rowspan]//parent::tr")

#To save the csv file
workbook = xlsxwriter.Workbook('Hotels.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0

#:)
for e in roomtypes:
    rtype = e.find_element(By.CLASS_NAME, "hprt-roomtype-icon-link").text
    price = e.find_element(By.CLASS_NAME, "prco-valign-middle-helper").text
    worksheet.write(row, 0, rtype)
    worksheet.write(row, 1, price)
    worksheet.write(row, 2, location)
    row += 1
    print({'location': location, 'rtype': rtype, 'price': price})

workbook.close()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import re
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.polygon.net")
######### ----Login Part------######
driver.find_element(By.ID, "loginLink").click()
username = driver.find_element(By.ID, 'Session_Username')
username.send_keys('142574')
password = driver.find_element(By.ID, 'Session_Password')
password.send_keys('diamond')
driver.find_element(By.XPATH, '//*[@id="memberLogin"]/div[5]/input').click()
try:
    driver.find_element(By.XPATH, '//*[@id="systemMessageDialog_modal"]/div/div/div[3]/a').click()
except:
    pass
# driver.find_element(By.XPATH, '//*[@id="systemMessageDialog_modal"]/div/div/div[3]/a').click()
######### ----Diamond search Part------######
driver.find_element(By.XPATH, '//*[@id="memberTabs"]/ul[2]/li[1]/a').click()
######### ----Filtering Part------######
# for k in range(1, 12):   
driver.find_element(By.ID, "criteria.shapeCode1").click() # Change the Shape type###########################
carat_min = driver.find_element(By.ID, 'criteria.caratWeightMin')
carat_min.send_keys('5')
carat_max = driver.find_element(By.ID, 'criteria.caratWeightMax')
carat_max.send_keys('5.99')
colorset = driver.find_element(By.ID, "criteria.colorMin")
driver.execute_script(
    "arguments[0].setAttribute('value','180_J')", colorset)
claritysetmax = driver.find_element(By.ID, "criteria.clarityMax")
driver.execute_script(
    "arguments[0].setAttribute('value','120_IFLC')", claritysetmax)
claritysetmin = driver.find_element(By.ID, "criteria.clarityMin")
driver.execute_script(
    "arguments[0].setAttribute('value','060_SI2')", claritysetmin)
gradesetmax = driver.find_element(By.ID, "criteria.cutGradeMax")
driver.execute_script(
    "arguments[0].setAttribute('value','040_VG')", gradesetmax)
gradesetmin = driver.find_element(By.ID, "criteria.cutGradeMin")
driver.execute_script(
    "arguments[0].setAttribute('value','040_VG')", gradesetmin)
driver.find_element(By.XPATH, '//*[@id="criteria.lab1"]').click()
driver.find_element(
    By.XPATH, '//*[@id="memberBodyLeft"]/p[1]/a[2]').click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="resultsPerPage"]')))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="resultsPerPage"]')))
select = Select(driver.find_element(By.XPATH, '//*[@id="resultsPerPage"]'))
select = Select(driver.find_element(By.XPATH, '//*[@id="resultsPerPage"]'))
select.select_by_value('100')
######### ----Scraping Part------######
diamond_list = []
shp = []
crt = []
clr = []
clrt = []
cutg = []
pricepc = []
tot = []
dep = []
tbl = []
fluo = []
time.sleep(5)
el = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
    (By.XPATH, '//*[@id="results"]/table/thead/tr[1]/td[2]/ul/li')))
    
total_iterator_count = int(el[len(el)-2].text)
print(total_iterator_count)
for i in range(0, total_iterator_count):
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="results"]/table/tbody')))
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="results"]/table/tbody')))
    tbody = driver.find_element(By.XPATH, '//*[@id="results"]/table/tbody')
    tbody = driver.find_element(By.XPATH, '//*[@id="results"]/table/tbody')
    try:
        rows = tbody.text.split('\n')
    except:
        break
    # print(rows)
    ############## ----To csv part-----------############

    ##################################################
    for row in rows:
        new_data = {}

        Shape = row.split(' ')[0]
        shp.append(Shape)
        new_data["Shape"] = Shape

        Carat = row.split(' ')[1]
        crt.append(Carat)
        new_data["Carat"] = Carat

        Color = row.split(' ')[2]
        clr.append(Color)
        new_data["Color"] = Color

        Clarity = row.split(' ')[3]
        clrt.append(Clarity)
        new_data["Clarity"] = Clarity

        CutGrade = row.split(' ')[4]
        cutg.append(CutGrade)
        new_data["CutGrade"] = CutGrade
        if CutGrade == "":
            row = re.sub(' +', ' ', row)
            pricepercarat = row.split(' ')[5]
            pricepc.append(pricepercarat)
            new_data["pricepercarat"] = pricepercarat

            Total = row.split(' ')[6]
            tot.append(Total)
            new_data["Total"] = Total

            Depth = row.split(' ')[7]
            dep.append(Depth)
            new_data["Depth"] = Depth

            Table = row.split(' ')[8]
            tbl.append(Table)
            new_data["Table"] = Table
            
            Fluorescence = row.split(' ')[9]
            fluo.append(Fluorescence)
            new_data["Fluorescence"] = Fluorescence
        else:
            pricepercarat = row.split(' ')[6]
            pricepc.append(pricepercarat)
            new_data["pricepercarat"] = pricepercarat

            Total = row.split(' ')[7]
            tot.append(Total)
            new_data["Total"] = Total

            Depth = row.split(' ')[8]
            dep.append(Depth)
            new_data["Depth"] = Depth

            Table = row.split(' ')[9]
            tbl.append(Table)
            new_data["Table"] = Table

            Fluorescence = row.split(' ')[10]
            fluo.append(Fluorescence)
            new_data["Fluorescence"] = Fluorescence
            

        diamond_list.append(new_data)

        dict = {'Shape': shp, 'Carat': crt, 'Color': clr, 'Clarity': clrt,
                'CutGrade': cutg, 'pricepercarat': pricepc, 'Total': tot, 'Depth': dep, 'Table': tbl, 'Fluorescence': fluo}

        df = pd.DataFrame(dict)

        df.to_csv('Result_diamond.csv')

    try:
        el = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//*[@id="results"]/table/thead/tr[1]/td[2]/ul/li')))
        if len(el) != 0:
            btn_next = el[len(el) - 1]
            btn_next.click()
    except:
        print("Info: Can't find Next button")

print(len(diamond_list))

while True:
    pass

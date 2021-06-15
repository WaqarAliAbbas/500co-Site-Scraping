# Developer Waqar Ali Abbas <---
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
url="https://500.co/startups?filter=1&region=&sector=&platform="
driver=webdriver.Chrome()
driver.get(url)
wait=WebDriverWait(driver,10)
while True:
    time.sleep(2)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Load More')]"))).click()
    except Exception as s:
        if "element click intercepted" in str(s):
            pass
        else:
            break
All_div=driver.find_elements_by_xpath('//tbody[@id="portfolioContainer"]/tr')[1:]
with open("sitedetails.csv","a",newline="") as f:
    file=csv.DictWriter(f,fieldnames=["name","website","country","sector","technology"])
    file.writeheader()
    for tr in All_div:
        try:
            Name=tr.find_element_by_xpath(".//td[@class='portfolio-name']").get_attribute("innerText")
        except:
            Name=""
        try:
            Website=tr.find_element_by_xpath(".//td[@class='portfolio-url']/a").get_attribute("href")
        except:
            Website=""
        try:
            Country=tr.find_element_by_xpath(".//td[@class='portfolio-country']").get_attribute("innerText")
        except:
            Country=""
        try:
            Sector=tr.find_element_by_xpath(".//td[@class='portfolio-sector']").get_attribute("innerText")
        except:
            Sector=""
        try:
            Technology=tr.find_element_by_xpath(".//td[@class='portfolio-platform']").get_attribute("innerText")
        except:
            Technology=""
        file.writerow(
            {
                "name":Name,
                "website":Website,
                "country":Country,
                "sector":Sector,
                "technology":Technology
            }
        )
        print(Name,Website,Country,Sector,Technology)
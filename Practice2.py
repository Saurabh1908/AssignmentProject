import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def Launch_browser():
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.redbus.in/")
    time.sleep(2)
    driver.save_screenshot('./Screenshots1/Launching_Browser.png')

def Input_Source_city():
    driver.find_element(By.ID,"src").send_keys("Mumbai")
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[text()='Borivali East']").click()
    time.sleep(5)
    driver.save_screenshot('./Screenshots1/Input-City.png')

def Input_Destination_city():
    driver.find_element(By.CSS_SELECTOR,"#dest").send_keys("Banglore")
    time.sleep(5)
    driver.find_element(By.XPATH,"//*[text()='Indiranagar']").click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,100)")
    time.sleep(4)
    driver.save_screenshot('./Screenshots1/Destination-City.png')

def date_pick():
    month_dates = driver.find_elements(By.XPATH,"//div[@class='DayTilesWrapper__RowWrap-sc-19pz9i8-1 fGGTDM']/span/div/span[not(contains(@class, 'DayTiles__CalendarDaysSpan-sc-1xum02u-1 gigHYE'))]")
    current_date = driver.find_element(By.XPATH, "//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 fgdqFw']")
    for i in month_dates:
        if i==current_date:
            driver.find_element(By.XPATH,"(//span[@class='DayTiles__CalendarDaysSpan-sc-1xum02u-1 dkWAbH'])[2]").click()
            driver.save_screenshot('./Screenshots1/Date-Select.png')

def search_button_click():
    search=driver.find_element(By.XPATH,"//*[text()='SEARCH BUSES']")
    search.click()
    time.sleep(3)
    driver.save_screenshot('./Screenshots1/Search-Button-Click.png')
def filter_buses():
    driver.find_element(By.XPATH,"//*[text()='SEATER']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//*[text()='AC']").click()
    time.sleep(3)
    driver.save_screenshot('./Screenshots1/Filter-Buses.png')
def find_lowest_fare_bus():
    driver.find_element(By.XPATH,"//a[text()='Fare']").click()
    time.sleep(3)
    element = driver.find_element(By.XPATH, "//*[text()='CLEAR ALL FILTERS']")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    time.sleep(4)
    buses= driver.find_elements(By.XPATH, "//div[@class='travels lh-24 f-bold d-color']")
    element1 = driver.find_element(By.XPATH,"//*[text()='SORT BY']")
    driver.execute_script("arguments[0].scrollIntoView();",element1)
    time.sleep(5)
    driver.save_screenshot('./Screenshots1/LowestFare-BusName.png')
    print("Lowest Fare Bus Name is:",buses[0].text)



Launch_browser()
Input_Source_city()
Input_Destination_city()
date_pick()
search_button_click()
filter_buses()
find_lowest_fare_bus()


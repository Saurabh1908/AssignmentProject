import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains



url = "https://www.redbus.in/"
input_src_city = "Mumbai"
actual_src_city = "Borivali East"
input_dest_city = "Banglore"
actual_dest_city = "Indiranagar"


def Launch_Browser():
    global driver
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.save_screenshot("./Screenshots/Launching-Browser.png")
    driver.maximize_window()
    driver.implicitly_wait(10)

def scroll_up():
    driver.execute_script("window.scrollTo(0,100)")
def input_source_city():
    driver.find_element(By.ID, "src").send_keys(input_src_city)
    time.sleep(2)
    from_city = driver.find_elements(By.XPATH, "//*[text()='Mumbai']/parent::div/parent::li/parent::ul/descendant::li")
    for city in from_city:
        # print(city.text)
        if actual_src_city in city.text:
            city.click()
            time.sleep(2)
            driver.save_screenshot("./Screenshots/Input-City.png")
            break


def input_destination_city():
    driver.find_element(By.CSS_SELECTOR, "#dest").send_keys(input_dest_city)

    to_city = driver.find_elements(By.XPATH, "//ul[@class='sc-dnqmqq eFEVtU']/li")
    time.sleep(2)
    for city in to_city:
        # print(city.text)
        if actual_dest_city in city.text:
            time.sleep(3)
            city.click()
            time.sleep(2)
            driver.save_screenshot("./Screenshots/Destination-City.png")
            break

def date_pick():
    current_month= driver.find_elements(By.XPATH,
                                      '//div[contains(@class,"DatePicker__CalendarContainer")]//div[contains(@class,"DayTilesWrapper__RowWrap")]//span//span[1]')

    current_Date = str(datetime.now().date()).split('-')[2]

    print(current_Date)
    for dates in current_month:
        date=dates.text
        if date=='4':
            if dates.text == str(date):
                    two_days_date_after_current_date = current_month.index(dates) + 2
                    current_month[two_days_date_after_current_date].click()
                    time.sleep(5)
                    driver.save_screenshot("./Screenshots/Date-Selected.png")
                    break
def click_search_button():
    # search=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='SEARCH BUSES']")))
    search = driver.find_element(By.CSS_SELECTOR,"#search_button")
    search.click()
    time.sleep(3)
    driver.save_screenshot("./Screenshots/Search-Button.png")

time.sleep(4)
def filter_type():
    # checkboxes=driver.find_elements(By.XPATH,"//ul[@class='list-chkbox']/li")
    checkboxes=driver.find_elements(By.XPATH,"//ul[@class='list-chkbox']//li/label[2]")
    checkbox1=driver.find_element(By.XPATH,"//*[text()='AC']")
    for checkbox in checkboxes:
        if checkbox==checkboxes[0] and checkboxes[2]:
            checkbox.click()
        else:
            pass
    checkbox1.click()
    driver.save_screenshot("./Screenshots/Filter-Buses.png")
    time.sleep(3)

def bus_names():

    driver.execute_script("window.scrollTo(0,5000)")
    names=driver.find_elements(By.XPATH,"//div[@class='clearfix bus-item-details']")
    time.sleep(4)
    driver.save_screenshot("/.ScreenshotsFilter-Buses.png")

    print("City count",len(names))
    for name in names:
        print(name.text)

def bus_names_lowest_fare():
     driver.execute_script("window.scrollTo(0,3000)")
     scroll_to_element = driver.find_element(By.XPATH, "//*[text()='CLEAR ALL FILTERS']")
     driver.execute_script("arguments[0].scrollIntoView();", scroll_to_element)
     time.sleep(4)
     bus_fares=driver.find_elements(By.XPATH,"//span[@class='f-19 f-bold']")
     l1=[]
     for price in bus_fares:
         l1.append(price.text)
     min_bus_fare=min(l1)
     ind_min_bus_fare = l1.index(min_bus_fare)
     bus_names = driver.find_elements(By.XPATH,"//div[@class='travels lh-24 f-bold d-color']")
     lowest_price_name= bus_names[ind_min_bus_fare].text
     driver.execute_script("window.scrollTo(0,5000)")
     time.sleep(5)
     action=ActionChains(driver)
     action.move_to_element(bus_fares[ind_min_bus_fare]).perform()
     time.sleep(5)
     driver.save_screenshot("./Screenshots/LowestFare-BusName.png")
     print("Lowest Fare Bus Name is",lowest_price_name)






Launch_Browser()
input_source_city()
input_destination_city()
scroll_up()
date_pick()
click_search_button()
filter_type()
bus_names()
bus_names_lowest_fare()


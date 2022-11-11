from pprint import pprint

import utils
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import chrome_webdrive, process_start_time, process_time, write_json_file


def print_element(elem):
    return str(elem.text.strip())


def google_maps_link(key, region, language):
    return 'https://www.google.com/maps/search/' + key + '/' + region + '?hl='+language


def check_element_precence_by_classname(driver, element_class_name):
    timeout = 2
    element_present = EC.presence_of_element_located((By.CLASS_NAME, element_class_name))
    WebDriverWait(driver, timeout).until(element_present)


start_time = process_start_time()
driver = chrome_webdrive()
driver.maximize_window()

# Language
arabe = "ar"
francais = "fr"
anglais = "en"

# Regions
grand_tunis = "@36.7970299,10.0157588,10.26z"
sousse = "@35.7829901,10.5572577,11.18z"
usa = "@38.7047142,-105.5977511,5z"

# Get the first google maps page
keyword = "Centre de formation".replace(" ", "+")
link = google_maps_link(keyword, grand_tunis, anglais)
driver.get(link)

# Check the "Update results when map moves" Button presence
button_classname = "jmUlyc-LaJeF-on-HG3vT-checkbox"
check_element_precence_by_classname(driver, button_classname)
driver.find_element_by_class_name(button_classname).click()


# link = google_maps_link(keyword, usa, anglais)
# driver.get(link)
# Get the needed region
# link = google_maps_link(keyword, usa, anglais)
# driver.get(link)

# Check the "loading" element presence
loading_classname = "wo1ice-loading"
try :
    check_element_precence_by_classname(driver, loading_classname)
except Exception as exp:
    pass

process_time(start_time)

i = 0
liste = []
while True:
    # Scroll down for the sidebar
    compteur_loading = 1
    while compteur_loading < 4:
        compteur_loading += 1
        try:
            element = driver.find_element_by_class_name(loading_classname)
            driver.implicitly_wait(2)
            webdriver.ActionChains(driver).move_to_element(element).perform()
            webdriver.ActionChains(driver).move_to_element(element).perform()
        except Exception as exp:
            pprint(exp)
            pass

    time.sleep(2)

    elements = driver.find_elements_by_xpath("//div[@class='Z8fK3b']")
    for element in elements:
        element_name = "None"
        element_rating = "None"
        element_adress = "None"
        element_time = "None"
        element_url = "None"

        try:
            element_name = element.find_element_by_css_selector("div.gm2-subtitle-alt-1").text
        except Exception as exp:
            pass

        try:
            element_rating = element.find_element_by_css_selector("span.gm2-body-2>span.ZkP5Je").text
        except Exception as exp:
            pass

        try:
            element_block = element.find_elements_by_css_selector("div.ZY2y6b-RWgCYc>div.ZY2y6b-RWgCYc")
            element_adress = element_block[0].text
            element_time = element_block[1].text
        except Exception as exp:
            pass

        try:
            element_url = driver.find_element_by_css_selector("[aria-label='"+element_name+"']").get_attribute('href')
        except Exception as exp:
            pass

        element_dict = dict(Name=element_name,
                            Rating=element_rating,
                            Adress=element_adress,
                            Time=element_time,
                            URL=element_url)
        print(element_dict)
        liste.append(element_dict)

    try:
        next_button_classname = "hV1iCc"
        next_button = driver.find_elements_by_class_name(next_button_classname)
        driver.implicitly_wait(5)
        next_button[1].click()
        print("____________________________")
        print(i)
        print("____________________________")
        i += 1

        liste_sorted = sorted(liste, key=lambda i: i['Rating'], reverse=True)

        # Saving Data
        write_json_file('Centre de formation.json', liste_sorted)

        time.sleep(7)

    except Exception:
        driver.close()
        break



# try:
#     element_name = element.find_element_by_css_selector("div.gm2-subtitle-alt-1").text
#     element_rating = element.find_element_by_css_selector("span.gm2-body-2>span.ZkP5Je").text
#     element_block = element.find_elements_by_css_selector("div.ZY2y6b-RWgCYc>div.ZY2y6b-RWgCYc")
#     element_adress = element_block[0].text
#     element_time = element_block[1].text

# element_image_src = element.find_element_by_class_name("image-container")
# element_url = search.find_elements_by_css_selector("[aria-label="+element_name.text+"]")

# print(element_name)
# print(element_rating)
# print(element_adress)
# print(element_time)
#
# elements_dict = dict(Name=element_name,
#                      Rating=element_rating,
#                      Adress=element_adress,
#                      Time=element_time,
#                      )
# liste.append(elements_dict)
#
# except Exception as exp:
# pprint(exp)
# pass


# CEO CXO
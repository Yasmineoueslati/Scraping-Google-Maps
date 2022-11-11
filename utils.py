import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time


# Using chrome
def chrome_webdrive():
    PATH = "C:\Program Files (x86)\Chrome web driver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    return driver


# Using Firefox
def firefox_webdrive():
    PATH = "C:\Program Files (x86)\Firefox web driver\geckodriver.exe"
    driver = webdriver.Firefox(executable_path=PATH)
    return driver


def process_start_time():
    return int((round(time.time() * 1000)) / 1000)


def process_time(start_time):
    process_time = int((round(time.time() * 1000))/1000) - start_time
    print(process_time)


def write_json_file(file_name, content):
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(content, f, indent=4, ensure_ascii=False)


def read_json_file(file_name, content):
    with open(file_name, 'r', encoding="utf-8") as f:
        json.dump(content, f, indent=4, ensure_ascii=False)


def try_exception(item, key):
    try:
        return item[key]
    except KeyError:
        return ""

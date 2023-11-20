from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from bs4 import BeautifulSoup

def scrap():
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
    class_name = ''
    # driver_path = 'C:/Program Files/Google/Chrome/chromedriver'
    driver_path = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(driver_path)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    all_div = soup.find_all('div', {"class": class_name})
    for i in all_div:
        print(i)
    driver.close()

def main():
    url = "http://www.naver.com"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(5)

if __name__ == '__main__':

    scrap()
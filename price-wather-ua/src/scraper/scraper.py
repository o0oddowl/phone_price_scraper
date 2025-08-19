import time
import random
import json
import csv

import fake_useragent
from bs4 import BeautifulSoup
from selenium import webdriver


def selenium(page = ""):
    driver = webdriver.Firefox()
     
    try:
        driver.get(f"https://rozetka.com.ua/ua/mobile-phones/c80003/{page}")
        time.sleep(10)
        with open(f"html_file/rozetka{page}.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        time.sleep(1)
    except Exception as e:
        print("SELENIUM ERROR:", e)
    finally:
        driver.quit()


def get_html(): 
    selenium("page=1")
    with open("../../html_file/rozetkapage=1.html") as file:
        scr = file.read()
    
    bs = BeautifulSoup(scr, "lxml")
    page = bs.find("div", class_=["list", "text-center"]).find_all("a", class_=["page", "text-2xl", "active"])[-1].text
    for num_page in range(2, int(page)+1):
        selenium(f"page={num_page}")
        print(num_page, "/", page)
    return int(page)   

def scraper():
    page = get_html()
    print(page)
    with open("../../data/mobile_price.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "phone_name",
                "status",
                "rating",
                "bonus",
                "price_before_discount",
                "price"            
            )
        )
    
    data = []
    for num_page in range(1, page+1):
        with open(f"../..html_file/rozetkapage={num_page}.html") as file:
            scr = file.read()
    
        bs = BeautifulSoup(scr, "lxml")
        content = bs.find_all("div", class_="content")
     
        for item in content:
            title = item.find("a", class_=["tile-title", "black-link", "text-base"]).text.strip()
            price = item.find("div", class_=["price", "color-red"]).text.strip().replace("\u00A0", "")[0:-1]
            try:
                old_price = item.find("div", class_=["old-price", "mb-1"]).text.strip().replace("\u00A0", "")[0:-1]
            except:
                old_price = 0
            try:
                rating = item.find("span", class_="rating-block-content").text.strip()
            except:
                rating = 0
            status = item.find("rz-tile-sell-status").text
            try:
                bonus = item.find("rz-tile-bonus").text.split()[0][1:]
            except:
                bonus = 0 
        
            data.append({
                "phone_name": title,
                "status": status,
                "rating": rating,
                "bonus": bonus,
                "price_before_discount": old_price,
                "price": price
            })
            with open("../data/mobile_price.csv", "a") as file:
                writer = csv.writer(file)
                writer.writerow(
                    (
                        title,
                        status,
                        rating,
                        bonus,
                        old_price,
                        price
                    )
                )
        with open("../../data/mobile_price.json", "a") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    scraper()

if __name__=="__main__":
    main()
    

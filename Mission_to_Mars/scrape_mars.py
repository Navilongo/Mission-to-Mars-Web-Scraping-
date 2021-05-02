# Download dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager





def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    news_title = soup.find_all('div', class_='content_title')[0].text
    
    news_p = soup.find_all('div', class_='article_teaser_body')[0].text
    
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    #scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")

    relative_image_path = soup.find_all('img')[1]['src']

    feature_image = url + relative_image_path

    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    #scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")
    print(soup.prettify())

    planet_profile_table = soup.find_all('table', class_= "table table-striped")
        
 
    mars_scraped = {
        "news_title": news_title,
        "news_p": news_p,
        "feature_image": feature_image,
        "planet_profile_table": str(planet_profile_table)
    }
    
    browser.quit()

    return mars_scraped
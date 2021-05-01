# Download dependencies
import os
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)



def scrape():
    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    soup = bs(browser.html, 'html.parser')

    print(soup.prettify())

    news_title = soup.find_all('div', class_='content_title')[0]
    news_title
    news_p = soup.find_all('div', class_='article_teaser_body')[0]
    news_p


    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    #scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")

    print(soup.prettify())

    relative_image_path = soup.find_all('img')[1]['src']
    relative_image_path


    feature_image = url + relative_image_path
    feature_image

    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)

    #scrape page into soup
    html = browser.html
    soup = bs(html, "html.parser")
    print(soup.prettify())

    planet_profile_table = soup.find_all('table', class_= "table table-striped")
    planet_profile_table


    url = "https://marshemispheres.com/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, "html.parser")
    print(soup.prettify())


    links = browser.find_by_css('a.product-item img')
    print(len(links))

    hemisphere_image_urls = []
    img_url = {}
    url = []

    for i,link in enumerate(links): 
        print(i, link)
        browser.find_by_css('a.product-item img')[i].click()
        
        titles = browser.find_by_css('h2.title').text
        print(titles)
        url = browser.find_by_css('li.href')
    
        img_url['title'] = titles
        img_url['img_url'] = url
        print(img_url)
        hemisphere_image_urls.append(img_url)
        browser.back()
        
    print(hemisphere_image_urls)


    print(img_url)

    print(hemisphere_image_urls)



    mars_scraped = {
        "news_title": news_title,
        "news_p": news_p,
        "feature_image": feature_image
        "planet_profile_table": str(planet_profile_table)
    }

    return mars_dict


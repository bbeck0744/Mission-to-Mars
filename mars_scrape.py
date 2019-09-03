# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:34:18 2019

@author: bbeck
"""

# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 

mars_info = {}

# Initialize browser
def init_browser():
    # Choose the executable path to driver 
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)

def mars_news():
    
    # Initialize browser 
    browser = init_browser()
    
    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    mars_info['news_title'] = news_title
    mars_info['news_p'] = news_p
    
    return mars_info

    # Close the browser after scraping
    browser.quit()



def mars_image():
    
    # Initialize browser 
    browser = init_browser()    

    # Visit Mars Space Images through splinter module
    image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url_featured)
    
    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + featured_image_url

    # Display full link to featured image
    featured_image_url

    mars_info['featured_image_url'] = featured_image_url
    
    return mars_info

    # Close the browser after scraping
    browser.quit()

def mars_weather():
    
    # Initialize browser 
    browser = init_browser()
    
    # Visit Mars Weather Report through splinter module
    html_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(html_weather)
    
    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_weather, 'html.parser')

    # Find all elements that contain tweets
    latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Find weather related tweets
    for tweet in latest_tweets: 
        weather_tweet = tweet.find('p', lang="en").text
        if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else: 
            pass
        
    mars_info['weather_tweet'] = weather_tweet
    
    return mars_info

    # Close the browser after scraping
    browser.quit()
    
def mars_facts():
    
    # Initialize browser 
    browser = init_browser()
    
    # Visit Mars Weather Report through splinter module
    html_facts = 'https://space-facts.com/mars/'
    browser.visit(html_facts)
    
    # HTML Object 
    html_facts = browser.html

    # Find table in using pandas
    tables = pd.read_html(html_facts)
    
    df = tables[0]
    df.columns = ['Description', 'Values', 'Earth']
    df=df.drop(['Earth'], axis=1)
    df.set_index('Description', inplace=True)

    # Save html code to folder Assets
    data = df.to_html()

    # Dictionary entry from MARS FACTS
    mars_info['mars_facts'] = data
    
    return mars_info

    # Close the browser after scraping
    browser.quit() 
    
def mars_hemispheres():
    
    # Initialize browser 
    browser = init_browser()
    
    # Visit Mars Weather Report through splinter module
    html_hemi = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(html_hemi)
    
    # HTML Object
    html_hemi = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemi, 'html.parser')
    
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_urls = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    for i in items:
        title = i.find('h3').text
        # Store link that leads to full image website
        partial_url = i.find('a', class_='itemLink product-item')['href']
        browser.visit(hemispheres_main_url + partial_url)
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
    
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')
    
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
    # Dictionary entry from MARS FACTS
    mars_info['hemisphere_image_urls'] = hemisphere_image_urls
    
    return mars_info

    # Close the browser after scraping
    browser.quit()
    

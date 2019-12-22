# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'



# %%
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
import os



# %%
# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
# get_ipython().system('which chromedriver')


# %%
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    # %%
    ### NASA Mars News
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)


    # %%
    html = browser.html
    soup = bs(html,"html.parser")


    # %%
    html


    # %%
    news_title = soup.find('div', class_='content_title').text
    print(news_title)

    news_p=soup.find('div', class_='article_teaser_body').text
    print(news_p)


    # %%
    ### JPL Mars Space Images - Featured Image
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search%3D%26category%3DMars'
    browser.visit(img_url)


    # %%
    secondclick = browser.find_by_id("full_image")
    secondclick.click()


    # %%
    thirdclick = browser.links.find_by_partial_text("more info")
    thirdclick.click()


    # %%
    html2=browser.html
    soup2=bs(html2,'html.parser')


    # %%
    soup2


    # %%
    partial_url = soup2.select_one('figure.lede a img').get("src")


    # %%
    full_url = f'https://www.jpl.nasa.gov{partial_url}'
    full_url


    # %%
    ### Mars Weather
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)


    # %%
    html3=browser.html
    soup3=bs(html3,'html.parser')


    # %%
    twitter= soup3.find("div", class_="js-tweet-text-container")
    twitter


    # %%
    twitter.find("p", "tweet-text").get_text()


    # %%
    mars_weather = twitter.find("p", "tweet-text").get_text()
    mars_weather


    # %%
    ### Mars Facts
    data_url = 'https://space-facts.com/mars/'
    browser.visit(data_url)


    # %%
    html4=browser.html
    soup4=bs(html4,'html.parser')


    # %%
    ### Mars table
    mars_data = pd.read_html(data_url)
    mars_data[0]
    mars_data_df=mars_data[0]


    # %%
    #Using Pandas to convert the data to a HTML table string.
    html_table=mars_data_df.to_html()
    html_table


    # %%
    mars_data_df.to_html('mars_table.html')


    # %%
    hemispheres_url= "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)


    # %%
    html5=browser.html
    soup4=bs(html5,'html.parser')


    # %%
    hemispheres = soup4.find_all('div', class_='item')
    print(hemispheres)


    # %%
    title_img_url = []


    # %%
    for hemisphere in hemispheres:
        
        title = soup4.find("h3").text
        
        img_url = soup4.find('a', class_='itemLink product-item')["href"]
        
        base_url = "https://astrogeology.usgs.gov"
        
        browser.visit(base_url + img_url)
        
        img_url_html = browser.html
        
        img_url_soup = soup4=bs(html5,'html.parser')
        
        full_image_url = base_url + img_url_soup.find("img",class_="thumb")["src"]
        
        title_img_url.append({"Title":title,"Img_url":full_image_url})


    # %%
    title_img_url

    # Store data in a dictionary
    mars_data1 = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": full_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_data,
        "hemisphere_image_urls": hemisphere_image_urls
        }




    # %%
    #Quit the Browser
    browser.quit()

        # Return results

    return mars_data1

    if __name__ == '__main__':
        scrape()
# %%



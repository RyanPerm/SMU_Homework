from splinter import Browser
from bs4 import BeautifulSoup as bsp
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time

class scrapeweb():
    def __init__(self):
        pass

    def init_browser(self):
        executable_path = {'executable_path': ChromeDriverManager().install()}
        browser = Browser('chrome', **executable_path)
        return browser
    
    def scrape_mars_info(self):

        scraped_data = {}
        browser = self.init_browser()

# NEWS

        url = "https://mars.nasa.gov/news/"
        browser.visit(url)
        time.sleep(2)

        soup = bsp(browser.html)
        slide = soup.find("li", {"class": "slide"})
        news_title = slide.find("div", {"class": "content_title"}).text.strip()
        news_p = slide.find("div", {"class": "article_teaser_body"}).text.strip()

# IMAGES

        # base = "https://www.jpl.nasa.gov"
        # url = f"{base}/spaceimages/?search=&category=Mars"
        # browser.visit(url)
        # time.sleep(2)

        # browser.find_by_id("full_image").click()
        # time.sleep(2)

        # browser.find_link_by_partial_text("more info").click()
        # time.sleep(2)

        # soup = bsp(browser.html)
        # image = soup.find("img", {"class": "main_image"})

        # image_url = base + image["src"]

# FACTS
        url = "https://space-facts.com/mars/"
        browser.visit(url)
        time.sleep(2)

        dfs = pd.read_html(browser.html)
        df = dfs[0]
        df.columns = ["Statistic","Value"]
        mars_facts = df.to_html(index=False)

# DATA

        base = "https://astrogeology.usgs.gov"
        url = f"{base}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
        browser.visit(url)
        time.sleep(2)

        soup = bsp(browser.html)
        links = soup.find("div", {"class": "results"}).findAll("a", {"class": "itemLink"})

        realLinks = []
        for link in links:
            image = link.find("img")
            if (image):
                realLinks.append(base + link["href"])
            
        hemi_data = []
        for realLink in realLinks:
            browser.visit(realLink)
            time.sleep(2)

            soup = bsp(browser.html)
            hemi_url = soup.find("ul").find("a")["href"]
            hemi_title = soup.find("h2", {'class', "title"}).text.split(" Enhanced")[0]
            hemi_data.append({"title": hemi_title, "url": hemi_url})
        
        browser.quit()

        scraped_data["news_title"] = news_title
        scraped_data["news_p"] = news_p
        #scraped_data["image_url"] = image_url
        scraped_data["mars_facts"] = mars_facts
        scraped_data["hemispheres"] = hemi_data

        return scraped_data

# -*- coding: utf-8 -*-
import scrapy
from one_page_scrap.items import OnePageScrapItem

import pandas as pd

class ReviewPageSpider(scrapy.Spider):
    name = 'review_page'
    allowed_domains = ['amazon.com/Clarks-Tilden-Walk-Leather-Brown/dp/B06XC432VT/ref=lp_18637582011_1_1?srs=18637582011']
    start_urls = ['https://www.amazon.com/Clarks-Tilden-Walk-Leather-Brown/dp/B06XC432VT/ref=lp_18637582011_1_1?srs=18637582011/']
   

    def parse(self, response):
        #rev=response.xpath(".//div[@class='a-section review']")
	rev=response.xpath(".//div[@class='a-section review aok-relative']")

        for lst in rev:
            name=lst.xpath(".//div[@class='a-profile-content']/span/text()").extract_first()
            #star=lst.xpath(".//i[@class='a-icon a-icon-star a-star-3 review-rating']/span[@class='a-icon-alt']/text()").extract_first()
	    star=lst.xpath(".//div[@class='a-row']/a[@class='a-link-normal']/i/span/text()").extract_first()
	    content=lst.xpath(".//div[@class='a-expander-content reviewText review-text-content a-expander-partial-collapse-content']/text()").extract_first()
	    
            data=OnePageScrapItem()
            data["name"]=name
            data["star"]=star
            data["content"]=content
            yield data
    
#df=pd.DataFrame(records,columns=['data','name','star','content']
#df.head()


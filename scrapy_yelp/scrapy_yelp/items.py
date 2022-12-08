# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class ScrapyYelpItem(scrapy.Item):
    business_name = Field()
    business_rating = Field()
    number_of_reviews = Field()
    business_yelp_url = Field()
    business_website = Field()

import scrapy

class InfoSpider(scrapy.Spider):
    name = 'yelp_spider'
    #allowed_domains = [' ']
    start_urls = ['https://www.yelp.ie/dublin']


    def parse(self, response):
        for data in response.css():
            business_name = data.css().get()
            business_rating = data.css().get()
            number_of_reviews = data.css().get()
            business_yelp_url = data.css().get()
            business_website = data.css().get()
            """
            list_of_first_five_reviews
            """


        yield {
            'business_name': business_name,
            'business_rating': business_rating,
            'number_of_reviews': number_of_reviews,
            'business_yelp_url': business_yelp_url,
            'business_website': business_website,
        }

        next_page = response.css().get()
        if next_page != None:
            yield response.follow(next_page, callback=self.parse)


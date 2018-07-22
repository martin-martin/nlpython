import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from yalescrape.items import YalescrapeItem


class YaleSpider(CrawlSpider):
    name = "yale"

    # since all writings are descendants of this URL, and the spider
    # crawls recursively, we can start off only with this one URL
    start_url = "https://president.yale.edu/speeches-writings/"

    # defining to omit links that are not interesting for this data
    # collection. we want only speeches and writings
    allowed_domain = "https://president.yale.edu/speeches-writings/"


    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse_items)

    def parse_items(self, response):
        # box for items
        items = []
        # fetching all the links recursively
        link_extractor = LinkExtractor(
            allow=[self.start_url],
            deny=[],
            tags='a',
            attrs='href',
            canonicalize=True
        )
        links = link_extractor.extract_links(response)
        # then go through them to further process
        for link in links:
            # check whether it's a link leading to some writing
            if self.allowed_domain in link.url:
                # we create an Item object and assign it the instance
                # variables we defined in the 'schema' over in items.py
                item = YalescrapeItem()
                item['url_from'] = response.url
                item['url_to'] = link.url
                items.append(item)
        return items

# helpful tutorial:
# https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/

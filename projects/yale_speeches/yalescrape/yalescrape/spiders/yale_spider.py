import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from scrapy.selector import Selector
from yalescrape.items import YalescrapeItem


class YaleSpider(CrawlSpider):
    name = "yale"

    # since all writings are descendants of this URL, and the spider
    # crawls recursively, we can start off only with this one URL
    start_urls = ["https://president.yale.edu/speeches-writings"]

    # defining to omit links that are not interesting for this data
    # collection. we want only speeches and writings
    # NOTE: adding the final "/" will only take subpages of that domain
    allowed_domains = ["president.yale.edu/speeches-writings/"]

    rules = [
        Rule(
            LinkExtractor(canonicalize=True, unique=True),
            callback='parse_items',
            follow=True,
        )
    ]

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse_items)

    def parse_items(self, response):
        link = response.xpath("//a").extract()
        print(link)
        # a box for our items
        items = []
        # link_extractor = LinkExtractor(canonicalize=True, unique=True)
        links = link_extractor.extract_links(response)
        # then go through them to further process
        for link in links:
            # check whether it's a link leading to some writing
            for ok_domain in self.allowed_domains:
                if ok_domain in link.url:
                    # we create an Item object and assign it the instance
                    # variables we defined in the 'schema' over in items.py
                    item = YalescrapeItem()
                    item['url_from'] = response.url
                    item['url_to'] = link.url
                    items.append(item)
        return items

# helpful tutorials:
# https://www.data-blogger.com/2016/08/18/scraping-a-website-with-python-scrapy/
# https://www.youtube.com/watch?v=P-_TpZ54Vcw

# to write output to file, call the spider using:
# scrapy crawl yale -o links.csv -t csv

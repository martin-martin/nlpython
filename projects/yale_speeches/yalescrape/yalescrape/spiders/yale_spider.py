import scrapy


class YaleSpider(scrapy.Spider):
    name = "yale"

    def start_requests(self):
        urls = [
            'https://president.yale.edu/speeches-writings/statements',
            'https://president.yale.edu/speeches-writings/notes-woodbridge-hall',
            'https://president.yale.edu/speeches-writings/speeches',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-1]
        filename = f'{page}.html'
        base_url = 'https://president.yale.edu'
        # improve to create a links.md document that has clickable links
        link_urls = response.css('td.views-field-title a::attr(href)').extract()
        link_titles = response.css('td.views-field-title a::text').extract()
        with open(filename, 'wb') as f:
            f.write(response.body)
        with open(f'{page}-links.html', 'wb') as f:
            for link in zip(link_titles, link_urls):
                f.write(f"{link[0]}\t{base_url}{link[1]}")
        self.log(f'Saved file {filename}')

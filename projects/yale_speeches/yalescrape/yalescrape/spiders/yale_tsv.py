import scrapy


class YaleSpider(scrapy.Spider):
    '''special spider to get link data as TSV files.'''
    name = "yale_tsv"

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
        link_urls = response.css('td.views-field-title a::attr(href)').extract()
        link_titles = response.css('td.views-field-title a::text').extract()
        # notes-woodbridge-hall has a different document structure
        # that will need to be addressed differently
        with open(f'{page}-links.tsv', 'wb') as f:
            for link in zip(link_titles, link_urls):
                # this one was tricky. f.write() only accepts
                # a bytes-like object, and f-strings don't support that
                # so I had to employ an older string formatting method
                # as well as explicit byte-encoding
                f.write(b"%b\t%b%b\n" % (link[0].encode('utf-8'),
                                        base_url.encode('utf-8'),
                                        link[1].encode('utf-8')))
        self.log(f'Saved file {filename}')

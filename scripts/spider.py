import scrapy
import json

class JobPostingSpider(scrapy.Spider):
    name = 'jobpostings'
    start_urls = [
        'https://www.ofir.dk/jobs/paedagog-undervisning-og-forskning/storkoebenhavn-jobs/',
        'https://www.ofir.dk/jobs/it-ingenioer-og-energi/storkoebenhavn-jobs/'
    ]

    def parse(self, response):
        data = response.css('#initial-state')

        output = json.loads(data.css('::text').get())    

        for next in output['searchPage']['results']:
            yield next

        
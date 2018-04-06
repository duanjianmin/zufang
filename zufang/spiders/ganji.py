import scrapy
from ..items import ZufangItem

class GanJiSpider(scrapy.Spider):
    name = "zufang"
    start_urls = ["http://bj.ganji.com/fang5/"]

    def parse(self, response):
        # print(response)
        zf = ZufangItem()
        price_list = response.xpath("//*[@class='f-list-item ershoufang-list']/dl/dd[5]/div[1]/span[1]/text()").extract()
        title_list = response.xpath("//*[@class='f-list-item ershoufang-list']/dl/dd[1]/a/text()").extract()
        for i, j in zip(price_list, title_list):
            zf['title'] = j
            zf['price'] = i
            yield zf
            # print(j, ":", i+"万"

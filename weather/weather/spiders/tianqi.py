# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class Tianqi(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['guangzhou.tianqi.com']
    start_urls = ['http://guangzhou.tianqi.com/']
    def parse(self,response):
        items = []

        # # V1.0
        # class_xpath = response.xpath('//div[@class="tqshow"]')
        # item = WeatherItem()
        # date = ''
        # for day in class_xpath.xpath('./h3//text()').extract():
        #     date += day
        # item['date'] = date
        # item['time'] = class_xpath.xpath('./ul/li[1]/text()').extract()[0]  # 日期
        # item['img'] = class_xpath.xpath('./ul/li[@class="tqpng_01"]/img/@src').extract()[0]
        # item['temperature'] = "".join(
        #     class_xpath.xpath('//*[@id="t_temp"]/font[1]/text()').extract()[0]) + "~" + "".join(
        #     class_xpath.xpath('//*[@id="t_temp"]/font[2]/text()').extract()[0])  # 温度
        # item['weather'] = class_xpath.xpath('./ul/li[4]/text()').extract()[0]  # 雨否
        # item['wind'] = class_xpath.xpath('./ul/li[5]/text()').extract()[0]  # 风向、风速
        # item['chuanyi'] = zhishu_xpath.xpath('./ul/li[1]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[1]/span/text()').extract()[0]  # 穿衣指数
        # item['chenlian'] = zhishu_xpath.xpath('./ul/li[2]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[2]/span/text()').extract()[0]  # 晨练指数
        # item['xiche'] = zhishu_xpath.xpath('./ul/li[3]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[3]/span/text()').extract()[0]  # 洗车指数
        # item['lvyou'] = zhishu_xpath.xpath('./ul/li[4]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[4]/span/text()').extract()[0]  # 旅游指数
        # item['ziwaixian'] = zhishu_xpath.xpath('./ul/li[5]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[5]/span/text()').extract()[0]  # 紫外线指数
        # item['liangshai'] = zhishu_xpath.xpath('./ul/li[6]/text()').extract()[0] + zhishu_xpath.xpath('./ul/li[6]/span/text()').extract()[0]  # 晾晒指数

        # 由于天气网更新，修改为V2.0
        # V2.0
        class_xpath = response.xpath('//div[@class="left"]/dl[@class="weather_info"]')
        item = WeatherItem()
        date = ''
        for day in class_xpath.xpath('./dd[1]/h2//text()').extract():
            date += day
        item['date'] = date
        item['time'] = class_xpath.xpath('./dd[2]/text()').extract()[0]  # 日期
        item['img'] = "https://www.tianqi.com" + class_xpath.xpath('./dd[3]/i/img/@src').extract()[0]
        item['temperature'] = "".join(class_xpath.xpath('./dd[3]/span/text()').extract()[0])  # 温度
        item['weather'] = class_xpath.xpath('./dd[3]/span/b/text()').extract()[0]  # 雨否
        item['wind'] = class_xpath.xpath('./dd[4]/b[2]/text()').extract()[0]  # 风向、风速

        items.append(item)
        return items

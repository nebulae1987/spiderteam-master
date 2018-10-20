#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/19 14:25
# @Author  : Jun
# @Site    : 
# @File    : boss_spider.py
# @Software: PyCharm
import scrapy,time
from lxml import etree

from spider_project.items import SpiderProjectItem


class BossSpider(scrapy.Spider):
    name = 'boss'

    def start_requests(self):

        querys = ['爬虫','python web','大数据','ai']
        #地区：101010100（北京）上海，广州，深圳
        scitys = ['101010100','101020100','101280100','101280600']
        pages = 1
        for query in querys:
            for scity in scitys:
                page = 0
                while page< pages:
                    url = 'https://www.zhipin.com/job_detail/?query='+query+'&scity='+scity+'&industry=&position=&page='+str(page)
                    yield scrapy.Request(url,callback=self.parse1)
                    page+=1
        #url = 'https://www.zhipin.com/job_detail/?query=ai&scity=101010100&industry=&position=&page=2'
        yield scrapy.Request(url, callback=self.parse1)
    #列表页解析：
    def parse1(self, response):
        print('列表解析开始-----------------------------------------')
        try:
            html_links = etree.HTML(response.text).xpath('//div[@class="info-primary"]/h3/a/@href')
            for url in html_links:
                url = 'https://www.zhipin.com/'+url
                print('url:',url)
                yield scrapy.Request(url, callback=self.parse)
        except Exception:
            pass
    #详情页采集：
    def parse(self, response):
        print('详情页开始解析========================================')
        html = etree.HTML(response.text)
        position,salary,company,experience,education,work_addr,company_size,job_info,job_requirements,main_business,department,com_net,status='无','无','无','无','无','无','无','无','无','无','无','无','无'
        try:
            position = html.xpath('//a[@ka="job_sug_2"]/text()')[0]
            print('position:',position)
        except Exception:
            pass
        try:
            salary = html.xpath('//span[@class="badge"]/text()')[0].strip()
        except Exception:
            pass
        try:
            company = html.xpath('//a[@ka="job-detail-company"]/text()')[0]
        except Exception:
            pass
        #经验：
        try:
            experience = html.xpath('//div[@class="job-primary detail-box"]/div/p/text()')[1]
        except Exception:
            pass
        # 学历：
        try:
            education = html.xpath('//div[@class="job-primary detail-box"]/div/p/text()')[2]
        except Exception:
            pass
        # com_net：
        try:
            com_net = html.xpath('//div[@class="job-primary detail-box"]/div/p/text()')[-1]
        except Exception:
            pass
        # 公司地点：
        try:
            work_addr = html.xpath('//div[@class="location-address"]/text()')[0]
        except Exception:
            pass
        # 公司规模：
        try:
            com = ''
            company_sizes = html.xpath('//div[@class ="info-company"]/p/text()')
            for company_size in company_sizes:
                com += company_size
            company_size = com
        except Exception:
            pass
        # 岗位描述：
        try:
            job = ''
            job_info = html.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')
            for i in job_info:
                job +=i
            job_info = job.strip()
        except Exception:
            pass
        # 主营业务：
        try:
            main_business = html.xpath('//a[@ka="job-detail-brandindustry"]/text()')[0]
        except Exception:
            pass

        create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print('create time:',create_time)

        #department 无,job_requirements:无，与job_info合并

        item = SpiderProjectItem()
        item['position'] = position
        item['salary'] = salary
        item['company'] = company
        item['experience'] = experience
        item['education'] = education
        item['work_addr'] = work_addr
        item['company_size'] = company_size
        item['job_info'] = job_info
        item['job_requirements'] = job_requirements
        item['main_business'] = main_business
        item['department'] = department
        item['create_time'] = create_time
        item['status'] = status
        item['com_net'] = com_net
        yield item

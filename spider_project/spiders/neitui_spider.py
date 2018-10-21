#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 20:47
# @Author  : Jun
# @Site    : 
# @File    : neitui_spider.py
# @Software: PyCharm
#http://www.neitui.me/?name=job&handle=lists&keyword=%E7%88%AC%E8%99%AB&city=%E5%8C%97%E4%BA%AC&page=2
import scrapy,time
from lxml import etree
from spider_project.items import SpiderProjectItem


class BossSpider(scrapy.Spider):
    name = 'neitui'
    #起始请求
    def start_requests(self):
        keywords = ['爬虫','python web','大数据','ai']
        keywords = ['大数据']
        #地区：101010100（北京）上海，广州，深圳
        citys = ['北京','上海','广州','深圳']
        citys = ['北京']
        #总采集页数：
        pages = 1
        # for city in citys:
        #     for keyword in keywords:
        #         page = 1
        #         while page<= pages:
        #                     #http://www.neitui.me/?name=job&handle=lists&keyword=%E7%88%AC%E8%99%AB&city=%E5%8C%97%E4%BA%AC&page=2
        #                    #http://www.neitui.me/?name=job&handle=lists&city=%E5%8C%97%E4%BA%AC&keyword=%E7%88%AC%E8%99%AB'
        #             url = 'http://www.neitui.me/?name=job&handle=lists&keyword='+keyword+'&city='+city+'&page='+str(page)
        #             yield scrapy.Request(url,callback=self.parse1)
        #             page+=1
        url = 'http://www.neitui.me/?name=job&handle=lists&city='+'北京'+'&keyword=大数据'
        yield scrapy.Request(url, callback=self.parse1)
    #列表页解析：
    def parse1(self, response):
        print('列表解析开始-----------------------------------------')
        print(response.text)
        try:
            # html_links = etree.HTML(response.text).xpath('//a[@class="media-left"]/@href')
            html_links = etree.HTML(response.text).xpath('//a[@class="font16 max300"]/@href')

            print(111111111,html_links)
            for url in html_links:
                if 'u' not in url:
                    url = 'http://www.neitui.me'+url
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
            position = html.xpath('//title/text()')[0].split('招聘')[0]
            print('position:',position)
        except Exception:
            pass
        try:
            salary = html.xpath('//span[@class="orange mr10"]/text()')[0]
            print('salary:', salary)
        except Exception:
            pass
        try:
            company = html.xpath('//a[@class="c333 font18"]/text()')[0].strip()
            print('company:', company)
        except Exception:
            pass
        #经验：
        try:
            experience = html.xpath('//span[@class="mr10"]/text()')[0]
            print('experience:', experience)
        except Exception:
            pass
        # 学历：
        try:
            education = html.xpath('//span[@class="mr10"]/text()')[1]
            print('education:', education)
        except Exception:
            pass
        # com_net：
        try:
            com_net = html.xpath('//a[@rel="nofollow"]/@href')[0]
            print('com_net:', com_net)
        except Exception:
            pass
        # 公司地点：
        try:
            work_addr = html.xpath('//div[@class="col-md-4 sider pl25"]/div/text()')[7][9:-8]
            if not work_addr:
                work_addr = html.xpath('//span[@class="mr10"]/text()')[2]
            print('work_addr:', work_addr)
        except Exception:
            pass
        # 公司规模：
        try:
            company_size = html.xpath('//span[@class="grey"]/text()')[2]
            print('company_size:', company_size)
        except Exception:
            pass
        # 岗位描述：
        try:
            job = ''
            job_info = html.xpath('//div[@class="mb20 jobdetailcon"]/text()')
            for i in job_info:
                job +=i
            job_info = job.strip()
            print('job_info:', job_info)
        except Exception:
            pass
        # 主营业务：
        try:
            main_business = html.xpath('//span[@class="grey"]/text()')[0]
            # if not main_business or main_business == '无':
            #     main_business = html.xpath('//span[@class="job_enterprisetype"]/text()')[1]
            print('main_business:', main_business)
        except Exception:
            pass
        create_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        print('create time:',create_time)

        #department 无
        #
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
        item['status'] = 'neitui'
        item['com_net'] = com_net
        yield item

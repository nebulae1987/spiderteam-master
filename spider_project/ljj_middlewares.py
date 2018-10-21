#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/20 17:21
# @Author  : Jun
# @Site    : 
# @File    : ljj_middlewares.py
# @Software: PyCharm

from .settings import USER_AGENT
import spider_project.proxy_ips as pc # 导入代理池
# from .items import myItem
import random
from scrapy import Request

#随机切换user_agent
class User_AgentDownloaderMiddlerware(object):
    def process_request(self, request, spider):
        request.headers.update({'User-Agent':random.choice(USER_AGENT)})
        return None
#随机换ip地址
class ProxyDownloaderMiddlerware(object):
    def __init__(self):
        self.db=pc.DB()
    def process_request(self, request, spider):
        #['http', '//182.88.212.11', '8123']
        ip_list =random.choice(self.db.get_all_ips())
        request.meta['proxy']=ip_list[2]+'://'+ip_list[0]+':'+ip_list[1]
        return None




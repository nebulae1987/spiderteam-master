# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class SpiderProjectPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.Connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = '666666',
            charset = 'utf8',
            db = 'spider'
        )

        self.cursor= self.conn.cursor()
    def process_item(self, item, spider):
        self.insert([item['position'],item['salary'],item['company'],item['experience'],item['education'],item['work_addr'],item['company_size'],item['job_info'],item['job_requirements'],item['main_business'],item['department'],item['create_time'],item['status'],item['com_net']])
        return item
    def insert(self,datas):
        sql = 'insert into t_recruit (position,salary,company,experience,education,work_addr,company_size,job_info,job_requirements,main_business,department,create_time,status,com_net) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql,datas)
        self.conn.commit()

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class U17Pipeline(object):
    def process_item(self, item, spider):
        return item


class U17MysqlPipeline(object):

    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get("MYSQL_HOST"),
            database = crawler.settings.get("MYSQL_DATABASE"),
            user = crawler.settings.get("MYSQL_USER"),
            password = crawler.settings.get("MYSQL_PASSWORD"),
            port = crawler.settings.get("MYSQL_PORT"),
        )

    def open_spider(self, spider):
        """
        爬虫打开的时候运行，只运行一次， 这两个方法名不能改，程序默认运行这两个方法
        :param spider:
        :return:
        """
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, charset='utf8', port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        """
        爬虫关闭的时候运行，关闭数据库连接
        :param spider:
        :return:
        """
        self.db.close()

    def process_item(self, item, spider):
        """
        存入数据库
        :param item:
        :param spider:
        :return:
        """
        sql = 'insert into yaoqi (comic_id , name , cover , category  ) values ("%s", "%s", "%s", "%s")' % (item['comic_id'], item['name'], item['cover'], item['category'])
        self.cursor.execute(sql)
        self.db.commit()
        return item


class U17ImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        url = request.url   # url是下面的方法传来的
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        yield Request(item['cover'])

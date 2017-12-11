# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import MySQLdb
import sys
import importlib
importlib.reload(sys)

class WeatherPipeline(object):
    def process_item(self, item, spider):
        # 打开数据库连接
        db = MySQLdb.connect(host="172.17.0.2", user="root", passwd="******", db="mysitedb",charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        max_price = 5
        # SQL 语句
        sql = 'insert into XYZblog_tianqiform values(1,"' + item['date'] + '","' + item['time'] + \
              '","' +item['img']+ '","' + item['temperature'] + '","' + item['weather'] + \
              '","' + item['wind'] + '") ON DUPLICATE KEY UPDATE chengshi="' + item['date'] + '",date="' + item['time'] + \
              '",img="' +item['img']+ '",temperature="' + item['temperature'] + '",cloud="' + item['weather'] + '",wind="' + item['wind'] + '"'
        cursor.execute(sql)
        db.commit()
#        try:
#            # 执行SQL语句
#            cursor.execute(sql)
#            # 提交到数据库执行
#            db.commit()
#        except:
#            # 发生错误时回滚
#            db.rollback()

        # 关闭数据库连接
        db.close()

        # base_dir = os.getcwd()
        # filename = base_dir + '/07150240-1.txt'
        # with open(filename,'w') as f:
        #     f.write(item['date'] + '\n')
        #     f.write(item['time'] + '\n')
        #     f.write(item['temperature'] + '\n')
        #     f.write(item['weather'] + '\n')
        #     f.write(item['wind'] + '\n')
        #     f.write(item['img'] + '\n\n')


            # f.write(item['chuanyi'] + '\n')
            # f.write(item['chenlian'] + '\n')
            # f.write(item['xiche'] + '\n')
            # f.write(item['lvyou'] + '\n')
            # f.write(item['ziwaixian'] + '\n')
            # f.write(item['liangshai'] + '\n')
#        return item


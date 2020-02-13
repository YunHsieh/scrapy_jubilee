# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class ScrapyJubileePipeline(object):
	def __init__(self):
		self.db = 'spider'
		self.crawl_table = 'crawl_click108'
		self.MYSQL_CONFIG = {
			'host' : 'db',
			'user' : 'root',
			'password' : '123456',
			'charset' : 'utf8mb4',
			'cursorclass' : pymysql.cursors.DictCursor
		}
		self.conn = pymysql.connect(**self.MYSQL_CONFIG)
		self.is_table(self.crawl_table)

	def process_item(self, item, spider):
		with self.conn.cursor() as cursor:
			all_columns = ','.join([('`%s`') % str(_element) for _element in item.keys()])
			all_values = ','.join([("'%s'") % str(_element) for _element in item.values()])
			sql = 'INSERT INTO `%s` (%s) VALUES (%s)' % (self.crawl_table, all_columns, all_values)
			cursor.execute(sql)
			self.conn.commit()

		return item


	def is_table(self,table_name):
		
		with self.conn.cursor() as cursor:
			stmt = "SHOW DATABASES LIKE '{db}';".format(db = self.db)
			cursor.execute(stmt)
			result = cursor.fetchone()
			if not result:
				sql = "CREATE DATABASE `{db}` CHARACTER SET utf8mb4 COLLATE UTF8MB4_UNICODE_CI;".format(db = self.db)
				cursor.execute(sql)
				self.conn.commit()

			# re-connection
			self.MYSQL_CONFIG['db'] = self.db
			self.conn = pymysql.connect(**self.MYSQL_CONFIG)
			
		with self.conn.cursor() as cursor:
			stmt = "SHOW TABLES LIKE '%s';" % (self.crawl_table)
			cursor.execute(stmt)
			result = cursor.fetchone()
			if not result:
				create_syntax = """
					CREATE TABLE `{table}` (
						`id` INT(11) NOT NULL AUTO_INCREMENT,
						`constellation_name` VARCHAR(3) NULL DEFAULT NULL,
						`overall_score` INT(11) NULL DEFAULT NULL,
						`overall_description` TEXT NULL DEFAULT NULL,
						`love_score` INT(11) NULL DEFAULT NULL,
						`love_description` TEXT NULL DEFAULT NULL,
						`work_score` INT(11) NULL DEFAULT NULL,
						`work_description` TEXT NULL DEFAULT NULL,
						`money_score` INT(11) NULL DEFAULT NULL,
						`money_description` TEXT NULL DEFAULT NULL,
						`date` DATE NULL DEFAULT NULL,
						INDEX `id` (`id`),
						INDEX `constellation_name` (`constellation_name`, `date`)
					)
					COLLATE='utf8mb4_unicode_ci'
					ENGINE=InnoDB
					AUTO_INCREMENT=13
					;
					""".format(
						table = self.crawl_table
						)
				cursor.execute(create_syntax)
				self.conn.commit()

	def close_spider(self, spider):
		self.conn.close()


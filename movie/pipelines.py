# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



class MoviePipeline(object):
  def process_item(self, item, spider):
    with open("my_meiju.txt",'a') as fp:
      fp.write(item["storyName"].encode("utf8") + "        ")
      fp.write(item["storyState"].encode("utf8") + "        ")
      if len(item["tvStation"]) == 0:
        fp.write("unknow        ")
      else:
        fp.write("%s         " %(item["tvStation"][0].encode("utf8")))
      fp.write("%s         \n" %(item["updateTime"].encode("utf8")))
    return item



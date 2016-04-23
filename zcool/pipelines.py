# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import os


class ZcoolPipeline(object):
    def process_item(self, item, spider):
        
        url=item['image_urls']
        pathname=url[-15:-4]
        floder=str(item['floder'])
        if os.path.exists(floder):
        else:
            os.mkdir(floder)
            path = '%s_%s.jpg' % (floder,pathname)
            data = urllib.urlopen(url).read()
            f = file(path,"wb")
            f.write(data)
            f.close()        

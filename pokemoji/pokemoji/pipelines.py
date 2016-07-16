# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy, json
from scrapy.pipelines.images import ImagesPipeline


class PokemojiPipeline(ImagesPipeline):
    # #Name download version
    # def image_path(self, url):
    #     print 'image key'
    #     image_guid = url.split('/')[-1]
    #     return 'full/%s.jpg' % (image_guid)

    # #Name thumbnail version
    # def thumb_path(self, url, thumb_id):
    #     print 'thumb key'
    #     image_guid = thumb_id + url.split('/')[-1]
    #     return 'thumbs/%s/%s.jpg' % (thumb_id, image_guid)

    def get_media_requests(self, item, info):
        for image in item['image_urls']:
            if image:
                yield scrapy.Request(image)

    # save the mapping of sha1 to image name
    def item_completed(self, results, item, info):
        for ok, x in results:
            if not ok:
                with open('images/image_map.txt', 'a+') as errors:
                    errors.write(str(x) + '\n')
            else:
                with open('images/image_map.txt', 'a+') as image_map:
                    image_map.write(x['url'].split('/')[-1].split('-')[-1] + ', ' + x['path'].split('/')[-1] + '\n')
        return item

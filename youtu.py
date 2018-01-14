# -*- coding: utf-8 -*-
# http://open.youtu.qq.com/#/develop/api-ocr-general
# github.com/se4

import os
import time
import random
import hmac
import hashlib
import binascii
import base64
import requests
import json


class Youtu(object):

    def __init__(self, app_id, secret_id, secret_key, qq=10000):
        self.app_id = app_id
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.qq = qq

    def cal_sig(self):
        timestamp = int(time.time())
        expired = str(timestamp + 2592000)
        rdm = str(random.randint(0, 999999999))
        plain_text = 'a={appid}&k={secret_id}&e={expired}&t={timestamp}&r={rdm}&u={qq}&f='
        plain_text = plain_text.format(appid=self.app_id,
                                       secret_id=self.secret_id,
                                       timestamp=timestamp,
                                       rdm=rdm, qq=self.qq,
                                       expired=expired)
        bin = hmac.new(self.secret_key.encode(), plain_text.encode(), hashlib.sha1).hexdigest()
        s = binascii.unhexlify(bin)
        s = s + plain_text.encode('ascii')
        signature = base64.b64encode(s).rstrip().decode()
        return signature

    def get_text(self, image_path):
        signature = self.cal_sig()
        headers = {'Host': 'api.youtu.qq.com', 'Content-Type': 'text/json', 'Authorization': signature}
        filepath = os.path.abspath(image_path)
        data = {'app_id': self.app_id, 'image': ''}
        data['image'] = base64.b64encode(open(filepath, 'rb').read()).rstrip().decode('utf-8')
        resp = requests.post('https://api.youtu.qq.com/youtu/ocrapi/generalocr',
                             data=json.dumps(data),
                             headers=headers)
        if 'items' in resp.text:
            return resp.content.decode('utf-8')
        else:
            return '0'


"""
接口申请：http://open.youtu.qq.com/
程序返回的是文本，若要作为字典使用，记得使用eval()方法
开发者QQ号可以使用默认值，变量名遵循官方的写法


time_start = time.time()
ocr = Youtu('xxx', 'xxx', 'xxx')
resp = ocr.get_text('3.png')
resp = eval(resp)
q = resp['items'][0]['itemstring']
a1, a2, a3 = resp['items'][1]['itemstring'], resp['items'][2]['itemstring'], resp['items'][3]['itemstring']
print(q, a1, a2, a3)
time_end = time.time()
print('totally cost： ', time_end-time_start)
"""
# -*- coding: utf-8 -*-
# github.com/se4

import requests
import base64
import json


class Hanvon(object):

    def __init__(self, appcode):
        self.appcode = appcode

    def get_pic_base64(self, pic_name, ext='jpg'):
        f = open('./{pic_name}.{ext}'.format(pic_name=pic_name, ext=ext), 'rb')
        ls_f = base64.b64encode(f.read())
        f.close()
        return ls_f

    def get_text(self, pic_name, ext='jpg'):
        body = {'uid': '118.12.0.12', 'lang': 'chns', 'image': '/9j/4AAQSkZJRgABAgAAAQABAAD'}
        headers = {'Authorization': 'APPCODE ' + self.appcode,
                   'Content-Type': 'application/octet-stream'}
        addr = 'http://text.aliapi.hanvon.com/rt/ws/v1/ocr/text/recg'
        body['image'] = self.get_pic_base64(pic_name=pic_name, ext=ext).decode()
        resp = requests.post(addr, headers=headers, data=json.dumps(body)).text
        if 'textResult' in resp:
            return eval(resp)['textResult']
        else:
            return ''


#appcode = ''
#ocr = Havon(appcode)
#print(ocr.get_text('3', 'png'))


"""
appcode在https://market.aliyun.com/products/57124001/cmapi011523.html获取
上文例子是提交同目录下zs.png进行识别

若在阿里云市场开启过IP验证，请释放下列注释，运行时间加0.2秒

import socket
import re

body['uid'] = get_ip()

def get_ip():
    names, aliases, ips = socket.gethostbyname_ex(socket.gethostname())
    for ip in ips:
        if not re.match('^192', ip):
            return ip

"""

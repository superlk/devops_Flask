#! /usr/bin/env python
# config:utf-8

import os 
import json
import requests

headers={'connten-type':'application/json'}
url="http://192.168.116.131:5000/api/"

# 获取主机数据
hostname=os.popen('hostname').readline()
lan_ip='192.168.1.1'
wan_ip='10.11.13.40'
cabinet_id=1
op='wwwwww'
phone='18600000'

# 主机数据拼成字典
data={'hostname':hostname,'lan_ip':lan_ip,'wan_ip':wan_ip,'cabinet_id':cabinet_id,'op':op,'phone':phone}

# post请求
r=requests.post(url,headers=headers,json=data)

# 返回json，并判断是否添加成功
data1=json.loads(r.text)
print data1
if data1['code']==0:
   print 'is ok'
else:
   print 'error'

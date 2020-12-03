import requests
import time
import re
import datetime
import json
import os

se = requests.session()
# api地址
post_url = "https://report.amap.com/ajax/roadRank.do?roadType=0&timeType=0&cityCode=440300"

# 爬取数据的日期
ti = datetime.datetime.now().strftime('%Y-%m-%d')

# 存储的文件名
filename = '['+ti+']''深圳道路拥堵信息'+'.json'

# 接受reponse,内容为json格式的字符串
reponsetxt = se.get(post_url).text.replace("'",'"').replace('/ ','/')

# json字符串转python对象
jsondata = json.loads(reponsetxt)

# 删除无用字段
del jsondata['updateTime']

for data in jsondata['tableData']:
    # 删除无用字段

    del data['id']
    del data['length']

    # 定义中文key值，并按网页中表格顺序进行排序
    for coords in data['coords']:
        coords['维度'] = coords.pop('lat')
        coords['经度'] = coords.pop('lon')
    data['排名'] = data.pop('number')
    data['道路名称'] = data.pop('name')
    data['方向'] = data.pop('dir')
    data['拥堵延时指数'] = data.pop('index')
    data['速度'] = data.pop('speed')
    data['旅行时间'] = data.pop('travelTime')
    data['延迟时间'] = data.pop('delayTime')
    data['坐标'] = data.pop('coords')

# 存储数据
with open(filename,"w", encoding="utf-8") as f:
    f.write(json.dumps(jsondata,ensure_ascii=False))
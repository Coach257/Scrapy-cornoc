from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import datetime
import os

# 加载配置
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='chromedriver',
    options=chrome_options)

# 网站地址
url='https://report.amap.com/detail.do?city=440300'
driver.get(url)

# 等待资源加载完毕
time.sleep(3)

# 爬取数据的日期
ti = datetime.datetime.now().strftime('%Y-%m-%d')

# 存储的文件名
filename = '['+ti+']''深圳区域拥堵信息'+'.json'

# 获取数据
tabledata = driver.find_elements_by_xpath("//table[@id = 'first_table']/tbody/tr")

jsondata = dict()
jsondata['tableData'] = []
for tr in tabledata:
    data = tr.text.split(" ")
    # 数据处理
    content = {
        "排名": data[0],
        "区域": data[1],
        "拥堵指数": data[2],
        "旅行速度": data[3]
    }
    jsondata['tableData'].append(content)

# 存储数据
with open(filename,"w", encoding="utf-8") as f:
    f.write(json.dumps(jsondata,ensure_ascii=False))

driver.close()

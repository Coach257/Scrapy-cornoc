# Scrapy-cornoc
>18373044 施哲纶

-----
介绍：
本项目实现了对静态网站以及动态网站的数据爬取，以及定时爬取，爬取的数据保存为json格式

|——amap :动态网站爬取项目\
|——cornoc_scrapy :静态网站爬取项目



## cornoc_scrapy
> 爬取网址：http://data.carnoc.com/corp/airport/csx__airportflight.html \
> 每24小时爬取一次
### 使用说明
定时爬取：
```
python main.py
```
单次爬取：
```
python MySpider.py
```
### 目录结构
|-scrapy.cfg: 项目的配置文件\
|-data.json: 爬取的数据文件\
|-requirements.txt\
|-cornoc_scrapy: 该项目的python模块\
| |-items.py: 项目中的item文件\
| |-main.py: 定时爬取执行文件\
| |-middlewares.py: 中间件\
| |-pipelines.py: 项目中的pipelines文件\
| |-settings.py: 项目的设置文件\
| |-spiders: 放置spider代码的目录\
| |-MySpider: 爬虫主程序

### 数据介绍
爬取网站内容如下图所示：
![](/img/cornoc.png)
json内容如下：
```json
{
    "type": "进港", 
    "img": "http://cdn.feeyo.com/fimg/ticket/img/air/3u.gif",
    "href": "http://data.carnoc.com/corp/airline/3u.html",
    "number": "3U4370",
    "city": "三亚", 
    "terminal": "---", 
    "expected": "01:00", 
    "actual": "-----", 
    "state": "起飞 "
}
```
- type: 进港/出港
- img: 航空公司logo图
- href: 航空公司网站地址
- number: 航班号
- city: 始发地
- terminal: 接机楼,如果为---表示接机楼未确认
- expected: 预计抵达时间
- actual: 实际抵达时间,如果为-----表示未到达
- state: 航班状态
### 爬虫结果截图
![](/img/json.png)

## amap
>爬取网址：https://report.amap.com/detail.do?city=440300\
>每24小时爬取一次
### 项目说明
动态网站的数据获取分为两种：
1. 网站在加载静态页面后请求后端数据，前端脚本进行处理，将数据写入html。此类动态网站爬取方式是等待页面以及数据加载完毕，并且html数据更新后，再进行爬取
2. 网站同样在加载静态页面后请求后端数据，前端脚本进行处理，但是数据不写入html，而是存储在js相应的data中。此类网站爬取可以通过分析js文件，或者直接截获请求发来的数据文件

该网站以上两种动态数据都有，本项目也对两种动态数据都进行了爬取
### 使用说明
定时爬取深圳道路拥堵信息：
```
python rrmain.py
```
单次爬取深圳道路拥堵信息：
```
python RoadRank.py
```
定时爬取深圳区域拥堵信息：
```
python drmain.py
```
单次爬取深圳区域拥堵信息：
```
python DistrictRank.py
```
### 目录结构
|-[time]深圳道路拥堵信息.json: 道路信息爬取数据\
|-[time]深圳区域拥堵信息.json: 区域信息爬取数据\
|-chromedriver.exe: 浏览器驱动\
|-DistrictRank.py: 区域信息爬取程序\
|-drmain.py: 区域信息定时爬取程序\
|-RoadRank.py: 道路信息爬取程序\
|-rrmain.py: 道路信息定时爬取程序\
|-requirements.txt

### 数据介绍
#### 区域拥堵数据
网站爬取内容如下，该数据为动态加载在html中的数据：
![](/img/区域拥堵排名.png)
json内容如下:
```json
{
    "tableData": [
        {
            "排名": "1", 
            "区域": "南山区", 
            "拥堵指数": "1.57", 
            "旅行速度": "30.55"
            }
            ...
            ]
            }
```
数据含义即中文字面含义
#### 道路拥堵数据
网站爬取内容如下，该数据为动态加载在js中的数据：
![](/img/道路拥堵排名.png)
json内容如下:
```json
{
    "tableData": [
        {
            "排名": 1, 
            "道路名称": "清水路", 
            "方向": "由西向东", 
            "拥堵延时指数": 3.6, 
            "速度": 9.7, 
            "旅行时间": 17.9, 
            "延迟时间": 12.9, 
            "坐标": [
                {
                    "维度": 22.7599382400513, 
                    "经度": 114.237513542175
                    }, 
                    ... 
                    ]
                    }
                    ...
                    ]
}
```
坐标为右侧地图数据，存储多个坐标表示道路节点，地图上连线即可表示道路
### 爬虫结果截图
#### 区域结果截图
![](/img/amap1.png)
#### 道路结果截图
![](/img/amap2.png)

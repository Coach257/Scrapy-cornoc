import os
import time

def run():
    while True:
        #爬虫运行指令
        os.system("python RoadRank.py")
        #休眠1天
        time.sleep(86400)

if __name__ == '__main__':
    run()
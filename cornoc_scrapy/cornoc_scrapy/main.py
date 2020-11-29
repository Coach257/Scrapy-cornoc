import os
import time

def run():
    while True:
        print("running\n")
        os.system("scrapy crawl MySpider")
        time.sleep(60)

if __name__ == '__main__':
    run()
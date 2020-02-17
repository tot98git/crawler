from crawler import Crawler
import logging
import sys

logging.basicConfig(filename='crawler/app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    crawler = Crawler()
    crawler.main()


if __name__=="__main__": 
    main() 
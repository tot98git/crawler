import schedule
from crawler import Crawler
import logging

logging.basicConfig(filename='app.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    crawler = Crawler()
    crawler.main()

if __name__=="__main__": 
    main() 
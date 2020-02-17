import feedparser
import pandas as pd 
import numpy 
from item import Item
import logging


class Crawler:
    def __init__(self, headlines = []):
        self.headlines = []
    
    @staticmethod
    def readFile():
        try: 
            df = pd.read_csv('data.csv', index_col=False)
            return df
        except:
            return None

    @staticmethod
    def ifExists(originalData, value):
        exists = int(value['id']) in originalData
        return exists
    
    def writeToFile(self):
        logging.info('Comparing existing data')
        
        curr_data = self.readFile()
        curr_data_empty = curr_data is None

        if not curr_data_empty:
            curr_data_id = list(curr_data.id)
            filtered_data = list(item for item in self.headlines if not self.ifExists(curr_data_id, item))
        else:
            filtered_data = self.headlines

        if (len(filtered_data) > 0):
            df = pd.DataFrame(filtered_data)
            logging.info('Writing new data %s', len(filtered_data))
            df.to_csv('data.csv', header = curr_data_empty,  mode='a', index=False)
            logging.info('Success!')
        else:
            logging.info('Nothing to write!')

    
    def readUrl(self, url):
        content = feedparser.parse(url)
        
        for entry in content.entries:
            item = Item(entry)
            self.headlines.append(item.__dict__)

    def main(self):
        logging.info('Started crawler: \n ')
        GENERAL_FEED = "https://insajderi.com/feed/"
        SPORT_FEED = "https://insajderi.com/sport/feed/"
        WORLD_FEED = "https://insajderi.com/bota/feed/"
        CULT_FEED = "https://insajderi.com/cultbiz-review/feed/"
        BIZ_FEED = "https://insajderi.com/biznes/"
        LIFE_FEED = "https://insajderi.com/life/feed/"
        sources = [GENERAL_FEED, SPORT_FEED, WORLD_FEED, CULT_FEED, BIZ_FEED, LIFE_FEED]

        for index, source in enumerate(sources):
            logging.info('Started fetching feed for %s', index + 1)
            self.readUrl(source)
            logging.info('Finished fetching feed for %s \n ---------', index + 1)

        self.writeToFile()
         

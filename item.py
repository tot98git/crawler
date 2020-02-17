import re

class Item:
    def __init__(self, entry):
        self.titulli = self.cleanData(entry.title)
        self.id = self.extractId(entry.guid)
        self.kategoria = entry.category

    @staticmethod
    def cleanData(line):
        return re.sub('(\(video\))|\(foto\)', '', line, flags = re.IGNORECASE)
    
    @staticmethod
    def extractId(line):
        t = re.search("p=([^&]*)", line)

        if t:
            return t.group(1)
    
__author__ = 'poke19962008'

import re

def extract(query):
    query = query.split(" ")
    StrippedQuery = []
    StopWords = open("StopWords.txt", "r").read().split("\n")
        
    for word in query:
        word = word.lower()
        word = re.sub(r"([^\w\s])|(/[^\x00-\x7F]+\ *(?:[^\x00-\x7F]| )*/g)", "", word)  # Remove all the punctuations and non-ASCII characters |([^\u0000-\u007F]+)
                    
        if word not in StopWords:
            StrippedQuery.append(word)
    return StrippedQuery

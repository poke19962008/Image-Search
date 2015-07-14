__author__ = 'poke19962008'

# -*- encoding:utf-8 -*-
import re, keywordExtractor

def removeUnicodes(line):
    reExp = "[^\u0000-\u007F]+"

    re.sub(reExp, "", line)
    return line

def removeStopWords(line):
    line = keywordExtractor.extract(line)
    line = " ".join(line)

    return line

if __name__ == "__main__":
    print("on prog.")
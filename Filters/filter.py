__author__ = 'poke19962008'

# -*- encoding:utf-8 -*-
import re, keywordExtractor, json

def extractKeyWords(line):
    line = keywordExtractor.extract(line)
    line = " ".join(line)

    return line

def isURL(line):
    if re.search(r"((https|http):(//)+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", line):
        return True
    else:
        return False

def startFiltering(dumpName):
    skip = False
    folderCheck = False
    folderURLCheck = False
    folder = ""

    file_ = open("FilteredDump.json", "wb")

    with open(dumpName, "r") as f:
        for line in f:
            if len(line.split()) is 0:
                folderURLCheck = True
                folderCheck = True
                folder = ""
                continue

            if folderURLCheck:
                if isURL(line):
                    folderURL = line.replace("\n", "")
                    folderURLCheck = False
                    # print("Folder URL=", folderURL)
                    continue

            if folderCheck:
                folderCheck = False
                folder = extractKeyWords(line).replace("\n", "").split()
                continue
            else:
                if skip:
                    skip = False
                    continue

                if isURL(line):
                    data['URL'] = line.replace("\n", "")
                    json.dump(data, file_)
                    file_.write("\n")
                    # print(data)
                else:

                    name = extractKeyWords(line)
                    if not len(name.split()):
                        skip = True
                        continue

                    data = {}
                    data['folder'] = folder
                    data['folderURL'] = folderURL
                    data['name'] = name.replace("\n", "").split()

if __name__ == "__main__":
    print("Filtering started...")
    startFiltering("dummy.txt")
    print("Filtering completed...")
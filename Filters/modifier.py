__author__ = 'poke19962008'

import json

def modifyRank():
    viewRank = 1

    file_ = open("filteredDump1.json", "a")

    with open("FilteredDump.json", "r") as f:
        for line in f.readlines():
            line  = json.loads(line)
            line['viewRank'] = viewRank
            json.dump(line, file_)
            file_.write("\n")
            viewRank = viewRank + 1

def modifyID():
    ID = 1
    file_ = open("mod.json", "a")

    with open('foo.json', 'r') as f:
        for line in f.readlines():
            line = json.loads(line)
            line['docID'] = ID
            json.dump(line, file_)
            file_.write('\n')
            ID = ID + 1

def main():
    print("Started")
    modifyID()
    print("Finish")


if __name__ == '__main__':
 main()
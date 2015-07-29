__author__ = 'poke19962008'

import json, mysql.connector

db = mysql.connector.connect(user='root', host='localhost', database = 'SRM_ISE', port=8888)
cursor = db.cursor()

command = "CREATE TABLE `Main Index` (`ID` VARCHAR(200) PRIMARY KEY, `Detail` TEXT)"
cursor.execute(command)

data = {}
with open('db.json', 'r') as f:
    for line in f.readlines():
        tuple = json.loads(line)

        for word in tuple['name']:
            if word not in data:
                data[word] = []
            data[word].append(str({'ID': tuple['docID'], 'Pos.': tuple['name'].index(word)}))

            print(tuple['docID'], "Done!")

command = "INSERT INTO `Main Index` (`ID`, `Detail`) VALUES (%(ID)s, %(Detail)s)"

for key, value in data.iteritems():
    cursor.execute(command, {'ID': key, 'Detail': str(value)})
    db.commit()
db.close()


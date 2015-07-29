__author__ = 'poke19962008'

import mysql.connector, json

db = mysql.connector.Connect(host='localhost', user='root', database='SRM_ISE', port=8888)
cursor = db.cursor()

command = "CREATE TABLE `DOC Index` " \
          "(`docID` INT(200) PRIMARY KEY, `View Rank` VARCHAR(200), `Name` VARCHAR(2000), `Folder` VARCHAR(2000), `URL` VARCHAR(500), `Folder URL` VARCHAR(500))"
cursor.execute(command)

with open('db.json') as file_:
    for line in file_.readlines():
        data = json.loads(line)

        data['name'] = str(data['name'])
        data['folder'] = str(data['name'])

        command  = "INSERT INTO `DOC Index` (`docID`, `View Rank`, `Name`, `Folder`, `URL`, `Folder URL`) " \
                   "VALUES (%(docID)s, %(viewRank)s, %(name)s, %(folder)s, %(URL)s, %(folderURL)s)"

        cursor.execute(command, data)
        db.commit()

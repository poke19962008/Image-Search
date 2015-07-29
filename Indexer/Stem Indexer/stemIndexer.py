__author__ = 'poke19962008'

import PorterStemmer as PS
import mysql.connector

stemmer = PS.PorterStemmer()

db =  mysql.connector.connect(user="root", host="localhost", database="SRM_ISE", port=8888)
cursor = db.cursor()

cursor.execute("CREATE TABLE `Stem Index` (`Stem ID` VARCHAR(200) PRIMARY KEY, `ID` TEXT)")

print("Fetching data from Main Index")
cursor.execute("SELECT `ID` FROM `Main Index`")
print("Success...")

for ele in cursor.fetchall():
    stem_word = stemmer.stem(ele[0], 0, len(ele[0])-1)
    cursor.execute("SELECT `Stem ID` FROM `Stem Index` WHERE `Stem ID` = %(SID)s", {'SID': stem_word})

    if len(cursor.fetchall()) == 0:
        cursor.execute("INSERT INTO `Stem Index` VALUES (%(SID)s, %(ID)s)", {'SID': stem_word,'ID': ele[0]})
        print("SID=" + stem_word + " ID=" + ele[0] + " INSERTED")
    else:
        cursor.execute("SELECT `ID` FROM `Stem Index` WHERE `Stem ID` = %(SID)s", {'SID': stem_word})
        data = cursor.fetchall()[0][0] + ", " + ele[0]
        cursor.execute("UPDATE `Stem Index` SET `ID` = %(ID)s WHERE `Stem ID` =  %(SID)s", {'ID': data,'SID': stem_word})
        print("SID=" + stem_word + " ID=" + ele[0] + "UPDATED")
    db.commit()
db.close()
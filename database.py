
import sqlite3
from time_modules import getDate

def createConnection():
    connection = sqlite3.connect('dataStore.db')
    return connection

def getDatabaseData():
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM QueryAndResults")
    return cursor.fetchall()

def getResultFromDatabase(question):
    data = getDatabaseData()
    for row in data:
        if row[0].lower() in question.lower():
            return row[1]
    return ""

def insertIntoQueryAndResults(query, result):
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO QueryAndResult values("'+query+'", "'+result+'")')
    connection.commit()


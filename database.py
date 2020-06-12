
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

def insertIntoInfo(name, value):
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute('INSERT into Info values("'+name+'", "'+value+'")')
    connection.commit()

def getInfoFromInfoTable(name):
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT value FROM Info where name = "'+name+'"')
    return cursor.fetchone()

def updateInfoTable(name, value):
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute('UPDATE Info set value = "'+value+'" where name = "'+name+'"')
    connection.commit()

def getSpeakingStatus():
    connection = createConnection()
    cursor = connection.cursor()
    cursor.execute('SELECT value FROM Info where name = "speech"')
    status = cursor.fetchone()[0]
    if status == 'on':
        return True
    return False


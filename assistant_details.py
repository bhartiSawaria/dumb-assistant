
from database import getInfoFromInfoTable, updateInfoTable

def getName():
    return getInfoFromInfoTable('assistant_name')[0]

def changeName(newName):
    updateInfoTable('assistant_name', newName)


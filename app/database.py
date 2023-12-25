import pyodbc
from hashlib import sha256
key = open("ServernameHere.txt",'r')
contents = key.read()
print(contents)

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      f'Server={contents};'
                      'Database=QLPHONGKHAM;'
                      'Trusted_Connection=yes;', autocommit=True) # autocommit for fast transaction

cursor = conn.cursor()

def hashPass(password: str) -> str:
    return sha256(password.encode()).hexdigest()
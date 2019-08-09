from flask import Flask
import mysql.connector as sql

app = Flask(__name__)

@app.route("/")
def hello():
    c = sql.connect(host='172.16.0.2',user='rahul',password='rahul.281294',database='testDB')
    a = c.cursor()
    a.execute("SELECT * FROM Persons")
    b = a.fetchone()
    f = ''.join(map(str,b))
    return f

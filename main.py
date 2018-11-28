from flask import Flask, render_template, redirect, request
import datetime
import pandas as pd
import numpy as np
import sqlite3
import pprint

app = Flask(__name__)

connection = sqlite3.connect('prototype.db')

cursor = connection.cursor()

session = dict()
session['user']=None

#-----------------------------------------------------------------------

#Login Mahasiswa
@app.route('/')
def login():
	return render_template("home.html")

@app.route('/handleLogin/')
def handleLogin():
	username =  request.args.get('username')
	password = request.args.get('password')
	
	
	cursor.execute("""SELECT * FROM Mahasiswa WHERE Username='{}' AND Password='{}'""".format(username,password))
	result=cursor.fetchall()
	
	if(len(result)==0):
		return render_template("home.html")
	else:		
		cursor.execute("""SELECT MataKuliah.Kode, MataKuliah.Nama FROM MataKuliah Inner Join (SELECT * FROM Mahasiswa INNER JOIN Mengambil ON Mahasiswa.Username = Mengambil.Username_Mahasiswa WHERE Mahasiswa.Username='{}') as Temp on MataKuliah.Kode=Temp.Kode_MataKuliah;""".format(username))
		result=cursor.fetchall()
		
		session['user']=username
		return render_template("dashboard.html",data=result)

#Login Dosen
@app.route('/dosen/')
def loginDosen():
	return render_template("dosen_login.html")

@app.route('/handleLoginDosen/')
def handleLoginDosen():
	username =  request.args.get('username')
	password = request.args.get('password')
	
	
	cursor.execute("""SELECT * FROM Dosen WHERE Username='{}' AND Password='{}'""".format(username,password))
	result=cursor.fetchall()
	
	if(len(result)==0):
		return render_template("home.html")
	else:		
		cursor.execute("""SELECT MataKuliah.Kode, MataKuliah.Nama FROM MataKuliah Inner Join (SELECT * FROM Dosen INNER JOIN Mengajar ON Dosen.Username = Mengajar.Username_Dosen WHERE Dosen.Username='{}') as Temp on MataKuliah.Kode=Temp.Kode_MataKuliah;""".format(username))
		result=cursor.fetchall()
		
		session['user']=username
		return render_template("dashboard.html",data=result)

#Forum
@app.route('/forum/')
def forum():
	Kode_MataKuliah =  request.args.get('Kode_MataKuliah')
	
	cursor.execute("""SELECT ThreadPertanyaan.Kode_MataKuliah,ThreadPertanyaan.ID,ThreadPertanyaan.Pertanyaan,ThreadPertanyaan.Tag FROM ThreadPertanyaan INNER JOIN MataKuliah ON ThreadPertanyaan.Kode_MataKuliah=MataKuliah.Kode WHERE ThreadPertanyaan.Kode_MataKuliah='{}'""".format(Kode_MataKuliah))
	result=cursor.fetchall()
	
	cursor.execute("""SELECT * From MataKuliah WHERE Kode='{}'""".format(Kode_MataKuliah))
	result_2=cursor.fetchall()
	
	return render_template("forum.html", data=result, matakuliah=result_2[0])

#Thread
@app.route('/thread/')
def thread():
	ID_ThreadPertanyaan =  request.args.get('ID_ThreadPertanyaan')
	
	cursor.execute("""SELECT * FROM Jawaban WHERE ID_ThreadPertanyaan='{}'""".format(ID_ThreadPertanyaan))
	result=cursor.fetchall()
	
	cursor.execute("""SELECT Pertanyaan FROM ThreadPertanyaan WHERE ID='{}'""".format(ID_ThreadPertanyaan))
	result_2=cursor.fetchall()
	
	return render_template("pertanyaan.html", data=result, pertanyaan=result_2[0][0])

#-----------------------------------------------------------------------

if __name__ == "__main__":
    app.run()


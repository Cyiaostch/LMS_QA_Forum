#import useful modules
import sqlite3
import os.path

if os.path.exists("prototype.db"):
	os.remove("prototype.db")

#open Connection
connection = sqlite3.connect('prototype.db')
cursor=connection.cursor()

#create Table Mahasiswa
cursor.execute('''CREATE TABLE Mahasiswa (
  Username varchar(100) NOT NULL,
  Password varchar(100) NOT NULL,
  Nama varchar(100) NOT NULL,
  NIM varchar(100) NOT NULL,
  PRIMARY KEY (Username)
);''')

cursor.execute('''INSERT INTO Mahasiswa VALUES ("deryan","deryan","Deryan","18216034")''')
cursor.execute('''INSERT INTO Mahasiswa VALUES ("jemi","jemi","Jemi","18216051")''')
cursor.execute('''INSERT INTO Mahasiswa VALUES ("athur","athur","Athur","18216004")''')
connection.commit()

#create Table Dosen
cursor.execute('''CREATE TABLE Dosen (
  Username varchar(100) NOT NULL,
  Password varchar(100) NOT NULL,
  Nama varchar(100) NOT NULL,
  NIP varchar(100) NOT NULL,
  PRIMARY KEY (Username)
);''')

cursor.execute('''INSERT INTO Dosen VALUES ("komang","komang","Komang","313133")''')
cursor.execute('''INSERT INTO Dosen VALUES ("somad","somad","Somad","212122")''')
cursor.execute('''INSERT INTO Dosen VALUES ("erte","erte","Erte","414144")''')
connection.commit()

#create Table MataKuliah
cursor.execute('''CREATE TABLE MataKuliah (
  Kode varchar(100) NOT NULL,
  Nama varchar(100) NOT NULL,
  PRIMARY KEY (Kode)
);''')

cursor.execute('''INSERT INTO MataKuliah VALUES ("TPB001","Kalkulus")''')
cursor.execute('''INSERT INTO MataKuliah VALUES ("TPB002","Fisika")''')
cursor.execute('''INSERT INTO MataKuliah VALUES ("TPB003","Kimia")''')
connection.commit()

#create Table ThreadPertanyaan
cursor.execute('''CREATE TABLE ThreadPertanyaan (
  Kode_MataKuliah varchar(100) NOT NULL,
  ID varchar(100) NOT NULL,
  Pertanyaan varchar(1000) NOT NULL,
  Tag varchar(1000) NOT NULL,
  PRIMARY KEY (ID)
);''')

cursor.execute('''INSERT INTO ThreadPertanyaan VALUES ("TPB001","{}","Berapakah nilai 1 + 1?","Materi")'''.format(hash("Berapakah nilai 1 + 1?")))
cursor.execute('''INSERT INTO ThreadPertanyaan VALUES ("TPB002","{}","Apakah batu bisa terbang?","Materi")'''.format(hash("Apakah batu bisa terbang?")))
cursor.execute('''INSERT INTO ThreadPertanyaan VALUES ("TPB003","{}","Mengapa fanta warnanya merah?","Materi")'''.format(hash("Mengapa fanta warnanya merah?")))
connection.commit()

#create Table Jawaban
cursor.execute('''CREATE TABLE Jawaban (
  ID_ThreadPertanyaan varchar(100) NOT NULL,
  ID varchar(100) NOT NULL,
  Jawaban varchar(1000) NOT NULL,
  Approved varchar(100) NOT NULL,
  PRIMARY KEY (ID)
);''')

cursor.execute('''INSERT INTO Jawaban VALUES ("{}","{}","Saya rasa jawabannya adalah 3","0")'''.format(hash("Berapakah nilai 1 + 1?"),hash("Saya rasa jawabannya adalah 3")))
cursor.execute('''INSERT INTO Jawaban VALUES ("{}","{}","Saya rasa batu bisa terbang. Tapi tidak tahu juga ya, kenapa ga tanya aja ke batunya?","0")'''.format(hash("Apakah batu bisa terbang?"),hash("Saya rasa batu bisa terbang. Tapi tidak tahu juga ya, kenapa ga tanya aja ke batunya?")))
cursor.execute('''INSERT INTO Jawaban VALUES ("{}","{}","Karena fanta diberi zat pewarna merah","0")'''.format(hash("Mengapa fanta warnanya merah?"),hash("Karena fanta diberi zat pewarna merah")))
connection.commit()

#create Table Mengambil
cursor.execute('''CREATE TABLE Mengambil (
  Username_Mahasiswa varchar(100) NOT NULL,
  Kode_MataKuliah varchar(100) NOT NULL,
  PRIMARY KEY (Username_Mahasiswa, Kode_MataKuliah)
);''')

cursor.execute('''INSERT INTO Mengambil VALUES ("deryan","TPB001")''')
cursor.execute('''INSERT INTO Mengambil VALUES ("jemi","TPB002")''')
cursor.execute('''INSERT INTO Mengambil VALUES ("athur","TPB003")''')
connection.commit()

#create Table Mengajar
cursor.execute('''CREATE TABLE Mengajar (
  Username_Dosen varchar(100) NOT NULL,
  Kode_MataKuliah varchar(100) NOT NULL,
  PRIMARY KEY (Username_Dosen, Kode_MataKuliah)
);''')

cursor.execute('''INSERT INTO Mengajar VALUES ("komang","TPB001")''')
cursor.execute('''INSERT INTO Mengajar VALUES ("somad","TPB002")''')
cursor.execute('''INSERT INTO Mengajar VALUES ("erte","TPB003")''')
connection.commit()

#close connection
connection.close()

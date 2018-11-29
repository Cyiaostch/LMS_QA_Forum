#import module
import sqlite3
import pprint

#open Connection
connection = sqlite3.connect('prototype.db')
cursor=connection.cursor()

#Query
cursor.execute("""Select * From Mahasiswa""")
data=cursor.fetchall()
print("Table Mahasiswa")
pprint.pprint(data)
print()

cursor.execute("""Select * From Dosen""")
data=cursor.fetchall()
print("Table Dosen")
pprint.pprint(data)
print()

cursor.execute("""Select * From MataKuliah""")
data=cursor.fetchall()
print("Table MataKuliah")
pprint.pprint(data)
print()

cursor.execute("""Select * From ThreadPertanyaan""")
data=cursor.fetchall()
print("Table ThreadPertanyaan")
pprint.pprint(data)
print()

cursor.execute("""Select * From Jawaban""")
data=cursor.fetchall()
print("Table Jawaban")
pprint.pprint(data)
print()

cursor.execute("""Select * From Mengambil""")
data=cursor.fetchall()
print("Table Mengambil")
pprint.pprint(data)
print()

cursor.execute("""Select * From Mengajar""")
data=cursor.fetchall()
print("Table Mengajar")
pprint.pprint(data)
print()

cursor.execute("""SELECT ThreadPertanyaan.Kode_MataKuliah,ThreadPertanyaan.ID,ThreadPertanyaan.Pertanyaan,ThreadPertanyaan.Tag FROM ThreadPertanyaan INNER JOIN MataKuliah ON ThreadPertanyaan.Kode_MataKuliah=MataKuliah.Kode WHERE ThreadPertanyaan.Kode_MataKuliah='{}'""".format("TPB001"))
data=cursor.fetchall()
print("Test")
pprint.pprint(data[0])
print()

cursor.execute("""SELECT Pertanyaan,ID FROM ThreadPertanyaan WHERE ID='{}'""".format("P001"))
data=cursor.fetchall()
print("Test")
pprint.pprint(data[0])
print()

#commit command
connection.commit()


#close connection
connection.close()

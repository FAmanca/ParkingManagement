import mysql.connector
import time

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="parking"
)


def create_item(owner, jenis, merk, plat, biaya):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO park (owner, jenis, merk, plat, biaya) VALUES (%s, %s, %s, %s, %s)",
        (owner, jenis, merk, plat, biaya)
    )
    db.commit()
    if cursor.rowcount > 0:
        print("DATA BERHASIL DITAMBAHKAN")
        time.sleep(1)
    else:
        print("DATA GAGAL DITAMBAHKAN")
        time.sleep(1)

def read_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM park")
    return cursor.fetchall()

def delete_item(plat):
    cursor = db.cursor()
    query = "DELETE FROM park WHERE plat = %s"
    cursor.execute(query, (plat,))
    db.commit()
    if cursor.rowcount > 0:
        print("DATA BERHASIL DIHAPUS")
        time.sleep(1)
    else:
        print("DATA GAGAL DIHAPUS")
        time.sleep(1)

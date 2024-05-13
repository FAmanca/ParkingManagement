import db

def add():
    owner = input("Masukan Nama Owner : ")
    jenis = input("Masukan Jenis Kendaraan : ")
    merk = input("Masukan Merk Kendaraan : ")
    plat = input("Masukan Plat Nomor Kendaraan :")
    biaya = int(input("Masukan Biaya Parkir : "))

    db.create_item(owner, jenis, merk, plat, biaya)

def read():
    print(
        """
+===================================================================================+
                                  DATA KENDARAAN
+===================================================================================+
+-----------------------------------------------------------------------------------+
|    NAMA OWNER      |  JENIS KENDARAAN  |  MERK KENDARAAN  |  PLAT NOMOR  |  BIAYA |
+-----------------------------------------------------------------------------------+"""
    )
    items = db.read_item()
    for item in items:
        owner = item[1]
        jenis = item[2]
        merk = item[3]
        plat = item[4]
        biaya = item[5]
        print(f"| {owner:<15}    | {jenis:<16}  | {merk:<15}  | {plat:<10}   | {biaya:<6} |")
    print(
        "+-----------------------------------------------------------------------------------+"
    )

def delete():
    plat = input("Masukan Plat Nomor : ")
    db.delete_item(plat)

def start():
    print("""
+===================================================================================+
                                PARKING LOT MANAGEMENT
+===================================================================================+""")
    print("1. Tampilkan Data Parkir")
    print("2. Tambah Kendaraan")
    print("3. Hapus Kendaraan")
    print("4. Keluar Program")

    choice = input("Pilih Menu : ")
    if choice == "1":
        read()
    elif choice == "2":
        add()
    elif choice == "3":
        delete()
    elif choice == "4":
        exit()
    else:
        print("Menu Tidak Tersedia")

if __name__ == "__main__":
  while True:
    start()

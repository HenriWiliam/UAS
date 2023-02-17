# fitur 3
def tesAnggota():
    dataAnggota = []
    f = open('anggota.txt')
    for each_line in f:
        dataAnggota.append(each_line.strip())
    f.close()
    return dataAnggota

def tesBuku():
    dataBuku = []
    f = open('buku.txt')
    for each_line in f:
        dataBuku.append(each_line.strip())
    f.close()
    return dataBuku

def cek_buku(kd_buku):
    for i in tesBuku():
        if i[:6] == kd_buku:
            return True
    return False

def cek_anggota(kd_anggota):
    for i in tesAnggota():
        if i[:6] == kd_anggota:
            return True
    return False

def cek_stok(kd_buku):
    dataBuku = tesBuku()
    for i in range (len(dataBuku)):
        if dataBuku [i][:6] == kd_buku:
            dataBuku[i] = dataBuku[i].split(",")
            if int(dataBuku[i][-1]) > 0:
                return True
    return False

def kurangStok(kd_buku):
    dataBuku = tesBuku()
    for i in range (len(dataBuku)):
        if dataBuku [i][:6] == kd_buku:
            dataBuku[i] = dataBuku[i].split(",")
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) -1)
            dataBuku[i] = ",".join(dataBuku[i])
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n")
    myfile.close()

def tesPinjamBuku():
    a_list = []
    myfile = open("peminjaman.txt")
    for line in myfile:
        a_list.append(line.strip())
    return a_list

def pinjamBuku(kd_buku,kd_anggota):
    datapinjam = tesPinjamBuku()
    ada = 0
    for i in range(len(datapinjam)):
        if datapinjam[i][:6] == kd_buku:
            datapinjam[i] = datapinjam[i]+","+kd_anggota
            ada = 1
    if ada == 1:
        f = open('peminjaman.txt',"w+")
        for i in datapinjam:
            f.write(i+"\n")
        f.close()
    else:
        f = open('peminjaman.txt',"a+")
        f.write(kd_buku+","+kd_anggota+"\n")
        f.close()
import random, string
print ("* SELAMAT DATANG DI NF LIBRARY *")
while True:
    print ("MENU:")
    print("[1] Tambah Anggota Baru")
    print("[2] Tambah Buku Baru")
    print("[3] Pinjam Buku")
    print("[4] Kembalikan Buku")
    print("[5] Lihat Data Pinjaman")
    print("[6] Keluar")
    milih = input("Masukkan menu pilihan anda :")
    if milih == "1":
        # import random, string
        kode = "LIB" + ''.join(random.choice(string.digits) for i in range(3))
        print("**PENDAFTARAN ANGGOTA BARU**")
        nama = str(input("Masukkan Nama :"))
        validasi = input("Apakah Anda Merupakan Karyawan NF group? Y/T :")
        if validasi == "Y":
            validasi = "1"
        else:
            validasi = "2"
        print("Pendaftaran Anggota dengan kode "+kode+" atas nama "+nama+" berhasil.")
        file = open("anggota.txt", "a+")
        file.write(kode + "," + nama + ","+validasi +"\n")
        file.close()
    elif milih == "2":
        # import random, string
        print("**PENAMBAHAN BUKU BARU**")
        nama_judul = input("judul: ")
        nama_penulis = input("Penulis: ")
        jumlah_stok = input("Stok: ")
        kode1 = nama_penulis[:3].upper()  + ''.join(random.choice(string.digits) for i in range(3))
        print(" Penambahan buku baru dengan kode " +kode1+ " dan judul " +nama_judul+ " Berhasil. ")
        file = open ("buku.txt", "a+")
        file.write(kode1+"," + nama_judul + ","+nama_penulis + ","+jumlah_stok +"\n")
        file.close()
    elif milih == "3":
        print("\n**PEMINJAMAN BUKU**")
        kd_buku = input("Kode Buku: ")
        if cek_buku(kd_buku):
            kd_anggota = input("Kode Anggota: ")
            if cek_anggota(kd_anggota):
                if cek_stok(kd_buku):
                    pinjamBuku(kd_buku,kd_anggota)
                    kurangStok(kd_buku)
                    print("Peminjaman buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")
                else:
                    print("Stok buku kosong. Peminjaman gagal.")
            else:
                print("Kode anggota tidak terdaftar. Peminjaman gagal.\n")
        else:
            print("Kode buku tidak ditemukan. Peminjaman gagal.\n")
    elif milih == "4":
        print("**PENGEMBALIAN BUKU**")
        # kode_buku = (input("kode buku: "))
        # kode_anggota = (input("kode anggota: "))
        kd_buku = "RAD421"
        kd_anggota = "LIB421"

        dataPinjam = []
        myfile = open("peminjaman.txt")
        for line in myfile:
            dataPinjam.append(line.strip())

        dataanggota = []
        myfile = open("anggota.txt")
        for line in myfile:
            dataanggota.append(line.strip())

        for i in range(len(dataPinjam)):
            if dataPinjam[i][:6] == kd_buku:
                dataPinjam[i] = dataPinjam[i].split(",")
                for j in range(1,len(dataPinjam[i])):
                    if dataPinjam[i][j] == kd_anggota:
                        dataPinjam[i].remove(kd_anggota)
                        break
                if len(dataPinjam[i]) == 1:
                    del dataPinjam[i]
                    break
                else:
                    dataPinjam[i] = ",".join(dataPinjam[i])
        f = open("peminjaman.txt","w+")
        for i in dataPinjam:
            f.write(i+"\n")
        f.close()
        dataBuku = tesBuku()
        for i in range (len(dataBuku)):
            if dataBuku [i][:6] == kd_buku:
                dataBuku[i] = dataBuku[i].split(",")
                dataBuku[i][-1] = str(int(dataBuku[i][-1]) +1)
                dataBuku[i] = ",".join(dataBuku[i])
        myfile = open('buku.txt', 'w+')
        for i in dataBuku:
            myfile.write(i+"\n")
        myfile.close()

        terlambat = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat) : "))
        denda = 0

        for i in dataanggota:
            if i [:6] == kd_anggota:
                if i[-1] == "1":
                    print("NF Group")
                    denda = 1000 * terlambat
                else:
                    print("Masyaakat umum")
                    denda = 2500 * terlambat

        print("Total denda :",denda)
        print("Silakan membayar denda keterlambatan di kasir.")
        print("Pengembalian buku", kd_buku, "oleh", kd_anggota, "berhasil.")
        dataBuku = []
        myfile = open("buku.txt")
        for line in myfile:
            dataBuku.append(line.strip())

        for i in range(len(dataBuku)):
            if dataBuku[i][:6] == kd_buku:
                dataBuku[i] = dataBuku[i].split(",")
                dataBuku[i][-1] = str(int(dataBuku[i][-1])+1)
                dataBuku[i] = ",".join(dataBuku[i])

        f = open("buku.txt","w+")
        for i in dataBuku:
            f.write(i+"\n")
        f.close()
        
    elif milih == "5":
        tabel = []
        buku = {}
        file_text = open("buku.txt")
        for baris in file_text:
            tabel = baris.split(",")
            buku[tabel[0]] = [tabel[1], tabel[2], str(int(tabel[3]))]

        tabel = []
        anggota = {}
        file_text = open("anggota.txt")
        for baris in file_text:
            tabel = baris.split(",")
            anggota[tabel[0]] = [tabel[1], str(int(tabel[2]))]

        tabel = []
        peminjaman = {}
        file_text = open("peminjaman.txt")
        for baris in file_text:
            tabel = baris.split(",")
            tabel[-1] = tabel[-1][0:-1]
            peminjaman[tabel[0]] = tabel[1:]
        print("** DAFTAR PEMINJAMAN BUKU **")
        for i in peminjaman.keys():
            number = 0
            print("Judul : " +buku[i][0])
            print("Penulis : " +buku[i][1])
            print("Daftar Pinjam : ")
            for x in peminjaman[i]:
                number += 1
                print((str(number)+". "+str(anggota[x][0]))+("(*)" if anggota[x][1] == "1" else ""))
            print()
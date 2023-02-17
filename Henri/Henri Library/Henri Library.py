import random, string 
def readBuku():
    dataBuku = []
    f = open('buku.txt')
    for each_line in f:
        dataBuku.append(each_line.strip())
    f.close()
    return dataBuku

def readAnggota():
    dataAnggota = []
    f = open('anggota.txt')
    for each_line in f:
        dataAnggota.append(each_line.strip())
    f.close()
    return dataAnggota

def cek_buku(kd_buku):
    for i in readBuku():
        if i[:6] == kd_buku:
            return True
    return False

def cek_anggota(kd_anggota):
    for i in readAnggota():
        if i[:6] == kd_anggota:
            return True
    return False

def cek_stok(kd_buku):
    dataBuku = readBuku()
    for i in range (len(dataBuku)):
        if dataBuku [i][:6] == kd_buku:
            dataBuku[i] = dataBuku[i].split(",")# Mengubah string menjadi list
            if int(dataBuku[i][-1]) > 0:
                return True
    return False

def kurangStok(kd_buku):
    dataBuku = readBuku()
    for i in range(len(dataBuku)): #Ini adalah perulangan 
        if dataBuku[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
            dataBuku[i] = dataBuku[i].split(",") #Ini untuk mengubah jadi list (ngambil stok)
            dataBuku[i][-1] = str(int(dataBuku[i][-1]) - 1)# Ngubah stok 
            dataBuku[i] = ",".join(dataBuku[i])#Ngembaliin menjadi str
    myfile = open('buku.txt', 'w+')
    for i in dataBuku:
        myfile.write(i+"\n")
    myfile.close()

def readPinjamBuku():    
    a_list = []
    myfile = open("peminjaman.txt")
    for line in myfile:
        a_list.append(line.strip())
    return a_list

def pinjamBuku(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    print(dataPinjam)
    ada = 0
    for i in range(len(dataPinjam)): #Ini adalah perulangan 
        if dataPinjam[i][:6] == kd_buku:
            dataPinjam[i] = dataPinjam[i]+","+kd_anggota
            ada = 1
    if ada == 1:
        f = open('peminjaman.txt',"w+")
        for i in dataPinjam:
            f.write(i+"\n")
            f.close()
    else:
        f = open('peminjaman.txt',"a+")
        f.write(kd_buku+","+kd_anggota+"\n")
        f.close()


def cek_statusAngggota(kd_anggota):
    dataAnggota = readAnggota()
    for i in range(len(dataAnggota)):
        if dataAnggota[i][:6] == kd_anggota:
            if dataAnggota[i][-1] == "1":
                return True
            else:
                return False
def anggota_pinjam(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == kd_buku:
            dataPinjam[i] = dataPinjam[i].split(",") #Ini untuk mengubah jadi list 
            if dataPinjam[i].count(kd_anggota) == 1:
                return True
            else:
                return False
            
def remove_anggota(kd_buku,kd_anggota):
    dataPinjam = readPinjamBuku()
    for i in range(len(dataPinjam)):
        if dataPinjam[i][:6] == kd_buku: # Mengecek buku ada atau tidak di dalam file 
            dataPinjam[i] = dataPinjam[i].split(",") #Ini untuk mengubah jadi list 
            dataPinjam[i].remove(kd_anggota)
            if len(dataPinjam[i]) == 1 :
                del dataPinjam[i]
            else:
                dataPinjam[i] = ",".join(dataPinjam[i])#Ngembaliin menjadi str
                
            myfile = open('peminjaman.txt', 'w+')
            for i in dataPinjam:
                myfile.write(i+"\n")
            myfile.close()

def viewPinjam():
            # ubah data text -> list (temp) -> dict (dataBuku)
            # Data buku
    temp = []
    dataBuku = {}
    myfile = open("buku.txt")
    for line in myfile:
                temp = line.split(",") #Mengubah menjadi multiple list
                dataBuku[temp[0]] = [temp[1],temp[2],str(int(temp[3]))] #Mengubah multi list menjadi dict
            # Data Anggota
    temp = []
    dataAnggota = {}
    myfile = open("anggota.txt")
    for line in myfile:
        temp = line.split(",") #Mengubah menjadi multiple list
        dataAnggota[temp[0]] = [temp[1],str(int(temp[2]))] #Mengubah multi list menjadi dict
            # Data Pinjam
    temp = []
    dataPinjam = {}
    myfile = open("peminjaman.txt")
    for line in myfile:
        temp = line.split(",") #Mengubah menjadi multiple list
        temp[-1] = temp[-1][0:-1]
        dataPinjam[temp[0]] = temp[1:] #Mengubah multi list menjadi dict

            #kita nampilin value dataBuku dimana keysnya adalah kode buku yang ada didalam dataPinjam
    print("*** DAFTAR PEMINJAMAN BUKU ***\n")

    for i in dataPinjam.keys():
        nomer = 0
        print("Judul : "+dataBuku[i][0])
        print("Penulis : "+dataBuku[i][1])
        print("Daftar Pinjam:")
        for j in dataPinjam[i]:
            nomer +=1
            print(str(nomer)+". "+str(dataAnggota[j][0])+("(*)" if dataAnggota[j][1] == "1" else ""))
        print()
            
def viewAnggota():
            dataAnggota = readAnggota()

            print("**** DAFTAR ANGGOTA ****\n")
            for i in range(len(dataAnggota)):
                dataAnggota[i] = dataAnggota[i].split(",")
                print("Anggota "+ dataAnggota[i][0])
                print("Nama : "+dataAnggota[i][1])
                print("Status : NF Group" if dataAnggota[i][2] == "1" else "Status : Masyarakat Umum")
                print()
def viewBuku():
            dataBuku = readBuku()
            print("**** DAFTAR BUKU ****\n")
            for i in range(len(dataBuku)):
                dataBuku[i] = dataBuku[i].split(",")
                print("Kode Buku "+ dataBuku[i][0])
                print("Judul : "+dataBuku[i][1])
                print("Penulis : "+dataBuku[i][2])
                print("Stok : "+dataBuku[i][3])
                print()
print ("***** SELAMAT DATANG DI NF LIBRARY *****"
"\n===============================================")
while True:
    print ("MENU: ")
    print ("[1] Tambah Anggota Baru")
    print ("[2] Tambah Buku Baru")
    print ("[3] Pinjam Buku")
    print ("[4] Kembalikan Buku")
    print ("[5] Lihat Data Peminjaman")
    print ("[6] Keluar")
    Pilih_Menu = input("Masukkan menu pilihan anda :")

    #Penambahan Anggota

    if Pilih_Menu == "1":
        kode = "LIB" + ''.join(random.choice(string.digits) for _ in range(3))
        print("Pendaftaran Anggota Baru")
        nama = str(input("Masukkan nama Anda :"))
        validasi = input("Apakah Anda Merupakan Karyawan Henri Group? Y/T : ")
        if validasi =="Y" :
            validasi = "1"
        else:
            validasi = "2"
        print("Pendaftaran Anggota Dengan Kode "+kode+" atas nama "+nama+" berhasil.")
        file= open("anggota.txt", "a+")
        file.write("\n"+str(kode) + "," + nama + "," + validasi)
        file.close()

        #Penambahan Buku

    if Pilih_Menu == "2":
        print("Penambahan Buku")
        judul_buku = input("Judul :")
        Penulis = input("Penulis :")
        stok_buku = str(input("Stok :"))

        Penulis = Penulis.split()
        Penulis = "".join(Penulis)
        kode_buku = Penulis[:3]+"".join(random.choice(string.digits) for _ in range(3))

        print("Penambahan buku anda " +kode_buku+ " dan " +judul_buku+ " berhasil.")
        file_buku= open("buku.txt", "a+")
        file_buku.write("\n"+str(kode_buku)+","+judul_buku+","+Penulis+","+stok_buku )
        file_buku.close()
        
        #Peminjaman Buku


    elif Pilih_Menu == "3":
        print("\n*** PEMINJAMAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_buku(kd_buku):
            kd_anggota = input("Kode anggota: ")
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

        #Pengembalian Buku


    elif Pilih_Menu == "4":
        print("\n*** PENGEMBALIAN BUKU ***")
        kd_buku = input("Kode buku: ")
        if cek_buku(kd_buku):
            kd_anggota = input("Kode anggota: ")
            if anggota_pinjam(kd_buku,kd_anggota):
                denda = int(input("Keterlambatan pengembalian (dalam hari, 0 jika tidak terlambat): "))
                if cek_statusAngggota(kd_anggota):
                    denda = 1000 * denda
                else:
                    denda = 2500 * denda
                print("Total denda =",denda)
                print("Silakan membayar denda keterlambatan di kasir.")
                remove_anggota(kd_buku,kd_anggota)
                print("Pengembalian buku "+kd_buku+" oleh "+kd_anggota+" berhasil.")

            else:
                 print("Kode anggota tidak terdaftar sebagai peminjam buku tersebut. Pengembalian buku gagal.\n")
        else:
            print("Kode buku salah. Pengembalian buku gagal.")
    elif Pilih_Menu == "5":
            viewPinjam()
    # elif Pilih_Menu == "":
    #         viewAnggota()
    # elif Pilih_Menu == "7":
    #         viewBuku()
    elif Pilih_Menu == "6":
            print("Terima kasih atas kunjungan Anda...")
            break
    else:
            print("Pilihan Anda salah. Ulangi.")
        

    # clear()
    # menu()
    

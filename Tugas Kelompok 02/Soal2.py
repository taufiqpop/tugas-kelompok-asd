## Anggota Kelompok :
## 1. Febri Lailian Ikhsanudin (L200190079)
## 2. Sigit Budi Utomo (L200190084)
## 3. Muhammad Nur Taufiq (L200190085)
## 4. Surya Apriatama (L200190115)
## 5. Afrijal Nur Izza Rakhman (L200190120)

### TANAMAN OBAT ###
class Toga(object):
    def __init__(self, data):
        self.TanamanObat = data.split(";")

    def __str__(self):
        return self.TanamanObat[0] + " mengandung " + self.TanamanObat[2]
    
class Toga(object):
    def __init__(self):
        print('Pilihan Shortcut')
        self.DaftarIsi()

    TanamanObat = """Nama;YangDiambil;Kandungan;Khasiat-
Kumis kucing;Bunga;lipophilic, flavonoid, orthosiphol;ginjal, diabetes-
Jahe;Sari;zat besi, kalium, vitamin;pusing, mual, maag-
Kunyit;Sari;vitamin, antioksidan, zat besi, fosfor, kalsium;kolesterol-
Lengkuas;Sari;vitamin, zat besi, serat;nyeri, radang, kanker-
Kencur;Sari;protein, serat, mineral;nafsu makan, stamina, flu-
Temulawak;Sari;karbohidrat, lemak, protein;kembung, nafsu makan-
Kemangi;Daun;zat besi, magnesium, kalium, folat;kembung, nafsu makan-
Jeruk Nipis;Buah;vitamin, antioksidan; jantung, ginjal, kulit-
Daun Sirih;Daun;yodium, kalium, vitamin;kanker, diabetes, malaria-
"""
    
    listArray = TanamanObat.split("-")

    def simpan(self,NamaTanaman,YangDiambil,Kandungan,Khasiat):
        TONew = "\n"+NamaTanaman+";"+YangDiambil+";"+Kandungan+";"+Khasiat
        self.listArray.append(TONew)

## Nomor 2
    def cari_sk(self,Khasiat):
        self.spliter = self.listArray[Khasiat].split(";")
        self.n = self.spliter[3]
        print(self.n)

## Nomor 3
    
    def DaftarIsi(self):
        print('''
            1. List Tanaman
            2. Tambah List Tanaman
            3. Khasiat Tanaman
            4. List Tanaman Ke-
            5. Selesai
        ''')
    
        self.Menu = int(input('Input Number : '))
    
        if self.Menu == 1:
            for x in self.listArray:
                print(x)
            self.DaftarIsi()

        elif self.Menu == 2:
            self.Nama = input('\nInput Tanaman : ')
            self.Bagian = input('Input Bagian Tanaman  : ')
            self.Kandungan = input('Input Kandungan Tanaman : ')
            self.Khasiat = input('Input Khasiat Tanaman : ')
            self.simpan(self.Nama, self.Bagian, self.Kandungan, self.Khasiat)
            print('\nSaved')
            self.DaftarIsi()

        elif self.Menu == 3:
            self.x = int(input('\nInput No Urut Tanaman : '))
            self.cari_sk(self.x)
            self.DaftarIsi()

        elif self.Menu == 4:
            self.List = int(input('\nInput List Tanaman : '))
            print(self.listArray[self.List])
            self.DaftarIsi()

        elif self.Menu == 5:
            print('\nSelesai')
            
        else:
            print('\nInvalid Input')
            DaftarIsi()

Toga()
    

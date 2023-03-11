## Anggota Kelompok :
## 1. Febri Lailian Ikhsanudin (L200190079)
## 2. Sigit Budi Utomo (L200190084)
## 3. Muhammad Nur Taufiq (L200190085)
## 4. Surya Apriatama (L200190115)
## 5. Afrijal Nur Izza Rakhman (L200190120)

                       ### TANAMAN OBAT ###
#Soal 1
                ### NO 1
class Toga(object):
    def __init__(self, nama, yangDiambil, kandungan, khasiat):
        self.nama = nama
        self.yangDiambil = yangDiambil
        self.kandungan = kandungan
        self.khasiat = khasiat

    def __str__(self):
        return "{} ({})".format(self.nama,self.kandungan)
        
                ### NO 2
TanamanObat = """nama;yangDiambil;kandungan;khasiat
Kumis kucing;Bunga;lipophilic, flavonoid, orthosiphol;ginjal, diabetes
Jahe;Sari;zat besi, kalium, vitamin;pusing, mual, maag
Kunyit;Sari;vitamin, antioksidan, zat besi, fosfor, kalsium;kolesterol
Lengkuas;Sari;vitamin, zat besi, serat;nyeri, radang, kanker
Kencur;Sari;protein, serat, mineral;nafsu makan, stamina, flu
Temulawak;Sari;karbohidrat, lemak, protein;kembung, nafsu makan
Kemangi;Daun;zat besi, magnesium, kalium, folat;kembung, nafsu makan
Jeruk Nipis;Buah;vitamin, antioksidan;jantung, ginjal, kulit
Daun Sirih;Daun;yodium, kalium, vitamin;kanker, diabetes, malaria
"""
                ### NO 3
class TogaSK(object):
    def __init__(self, n):
        self._internal = n * [None]

    def __setitem__(self, key, value):
        if key >= len(self._internal):
            kurang = key - len(self._internal) + 1
            li = kurang * [None]
            self._internal.extend(li)
        self._internal[key] = value

    def __getitem__(self, key):
        if 0 <= key < len(self._internal):
            return self._internal[key]
        else:
            raise KeyError("Indeks Di Luar Kapasitas Array")
        
                ### NO 4
    def simpan(self, data):
        itemdata = data.split('\n')
        listobject = []
        for x in itemdata[1::]:
            kolom = x.split(';')
            listobject.append(kolom)

        anyar = len(listobject) - len(self._internal)
        self.__setitem__(anyar, None)
        for x in range(len(self._internal)):
            # buat object tanaman obat lalu memasukan kedalam list
            new = Toga(listobject[x][0], listobject[x][1], listobject[x][2], listobject[x][3])
            self.__setitem__(x, new)

#SOAL 2
    def cari_sk(self, kandungan):
        data = self._internal
        p = []
        kata = 'mengandung khasiat'
        for x in data:
            if x.kandungan.upper() == kandungan.upper():
                p.append(x.khasiat)
        return p

# SOAL 3
# membuat Array
DataTanamanObat = """nama;yangDiambil;kandungan;khasiat
Kumis kucing;Bunga;flavonoid;ginjal
Jahe;Sari;zat besi;pusing
Kunyit;Sari;vitamin;kolesterol
Lengkuas;Sari;vitamin;nyeri
Kencur;Sari;protein;nafsu makan
Temulawak;Sari;karbohidrat;kembung
Kemangi;Daun;zat besi;kembung
Jeruk Nipis;Buah;vitamin;jantung
Daun Sirih;Daun;yodium;kanker
"""

#memanggil method simpan
tobat = TogaSK(2)
tobat.simpan(DataTanamanObat)

#memanggil hasil memanggil method cari_sk()
print("kandungan yang berkhasiat untuk :", tobat.cari_sk('vitamin'))
print('kandungan yang berkhasiat untuk :', tobat.cari_sk('flavonoid'))

## Anggota Kelompok :
## 1. Febri Lailian Ikhsanudin (L200190079)
## 2. Sigit Budi Utomo (L200190084)
## 3. Muhammad Nur Taufiq (L200190085)
## 4. Surya Apriatama (L200190115)
## 5. Afrijal Nur Izza Rakhman (L200190120)

### TANAMAN OBAT ###
## Soal Nomor 1
class Toga(object):
    def __init__(self, data):
        self.TanamanObat = data.split(";")

    def __str__(self):
        return self.TanamanObat[0] + " mengandung " + self.TanamanObat[2]
    
# S = "Kumis kucing;Bunga;lipophilic, flavonoid, orthosiphol;ginjal"
# t = Toga(S)
# print(t)


## Soal Nomor 2
    TanamanObat = """Nama;YangDiambil;Kandungan;Khasiat
    Kumis kucing;Bunga;lipophilic, flavonoid, orthosiphol;ginjal, diabetes
    Jahe;Sari;zat besi, kalium, vitamin;pusing, mual, maag
    Kunyit;Sari;vitamin, antioksidan, zat besi, fosfor, kalsium;kolesterol
    Lengkuas;Sari;vitamin, zat besi, serat;nyeri, radang, kanker
    Kencur;Sari;protein, serat, mineral;nafsu makan, stamina, flu
    Temulawak;Sari;karbohidrat, lemak, protein;kembung, nafsu makan
    Lidah Buaya;Daun;vitamin, beta karoten;luka, pencernaan, jerawat
    Kemangi;Daun;zat besi, magnesium, kalium, folat;kembung, nafsu makan
    Jeruk Nipis;Buah;vitamin, antioksidan; jantung, ginjal, kulit
    Daun Sirih;Daun;yodium, kalium, vitamin;kanker, diabetes, malaria
    """

## Soal Nomor 3
    listArray = TanamanObat.split("-")

## Soal Nomor 4
    def simpan(self,NamaTanaman,YangDiambil,Kandungan,Khasiat):
        TONew = "\n"+NamaTanaman+";"+YangDiambil+";"+Kandungan+";"+Khasiat
        self.listArray.append(TONew)

## Soal Nomor 5
    def lihat_khasiat(self,NoUrutTanaman):
        self.spliter = self.listArray[NoUrutTanaman].split(";")
        self.n = self.spliter[3]
        print(self.n)

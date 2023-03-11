class Toga(object):
    def __init__(self, data):
        self.TanamanObat = data.split(";")

    def __str__(self):
        return self.TanamanObat[0] + " mengandung " + self.TanamanObat[2]

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

    listArray = TanamanObat.split("-")

# Soal Nomor 1

class Toga(object):
    def __init__(self, data):
        self.TanamanObat = data.split(";")

    def __str__(self):
        return self.TanamanObat[0] + " mengandung " + self.TanamanObat[2]
    
# S = "Kumis kucing;Bunga;lipophilic, flavonoid, orthosiphol;ginjal"
# t = Toga(S)
# print(t)

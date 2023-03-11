def lihat_khasiat(self,NoUrutTanaman):
        self.spliter = self.listArray[NoUrutTanaman].split(";")
        self.n = self.spliter[3]
        print(self.n)

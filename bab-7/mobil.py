class Mobil : 
  nama = ""
  warna = "merah"
  tahun = 0

  def maju(self) :
    print("Mobil maju")
  def mundur(self) :
    print("Mobil mundur")
  def belok(self) :
    print("Mobil belok")
  
  def ganti_warna(self, warna_baru) :
    self.warna = warna_baru
    print(f"Warna mobil di ganti menjadi {self.warna}")
  
  def merek_mobil(self) :
    print(f"Nama mobil adalah {self.nama} , tahun {self.tahun} , warna {self.warna}")
  
  @staticmethod
  def jumlah_roda() :
    print("Jumlah roda mobil adalah 4")

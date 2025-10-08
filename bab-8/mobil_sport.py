from mobil import Mobil

class MobilSport(Mobil):
  def turbo(self):
    self.kecepatan += 50

mobil_sport1 = MobilSport("merah", "Ferrari", 200)
print(mobil_sport1.merek)
print(mobil_sport1.kecepatan)
print(mobil_sport1.warna)
mobil_sport1.turbo()
print(mobil_sport1.kecepatan)
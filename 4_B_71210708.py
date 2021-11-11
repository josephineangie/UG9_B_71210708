print ("=====GEBYAR DISKON=====")
print ("=====MASUKKAN JUMLAH BARANG YANG DIPESAN=====")

kipas = int(input("KIPAS ANGIN DISKON 10%    Rp 25.000,00 : "))
sepeda = int(input("KIPAS ANGIN DISKON 55%    Rp 6.000,00 : "))
helm = int(input("KIPAS ANGIN DISKON 77%    Rp 8.000,00 : "))

totalkipas = (25000 * 10 / 100) * kipas
totalsepeda = (6000 * 55 / 100) * sepeda
totalhelm  = (8000 * 77 / 100) * helm

print ("=====TOTAL=====")
print ("TOTAL KIPAS ANGIN    : Rp", totalkipas)
print ("TOTAL SEPEDA SUPER   : Rp", totalsepeda)
print ("TOTAL HELMTHOR       : Rp", totalhelm)
print ("Jumlah total bayar yang harus dibayar adalah Rp", totalkipas + totalsepeda + totalhelm)
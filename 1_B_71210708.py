kata = input ("Nama : ")
cetak = kata.split ()

cetak = kata.split ()

birth = str(input ("Tempat tanggal lahir : "))
show = birth.split ()
tempat = show[0]
lahir = show[1], show[2], show[3]

if len (cetak)>2:
    print ("Haloo!", cetak[2] + ",", cetak[0], cetak[1])
else:
    print ("Haloo!", cetak[1] + ",", cetak[0])

print ("Anda Lahir di", tempat, "pada tanggal", *lahir)
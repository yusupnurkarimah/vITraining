angka = int(input("Masukkan angka: "))

if angka > 1:

   for i in range(2,angka):
       if (angka % i) == 0:
           print (angka,"bukan bilangan prima")
           print ("karena", i,"dikalikan",angka//i,"hasilnya adalah",angka)
           break
   else:
       print (angka,"adalah bilangan prima")

else:
   print (angka,"is not a prime number")
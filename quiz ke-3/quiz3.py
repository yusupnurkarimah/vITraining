list1 = []
loo = int(input("angka looping : "))

for i in range(1, loo+1):
    angka = int(input("masukan angka list ke-{}: ".format(i)))
    list1.append(angka)

pos_count, neg_count = 0, 0
 
for num in list1: 
    if num >= 0: 
        pos_count += 1
    else: 
        neg_count += 1
print(list1)
print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
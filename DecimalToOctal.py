sayi = int(input("Enter your decimal bullshit:"))
bolum = sayi // 8
kalan = sayi % 8
sekizlik = str(kalan)
while(bolum != 0):
    process = bolum
    bolum = process // 8
    kalan = process % 8
    sekizlik = sekizlik + str(kalan)
print(sekizlik[::-1])
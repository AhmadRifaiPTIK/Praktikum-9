#RUmus

def bintang(n) :
    for r in range(1,n) :
        bintang = "*" * (1 + (r-1)*2)
        print(bintang.center(10))

bintang(5)

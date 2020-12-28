#Rumus

# bintang yang dikurang

def Formasibintang2(n) :
    for r in range(n,0,-1) :
        bintang = "*" * (1 + (r-1)*2)
        print(bintang.center(10))

# bintang yang ditambah

def Formasibintang1(n) :
    for r in range(1,n+1) :
        bintang = "*" * (1 + (r-1)*2)
        print(bintang.center(10))

# Syarat
def Formasibintang3(n) :
    if (n % 2 == 0) :
        # Genap
        Formasibintang1(n//2)
    else :
        # Ganjil
        Formasibintang1(n//2+1)
    Formasibintang2(n//2)

Formasibintang3(7)
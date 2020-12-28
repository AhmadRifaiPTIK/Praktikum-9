#Rumus

import random

def shuffleString(r,n) :
    Hasil = []
    i = 0
    while i < n :
        acak = ''.join(random.sample(r,len(r)))
        if (acak not in Hasil) :
            Hasil += [acak]
            i += 1
    print(Hasil)

#output

shuffleString('aku',6)
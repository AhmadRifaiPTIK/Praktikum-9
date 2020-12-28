#Rumus

def ubahHuruf(teks, a, b):
    listTeks = list(teks)
    output = ""

    for char in listTeks:
        if (char == a):
            char = b
        output = ''.join([output, char])
    return output

#output

print(ubahHuruf("MATEMATIKA", "T", "S"))
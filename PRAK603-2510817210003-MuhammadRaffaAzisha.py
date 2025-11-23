n1, n2 = map(int, input().split())

if n1 != n2:
    print("Jumlah tidak sama")
else:
    baris1 = list(map(int, input().split()))
    baris2 = list(map(int, input().split()))
    
    hasil = []
    for i in range(n1):
        hasil.append(str(baris1[i] * baris2[i]))
    
    print(' '.join(hasil))
kode = input()
pesan = input()

jumlah_bintang = 0
jumlah_pagar = 0
hasil_simbol = ""

if len(kode) != len(pesan):
    print("Panjang kalimat berbeda, pesan palsu")
else:
    for i in range(len(kode)):
        if kode[i] == ' ' and pesan[i] == ' ':
            hasil_simbol += ' '
            continue 
        
        if kode[i] == pesan[i]:
            hasil_simbol += '*'
            jumlah_bintang += 1
        else:
            hasil_simbol += '#'
            jumlah_pagar += 1

    print(hasil_simbol)
    print(f"* = {jumlah_bintang}")
    print(f"# = {jumlah_pagar}")

    if jumlah_bintang >= jumlah_pagar:
        print("Pesan Asli")
    else:
        print("Pesan Palsu")
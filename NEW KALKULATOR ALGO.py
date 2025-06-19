def PilihanUtama():
    print("===============================")
    print("1. Perhitungan")
    print("2. Faktorial")#Tambahan (part2)
    print("3. History")
    print("4. Akhiri")

def PilihanOperator():
    print("===============================")
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (*)")
    print("4. Bagi (/)")
    
def Perhitungan(a,b,c):
    a = float(a)
    c = float(c)
    hasil = 0
    if b == '+':
        hasil = a + c
    elif b == '-':
        hasil = a - c
    elif b == '*':
        hasil = a * c
    else:
        if (b == '/' and c == 0):
            hasil = 0
            print("Tidak Terdefinisi")
        else:
            hasil = a/c
    return(hasil)

def Faktorial(a):#Tambahan (part2)
     if(a == 0):
        return(1)
     else:
        return(a*Faktorial(a-1))

def MasukkanFaktorial(a):#Tambahan (part2)
    history.append(f"{a}!")
    history.append("=")
    history.append(hasil)
    history.append("")
    history.append("")
    History(history)
    history.clear()

def Operator(a):
    if a == '1':
        op = '+'
    elif a == '2':
        op = '-'
    elif a == '3':
        op = '*'
    elif a == '4':
        op = '/'
    return(op)

historyMain = []
history = []

def History(a):
    historyMain.append(a.copy())

def Masukkan(x,operator,y):
    history.append(x)
    history.append(operator)
    history.append(y)
    history.append("=")

jawab = 'Y'
while jawab == 'Y' or jawab == 'y':
    hasil = 0
    PilihanUtama()
    mulai = input("Masukkan pilihan berdasarkan angka = ")
    if mulai == '1':
        PilihanOperator()
        ulang2 = 'y'
        while ulang2 == 'y':
            mulai2 = input("Masukkan pilihan berdasarkan angka = ")
            if mulai2 != "1" and mulai2 != "2" and mulai2 != "3" and mulai2 != "4":
                        print("Salah Input!!")
            else:
                ulang2 = 't'
        operator = Operator(mulai2)
        x = input("Masukkan bil1 = ")
        y = input("Masukkan bil2 = ")
        
        Masukkan(x,operator,y)
        hasil = Perhitungan(x,operator,y)
        ##############################(Ada yang dihilangkan(part2))
##        if (b == '/' and c == 0):
##            hasil = 0
##            print("Tidak Terdefinisi")
##        else:
##            hasil = a/c
        ##############################
        history.append(hasil)
        History(history)
        history.clear()
        lanjut = 'Y'
        lanjut2 = 'T' ##tambahan
        while lanjut == 'Y' or lanjut == 'y':
            print("===============================")
            print("1. Hasil")
            print("2. Lanjut Operator")
            mulai3 = input("Masukkan pilihan berdasarkan angka: ")
            if mulai3 == '1':
                print("===============================")
                print("Hasil =", hasil)
                lanjut2 = input("Apakah anda ingin lanjut berhitung? (Y/T) = ")##Diubah
                #dihilangkan (part2)
            elif mulai3 == '2':
                lanjut2 = 'Y'
            else:
                print("Salah Input")## diubah
                lanjut2 = 't' ## tambahan
            if lanjut2 == 'Y' or lanjut2 == 'y':##diubah
                x = hasil
                PilihanOperator()
                ulang2 = 'y'
                while ulang2 == 'y':
                    mulai2 = input("Masukkan pilihan berdasarkan angka = ")
                    if mulai2 != "1" and mulai2 != "2" and mulai2 != "3" and mulai2 != "4":
                        print("Salah Input!!")
                    else:
                        ulang2 = 't'
                operator = Operator(mulai2)
                y = input("Masukkan bil = ")
                lanjut = 'y' ##Tambah
                Masukkan(x, operator, y)
                hasil = Perhitungan(x,operator,y)
                history.append(hasil)
                History(history)
                history.clear()
            else:
                lanjut = 't'#tambah(part2)
    elif mulai == '2':#tambah(part2)
        jawab2 = 'Y'
        while jawab2 == 'y' or jawab2 =='Y':
            print("===============================")
            masukBil = int(input("Masukkan bil faktorial = "))
            hasil = Faktorial(masukBil)
            isi = masukBil
            MasukkanFaktorial(isi)
            for i in range(0,masukBil):
                if i == masukBil-1:
                    print(isi,end=" = ")
                else:
                    print(isi,end=" * ")
                isi -= 1
            print(hasil)
            jawab2 = input("Apakah ingin mengulang program? (Y/T) = ")
    elif mulai == '3': #Diubah(part2)
        up = len(historyMain)
        for i in range(0,up):
            print((i+1),end=") ")
            for j in range(0,5):
                print(historyMain[i][j], end=" ")
            print()
    elif mulai == '4': #diubah(part2)
        print()
        jawab = 't'
    else:
        print("Salah input!!!")

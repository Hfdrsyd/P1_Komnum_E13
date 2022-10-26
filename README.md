# P1_Komnum_E13

kelompok 13:
1. Muhammad Hafidh Rosyadi – 5025211013 
2. Heru Dwi Kurniawan – 5025211055 
3. Mohammad Ahnaf Fauzan – 5025211170

metode bolzano merupakan metode pencarian akar persamaan dengan membandingkan nilai tengah dari suatu rentang solusi dengan rentang solusi tersebut, dengan tujuan mendekat kan hasil ke arah 0. Selain itu pembandingan tersebut dilakukan hingga mencapai suatu ketelitian tertentu.
metode bolzano ahnya dapat dijalankan ketika perkalian kedua rentang dari solusi persamaan bernilai negatif

print("rentang perkiraan letak solusi persamaan ")
Xa = float(input("rentang awal : "))
Xb = float(input("rentang akhir: "))
n = int(input("banyak iterasi : "))
if f(Xa)*f(Xb) < 0:
    ArrTable = []
    for i in range(n):
        Xc = (Xa + Xb)/2
        Fa = f(Xa)
        Fb = f(Xb)
        Fc = f(Xc)

        ArrTable.append([Xa, Xb, Xc, Fa, Fb, Fc])

        if Fa*Fc < 0:
            Xb = Xc
        elif Fa*Fc > 0:
            Xa = Xc
        else:
            break
    Table = pd.DataFrame(ArrTable, columns=['Xa', 'Xb', 'Xc', 'Fa', 'Fb', 'Fc'])
    Table.index = np.arange(1, len(Table)+1)
    print(Table)
    print(f"\nMaka akar persamaan yang diperoleh adalah {Xc}\n")
else:
    print("Tidak memenuhi syarat metode bolzano")

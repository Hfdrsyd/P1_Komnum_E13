# P1_Komnum_E13

kelompok 13:
1. Muhammad Hafidh Rosyadi – 5025211013 
2. Heru Dwi Kurniawan – 5025211055 
3. Mohammad Ahnaf Fauzan – 5025211170

metode bolzano merupakan metode pencarian akar persamaan dengan membandingkan nilai tengah dari suatu rentang solusi dengan rentang solusi tersebut, dengan tujuan mendekat kan hasil ke arah 0. 
Selain itu pembandingan tersebut dilakukan hingga mencapai suatu ketelitian tertentu.
metode bolzano hanya dapat dijalankan ketika perkalian kedua rentang dari solusi persamaan bernilai negatif.
disini kami menggunakan library numpy(untuk menggenerate angka), pandas(untuk membuat tabel), dan matplotlib (untuk menggambar perkiraan grafik).

berikut merupakan kode untuk perhitungan metode bolzano
```python
    print("rentang perkiraan letak solusi persamaan ")
    Xa = float(input("rentang awal : "))
    Xb = float(input("rentang akhir: "))
    n = int(input("banyak iterasi : "))
    if f(Xa)*f(Xb) < 0:#melakukan pengecekan terhadap syarat metode bolzano
        ArrTable = []
        for i in range(n):#melakukan looping hingga mencapai ketelitian yang tertentu yang diharapkan
            #menghitung nilai tengah dari rentang
            Xc = (Xa + Xb)/2
            Fa = f(Xa)
            Fb = f(Xb)
            Fc = f(Xc)
            #melakukan push ke list penyimpanan
            ArrTable.append([Xa, Xb, Xc, Fa, Fb, Fc])
            #melakukan penetapan nilai rentang yang baru
            if Fa*Fc < 0:
                Xb = Xc
            elif Fa*Fc > 0:
                Xa = Xc
            else: #sudah bertemu akar persamaan
                break
        #memasukkan data list ke dalam tabel dengan bantuan library pandas
        Table = pd.DataFrame(ArrTable, columns=['Xa', 'Xb', 'Xc', 'Fa', 'Fb', 'Fc'])
        Table.index = np.arange(1, len(Table)+1)#melakukan generating index pada tabel 
        print(Table)#print terhadap tabel yang telah buat
        print(f"\nMaka akar persamaan yang diperoleh adalah {Xc}\n")#print nilai x setelah n iterasi
    else:
        print("Tidak memenuhi syarat metode bolzano")
```
selanjutnya untuk menampilkan grafik dilakukan dengan library matplotlib, yaitu menampilkan grafik menggunakan titik - titik dari suatu fungsi yang dihubungkan dengan garis.
berikut kode untuk menampilkan grafik:
```python
    print("rentang grafik yang akan ditampilkan : ")
    Xawal = float(input("X awal : "))
    Xakhir = float(input("X akhir : "))
    x = np.arange(Xawal, Xakhir, 0.01)#meng-generate titik x dengan batas Xawal hingga Xakhir dengan ketelitian 0.01
    y = f(x)#melakukan perhitungan nilai y pada setiap titik x
    plt.grid()#memberi grid pada grafik sehingga memudahkan membaca
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.plot(x, y)#melakukan plotting terhadap tiap nilai x dan y
    plt.show()#menampilkan grafik
```
misal digunakan fungsi
```python
    def f(x):
        return x**2+x-5
```
dengan Xa = -5, Xb = 0, dan hingga 20 iterasi diperoleh output sebagai berikut:
![image](https://user-images.githubusercontent.com/92217730/198016406-b66968c0-77d5-4413-8e37-5c8ddecbbc75.png)

kemudian digunakan Xawal = -20 dan Xakhir = 20, sehingga diperoleh grafik sebagai berikut:
![image](https://user-images.githubusercontent.com/92217730/198017224-76c36e60-4fea-452e-9060-72f3f5eb7cdc.png)


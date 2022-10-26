import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return x**2+x-5

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


print("rentang grafik yang akan ditampilkan : ")
Xawal = float(input("X awal : "))
Xakhir = float(input("X akhir : "))
x = np.arange(Xawal, Xakhir, 0.01)
y = f(x)
plt.grid()
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x, y)
plt.show()


import time
import numpy as np
import matplotlib.pyplot as plt

def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        total += f(a + i * dx) * dx
    return total

def f(x):
    return 4 / (1 + x**2)

# Nilai Referensi π
pi_referensi = 3.14159265358979323846

# Variasi Nilai N
nilai_N = [10, 100, 1000, 10000]

# Simpan Hasil
hasil = []

for N in nilai_N:
    start_time = time.time()
    pi_approx = riemann_integral(f, 0, 1, N)
    waktu_eksekusi = time.time() - start_time
    galat_rms = np.sqrt((pi_approx - pi_referensi)**2)
    hasil.append((N, pi_approx, galat_rms, waktu_eksekusi))

# Tampilkan hasil 
for N, pi_approx, galat_rms, waktu_eksekusi in hasil:
    print(f"N={N}, pi_approx={pi_approx:.6f}, Galat RMS={galat_rms:.6f}, Waktu Eksekusi={waktu_eksekusi:.6f} detik")


N_values = [x[0] for x in hasil]
galat_rms_values = [x[2] for x in hasil]
waktu_eksekusi_values = [x[3] for x in hasil]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(N_values, galat_rms_values, marker='o')
plt.xscale('log')
plt.xlabel('N (skala log)')
plt.ylabel('Galat RMS')
plt.title('Galat RMS terhadap Nilai N')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(N_values, waktu_eksekusi_values, marker='o')
plt.xscale('log')
plt.xlabel('N (skala log)')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Waktu Eksekusi terhadap Nilai N')
plt.grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Rentang usia 0 sampai 150 tahun
usia = np.linspace(0, 150, 3000)


# ==========================================
# FUNGSI KEANGGOTAAN TRAPESIUM
# ==========================================

def fungsi_trapesium(usia, a, b, c, d):

    nilai = np.zeros_like(usia)

    # Bagian naik
    if b > a:
        kondisi_naik = (usia >= a) & (usia < b)
        nilai[kondisi_naik] = (usia[kondisi_naik] - a) / (b - a)

    # Bagian datar
    kondisi_datar = (usia >= b) & (usia <= c)
    nilai[kondisi_datar] = 1

    # Bagian turun
    if d > c:
        kondisi_turun = (usia > c) & (usia <= d)
        nilai[kondisi_turun] = (d - usia[kondisi_turun]) / (d - c)

    return nilai


# ==========================================
# FUNGSI SETIAP KATEGORI USIA
# ==========================================

# Bayi / Balita
bayi = fungsi_trapesium(usia, 0, 3, 3, 5)

# Anak-anak
anak = fungsi_trapesium(usia, 5, 8.5, 8.5, 11)

# Remaja
remaja = fungsi_trapesium(usia, 11, 14, 14, 19)

# Pemuda
pemuda = fungsi_trapesium(usia, 15, 20, 20, 24)

# Dewasa
dewasa = fungsi_trapesium(usia, 20, 40, 40, 65)

# Lansia
lansia = fungsi_trapesium(usia, 65, 85, 85, 95)


# ==========================================
# MEMBUAT GRAFIK
# ==========================================

plt.figure(figsize=(14, 7))

plt.plot(
    usia, bayi,
    label="Bayi / Balita (0-5 thn)",
    color="blue"
)

plt.plot(
    usia, anak,
    label="Anak-anak (6-11 thn)",
    color="green"
)

plt.plot(
    usia, remaja,
    label="Remaja (11-19 thn)",
    color="purple"
)

plt.plot(
    usia, pemuda,
    label="Pemuda (15-24 thn)",
    color="orange"
)

plt.plot(
    usia, dewasa,
    label="Dewasa (24-65 thn)",
    color="red"
)

plt.plot(
    usia, lansia,
    label="Lansia (>=65 thn)",
    color="brown"
)


# ==========================================
# PENGATURAN GRAFIK
# ==========================================

plt.title("Fungsi Keanggotaan Usia (Trapesium)")

plt.xlabel("Usia (Tahun)")

plt.ylabel("Derajat Keanggotaan (μ)")

plt.xlim(0, 150)

plt.ylim(0, 1.05)

plt.xticks(np.arange(0, 151, 5))

plt.yticks(np.arange(0, 1.1, 0.2))

plt.grid(
    True,
    linestyle="--",
    alpha=0.5
)

plt.legend()

plt.tight_layout()

plt.show()
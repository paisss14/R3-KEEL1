# ini fungsi buat ngitung diskonnya
def hitung_diskon(harga, diskon):
    return harga - (harga * diskon // 100)

# ini fungsi buat nentuin kategori diskon
def kategori_diskon(diskon):
    if diskon <= 0:
        return "tidak dapat diskon"
    elif diskon < 20:
        return "💸 Hemat kecil"
    elif diskon < 50:
        return "💰 Hemat sedang"
    else:
        return "🎉 Hemat besar!"

# ini buat inputan sama ngehitung harga akhir + diskon nya
harga_awal = int(input("Masukkan harga barang: Rp "))
diskon = int(input("Masukkan diskon (%): "))
nama_barang = input("masukkan nama barang mu: ")
harga_akhir = hitung_diskon(harga_awal, diskon)
harga_diskon = harga_awal - harga_akhir

# ini hasil akhir yng bakal di cetak semuanye
print("===== Kalkulator Diskon =====")
print(f"📦 Barang = {nama_barang}")
print(f"💵 Harga awal = {harga_awal}")
print(f"🔖 Diskon = {diskon}%")
print(f"✅ Harga setelah diskon = Rp.{harga_akhir}")
print(f"🎯 kamu {kategori_diskon(diskon)}, senilai = Rp.{harga_diskon}")

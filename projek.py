# ini fungsi buat ngitung diskonnya
def hitung_diskon(harga, diskon):
    return harga - (harga * diskon / 100)

def kategori_diskon(diskon):
    if diskon < 20:
        return "💸 Hemat kecil"
    elif diskon < 50:
        return "💰 Hemat sedang"
    else:
        return "🎉 Hemat besar!"

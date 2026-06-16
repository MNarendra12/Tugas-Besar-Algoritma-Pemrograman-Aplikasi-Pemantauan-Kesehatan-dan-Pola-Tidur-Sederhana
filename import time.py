import time

riwayat_tidur = []
def hitung_durasi(jam_tidur, jam_bangun):
    jt, mt = map(int, jam_tidur.split('.' ))
    jb, mb = map(int, jam_bangun.split('.'))
    
    tidur_menit = jt * 60 + mt
    bangun_menit = jb * 60 + mb
    
    if bangun_menit < tidur_menit:
        bangun_menit += 24 * 60
        
    durasi_jam = (bangun_menit - tidur_menit) / 60
    return round(durasi_jam, 2)

def saran_pola_tidur(durasi):
    if durasi < 7:
        return "Kurang tidur. Disarankan untuk tidur 7-9 jam per malam."
    elif durasi > 9:
        return "Tidur berlebih. Usahakan tidur maksimal 9 jam."
    else:
        return "Pola tidur sangat sehat. Pertahankan!"

def konversi_tanggal(tanggal):
    hari, bulan, tahun = tanggal.split('-')
    return int(f"{tahun}{bulan}{hari}")

def tambah_data():
    tanggal = input("Masukkan tanggal (DD-MM-YYYY): ")
    jam_tidur = input("Masukkan jam tidur (jam.menit): ")
    jam_bangun = input("Masukkan jam bangun (jam.menit): ")
    kualitas = input("Kualitas tidur (Baik/Biasa/Buruk): ")
    
    durasi = hitung_durasi(jam_tidur, jam_bangun)
    saran = saran_pola_tidur(durasi)
    
    data_baru = {
        'tanggal': tanggal,
        'jam_tidur': jam_tidur,
        'jam_bangun': jam_bangun,
        'kualitas': kualitas,
        'durasi': durasi,
        'saran': saran
    }
    riwayat_tidur.append(data_baru)
    print("Data berhasil ditambahkan.")

def ubah_data():
    tanggal = input("Masukkan tanggal data yang ingin diubah (DD-MM-YYYY): ")
    for data in riwayat_tidur:
        if data['tanggal'] == tanggal:
            print("Data ditemukan.")
            data['jam_tidur'] = input("Jam tidur baru (jam.menit): ")
            data['jam_bangun'] = input("Jam bangun baru (jam.menit): ")
            data['kualitas'] = input("Kualitas tidur baru: ")
            data['durasi'] = hitung_durasi(data['jam_tidur'], data['jam_bangun'])
            data['saran'] = saran_pola_tidur(data['durasi'])
            print("Data berhasil diubah.")
            return
    print("Data tidak ditemukan.")

def hapus_data():
    tanggal = input("Masukkan tanggal data yang ingin dihapus (DD-MM-YYYY): ")
    for i in range(len(riwayat_tidur)):
        if riwayat_tidur[i]['tanggal'] == tanggal:
            del riwayat_tidur[i]
            print("Data berhasil dihapus.")
            return
    print("Data tidak ditemukan.")

def cari_sequential(tanggal_dicari):
    hasil = []
    for data in riwayat_tidur:
        if data['tanggal'] == tanggal_dicari:
            hasil.append(data)
    return hasil

def cari_binary(tanggal_dicari):
    sort_insertion_tanggal()
    target = konversi_tanggal(tanggal_dicari)
    low = 0
    high = len(riwayat_tidur) - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_val = konversi_tanggal(riwayat_tidur[mid]['tanggal'])
        
        if mid_val == target:
            return riwayat_tidur[mid]
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def menu_cari_data():
    print("\n--- Menu Cari Data ---")
    print("1. Pencarian Sequential")
    print("2. Pencarian Binary")
    pilihan_cari = input("Pilih metode pencarian (1/2): ")
    
    if pilihan_cari == '1':
        tgl = input("Masukkan tanggal yang dicari (DD-MM-YYYY): ")
        hasil = cari_sequential(tgl)
        
        if hasil:
            for h in hasil:
                print(f"Ditemukan: Durasi {h['durasi']} jam, Kualitas: {h['kualitas']}")
        else:
            print("Data tidak ditemukan.")
            
    elif pilihan_cari == '2':
        tgl = input("Masukkan tanggal yang dicari (DD-MM-YYYY): ")
        hasil = cari_binary(tgl)
        
        if hasil:
            print(f"Ditemukan: Durasi {hasil['durasi']} jam, Kualitas: {hasil['kualitas']}")
        else:
            print("Data tidak ditemukan.")

            
    else:
        print("Pilihan metode tidak valid.")

def sort_selection_durasi():
    n = len(riwayat_tidur)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if riwayat_tidur[j]['durasi'] < riwayat_tidur[min_idx]['durasi']:
                min_idx = j
        riwayat_tidur[i], riwayat_tidur[min_idx] = riwayat_tidur[min_idx], riwayat_tidur[i]

def sort_insertion_tanggal():
    for i in range(1, len(riwayat_tidur)):
        key_item = riwayat_tidur[i]
        j = i - 1
        
        while j >= 0 and konversi_tanggal(riwayat_tidur[j]['tanggal']) > konversi_tanggal(key_item['tanggal']):
            riwayat_tidur[j + 1] = riwayat_tidur[j]
            j -= 1
        riwayat_tidur[j + 1] = key_item

def menu_urutkan_data():
    print("\n--- Menu Urutkan Data ---")
    print("1. Urutkan berdasar Durasi (Selection Sort)")
    print("2. Urutkan berdasar Tanggal (Insertion Sort)")
    pilihan_urut = input("Pilih metode pengurutan (1/2): ")
    
    if pilihan_urut == '1':
        sort_selection_durasi()
        print("Data berhasil diurutkan berdasarkan durasi.")
        for d in riwayat_tidur:
            print(f"Tanggal: {d['tanggal']} - Durasi: {d['durasi']} jam")
    elif pilihan_urut == '2':
        sort_insertion_tanggal()
        print("Data berhasil diurutkan berdasarkan tanggal.")
        for d in riwayat_tidur:
            print(f"Tanggal: {d['tanggal']} - Durasi: {d['durasi']} jam")
    else:
        print("Pilihan metode tidak valid.")

def tampilkan_laporan():
    if not riwayat_tidur:
        print("Belum ada data untuk ditampilkan.")
        return
        
    sort_insertion_tanggal()
    print("\n--- Laporan 7 Hari Terakhir ---")
    
    terakhir = riwayat_tidur[-7:]
    total_durasi = 0
    
    for data in terakhir:
        print(f"Tanggal: {data['tanggal']} | Tidur: {data['jam_tidur']} - Bangun: {data['jam_bangun']}")
        print(f"Durasi: {data['durasi']} jam | Kualitas: {data['kualitas']}")
        print(f"Catatan: {data['saran']}\n")
        total_durasi += data['durasi']
    
    rata_rata = total_durasi / len(terakhir)
    print("--- Rekapitulasi Mingguan ---")
    print(f"Total durasi tidur: {total_durasi:.2f} jam")
    print(f"Rata-rata durasi tidur per hari: {rata_rata:.2f} jam")

while True:
    print("\n=== Aplikasi Pemantauan Pola Tidur ===")
    print("1. Tambah Riwayat Tidur")
    print("2. Ubah Riwayat Tidur")
    print("3. Hapus Riwayat Tidur")
    print("4. Cari Data")
    print("5. Urutkan Data")
    print("6. Tampilkan Laporan Mingguan")
    print("7. Keluar")
    
    pilihan = input("Pilih menu (1-7): ")
    
    if pilihan == '1':
        tambah_data()
    elif pilihan == '2':
        ubah_data()
    elif pilihan == '3':
        hapus_data()
    elif pilihan == '4':
        menu_cari_data()
    elif pilihan == '5':
        menu_urutkan_data()
    elif pilihan == '6':
        tampilkan_laporan()
    elif pilihan == '7':
        print("Terima kasih telah menggunakan aplikasi ini.")
        break
    else:
        print("Pilihan tidak valid.")
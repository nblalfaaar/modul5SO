def hitung_need(maks, alokasi):
    """Need = Max - Allocation (sisa kebutuhan tiap proses)."""
    return [[m - a for m, a in zip(baris_m, baris_a)]
            for baris_m, baris_a in zip(maks, alokasi)]


def cek_aman(tersedia, maks, alokasi, nama):
    """Safety Algorithm: cari urutan penyelesaian yang aman."""
    need = hitung_need(maks, alokasi)
    work = tersedia[:] 
    selesai = [False] * len(nama)
    urutan = []

    while len(urutan) < len(nama):
        ada_yang_bisa = False
        for i in range(len(nama)):
            if not selesai[i] and all(n <= w for n, w in zip(need[i], work)):
                work = [w + a for w, a in zip(work, alokasi[i])]
                selesai[i] = True
                urutan.append(nama[i])
                ada_yang_bisa = True
        if not ada_yang_bisa:
            return False, urutan 
    return True, urutan


def minta_resource(i, request, tersedia, maks, alokasi, nama):
    """Resource-Request Algorithm: izinkan hanya jika hasilnya tetap aman."""
    need = hitung_need(maks, alokasi)
    print(f"\n>> {nama[i]} meminta {request}")

    if any(r > n for r, n in zip(request, need[i])):
        print("   DITOLAK : permintaan melebihi klaim maksimum (Need)")
        return False
    if any(r > t for r, t in zip(request, tersedia)):
        print("   DITUNDA : resource belum tersedia, proses harus menunggu")
        return False

    # Langkah 1: alokasikan sementara
    tersedia_coba = [t - r for t, r in zip(tersedia, request)]
    alokasi_coba = [baris[:] for baris in alokasi]
    alokasi_coba[i] = [a + r for a, r in zip(alokasi_coba[i], request)]

    # Langkah 2: cek apakah state hasilnya aman
    aman, urutan = cek_aman(tersedia_coba, maks, alokasi_coba, nama)

    if aman:
        # Langkah 3a: aman -> kabulkan sungguhan
        tersedia[:] = tersedia_coba
        alokasi[:] = alokasi_coba
        print("   DIIZINKAN : state tetap AMAN. Urutan aman: " + " -> ".join(urutan))
        return True

    # Langkah 3b: tidak aman -> batalkan, proses menunggu
    print("   DITOLAK : jika dikabulkan, state menjadi TIDAK AMAN (berisiko deadlock)")
    return False


def lepas_semua(i, tersedia, alokasi, nama):
    """Proses i selesai dan mengembalikan semua resource yang dipegang."""
    tersedia[:] = [t + a for t, a in zip(tersedia, alokasi[i])]
    alokasi[i] = [0] * len(tersedia)
    print(f"\n>> {nama[i]} selesai, semua resource dikembalikan. Available = {tersedia}")


def tampilkan(judul, tersedia, maks, alokasi, nama):
    need = hitung_need(maks, alokasi)
    print(f"\n=== {judul} ===")
    print(f"{'Proses':<10}{'Allocation':<14}{'Max':<14}{'Need':<14}")
    for i, p in enumerate(nama):
        print(f"{p:<10}{str(alokasi[i]):<14}{str(maks[i]):<14}{str(need[i]):<14}")
    print(f"Available : {tersedia}")
    aman, urutan = cek_aman(tersedia, maks, alokasi, nama)
    print("State     : " + ("AMAN, urutan " + " -> ".join(urutan) if aman else "TIDAK AMAN"))

#  Kasus 1 : Cerita Orang 1 & Orang 2
#  Resource = [kunci1, kunci2], masing-masing hanya 1 buah.
#  Max = [1, 1]
print("#" * 60)
print("KASUS 1 : Orang 1 & Orang 2 memperebutkan kunci1 dan kunci2")
print("#" * 60)

nama = ["Orang 1", "Orang 2"]
maks = [[1, 1], [1, 1]]
alokasi = [[0, 0], [0, 0]]
tersedia = [1, 1]

tampilkan("Kondisi awal", tersedia, maks, alokasi, nama)

minta_resource(0, [1, 0], tersedia, maks, alokasi, nama)   # Orang 1 minta kunci1
minta_resource(1, [0, 1], tersedia, maks, alokasi, nama)   # Orang 2 minta kunci2
minta_resource(0, [0, 1], tersedia, maks, alokasi, nama)   # Orang 1 minta kunci2
lepas_semua(0, tersedia, alokasi, nama)                    # Orang 1 selesai
minta_resource(1, [0, 1], tersedia, maks, alokasi, nama)   # sekarang giliran Orang 2


#  Kasus 2 : Contoh klasik 5 proses x 3 jenis resource (A, B, C)
#  Total resource: A = 10, B = 5, C = 7

print("\n" + "#" * 60)
print("KASUS 2 : 5 proses x 3 jenis resource (contoh klasik)")
print("#" * 60)

nama = ["P0", "P1", "P2", "P3", "P4"]
alokasi = [[0, 1, 0],
           [2, 0, 0],
           [3, 0, 2],
           [2, 1, 1],
           [0, 0, 2]]
maks = [[7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]]
tersedia = [3, 3, 2]

tampilkan("Kondisi awal", tersedia, maks, alokasi, nama)

minta_resource(1, [1, 0, 2], tersedia, maks, alokasi, nama)   # P1 minta (1,0,2)
minta_resource(4, [3, 3, 0], tersedia, maks, alokasi, nama)   # P4 minta (3,3,0)
minta_resource(0, [0, 2, 0], tersedia, maks, alokasi, nama)   # P0 minta (0,2,0)
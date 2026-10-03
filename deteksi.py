def buat_wait_for(memegang, menunggu):
    """
    memegang : {resource: pemilik}   -> siapa memegang resource apa
    menunggu : {proses: resource}    -> proses sedang menunggu resource apa
    Hasil    : {proses: [proses yang ditunggu]}  (Wait-For Graph)
    """
    semua_proses = sorted(set(memegang.values()) | set(menunggu))
    graph = {p: [] for p in semua_proses}
    for proses, resource in menunggu.items():
        pemilik = memegang.get(resource)
        if pemilik is not None and pemilik != proses:
            graph[proses].append(pemilik)
    return graph


def cek_siklus(graph):
    """Cari siklus di graph dengan DFS. Hasil: list siklus, atau None."""
    pernah_dikunjungi = set()
    jalur = []  

    def dfs(node):
        pernah_dikunjungi.add(node)
        jalur.append(node)

        for tetangga in graph.get(node, []):
            if tetangga in jalur:  
                awal = jalur.index(tetangga)
                return jalur[awal:] + [tetangga]
            if tetangga not in pernah_dikunjungi:
                hasil = dfs(tetangga)
                if hasil:
                    return hasil

        jalur.pop()
        return None

    for node in graph:
        if node not in pernah_dikunjungi:
            hasil = dfs(node)
            if hasil:
                return hasil
    return None


def tampilkan(judul, graph):
    print(f"\n=== {judul} ===")
    for proses, tujuan in graph.items():
        print(f"  {proses} menunggu: {', '.join(tujuan) if tujuan else '-'}")


def periksa(judul, memegang, menunggu):
    graph = buat_wait_for(memegang, menunggu)
    tampilkan(judul, graph)
    siklus = cek_siklus(graph)
    if siklus:
        print("  DEADLOCK DETECTED! Siklus: " + " -> ".join(siklus))
    else:
        print("  Tidak ada deadlock")
    return siklus

# Kasus 1 : kondisi program deadlock.py setelah 1 detik
memegang_macet = {"kunci1": "Orang 1", "kunci2": "Orang 2"}
menunggu_macet = {"Orang 1": "kunci2", "Orang 2": "kunci1"}
periksa("Kasus 1 (macet)", memegang_macet, menunggu_macet)

# Kasus 2 : Orang 2 sudah memegang kunci2 tetapi tidak menunggu apa pun
memegang_aman = {"kunci1": "Orang 1", "kunci2": "Orang 2"}
menunggu_aman = {"Orang 1": "kunci2"}
periksa("Kasus 2 (aman)", memegang_aman, menunggu_aman)
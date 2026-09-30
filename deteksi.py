def cek_siklus(graph):
    pernah_dikunjungi = set()
    sedang_dalam_stack = set()

    def dfs(node, jalur):
        pernah_dikunjungi.add(node)
        sedang_dalam_stack.add(node)

        for next_node in graph.get(node, []):
            if next_node in sedang_dalam_stack:
                # potong jalur mulai dari awal siklus
                return jalur[jalur.index(next_node):] + [next_node]
            if next_node not in pernah_dikunjungi:
                hasil = dfs(next_node, jalur + [next_node])
                if hasil:
                    return hasil

        sedang_dalam_stack.remove(node)
        return None

    for node in graph:
        if node not in pernah_dikunjungi:
            siklus = dfs(node, [node])
            if siklus:
                return True, siklus

    return False, []

def tampilkan(nama, graph):
    macet, siklus = cek_siklus(graph)
    print(f"[{nama}]")
    if macet:
        print("  DEADLOCK DETECTED! Siklus:", " -> ".join(siklus))
    else:
        print("  Amannnn, ga ada deadlock yeyy")

kasus_macet = {
    "Orang 1": ["Orang 2"],
    "Orang 2": ["Orang 1"],
}
kasus_aman = {
    "Orang 1": ["Orang 2"],
    "Orang 2": [],
}

tampilkan("Kasus 1: saling menunggu", kasus_macet)
tampilkan("Kasus 2: menunggu tanpa siklus", kasus_aman)
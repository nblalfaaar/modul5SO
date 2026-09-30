def hentikan_proses(graph, korban):
#     """Simulasi process termination: hapus korban dari graph."""
#     return {
#         p: [x for x in tujuan if x != korban]
#         for p, tujuan in graph.items() if p != korban
#     }

# macet, siklus = cek_siklus(kasus_macet)
# if macet:
#     korban = siklus[0]   # korban = proses pertama di dalam siklus
#     print(f"\n[Recovery] Menghentikan {korban}")
#     kasus_macet = hentikan_proses(kasus_macet, korban)
#     tampilkan("Kasus 1 setelah recovery", kasus_macet)
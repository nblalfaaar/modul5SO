def cek_aman(available, max_need, allocation):
    n = len(allocation)
    m = len(available)

    need = [[max_need[i][j] - allocation[i][j] for j in range(m)]
            for i in range(n)]

    work = available[:]
    selesai = [False] * n
    urutan_aman = []

    while len(urutan_aman) < n:
        ada_yang_maju = False
        for i in range(n):
            if not selesai[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += allocation[i][j]   # proses selesai, resource kembali
                selesai[i] = True
                urutan_aman.append(i)
                ada_yang_maju = True

        if not ada_yang_maju:
            return False, []

    return True, urutan_aman

available = [3, 3, 2]
max_need = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3],
]
allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2],
]

print("SKENARIO 1: AMAN")
aman, urutan = cek_aman(available, max_need, allocation)
if aman:
    print(f"Aman! Urutan: {urutan}")
else:
    print("Tidak aman!")

print("\nSKENARIO 2: TIDAK AMAN")
available_unsafe = [1, 1, 0]
aman, urutan = cek_aman(available_unsafe, max_need, allocation)
if aman:
    print(f"Aman! Urutan: {urutan}")
else:
    print("Tidak aman! Tidak ada proses yang bisa diselesaikan dengan resource tersedia.")
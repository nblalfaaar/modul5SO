antrean = [98, 183, 37, 122, 14, 124, 65, 67]
kepala = 53
maks = 199

def total(jalur):
    return sum(abs(b - a) for a, b in zip(jalur, jalur[1:]))

def fcfs(q, h):
    return [h] + q

def sstf(q, h):
    jalur, sisa = [h], q[:]
    while sisa:
        terdekat = min(sisa, key=lambda x: abs(x - jalur[-1]))
        jalur.append(terdekat)
        sisa.remove(terdekat)
    return jalur

def scan(q, h):
    bawah = sorted([x for x in q if x < h], reverse=True)
    atas = sorted([x for x in q if x >= h])
    return [h] + bawah + [0] + atas

def cscan(q, h, m):
    atas = sorted([x for x in q if x >= h])
    bawah = sorted([x for x in q if x < h])
    return [h] + atas + [m, 0] + bawah

for nama, jalur in [("FCFS", fcfs(antrean, kepala)),
                    ("SSTF", sstf(antrean, kepala)),
                    ("SCAN", scan(antrean, kepala)),
                    ("C-SCAN", cscan(antrean, kepala, maks))]:
    print(f"{nama:7} total = {total(jalur):3}  jalur: {jalur}")
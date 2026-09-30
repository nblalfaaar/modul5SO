import threading
import time

kunci1 = threading.Lock()
kunci2 = threading.Lock()

def orang_pertama():
    print("[Orang 1] ambil kunci 1")
    kunci1.acquire()
    print("[Orang 1] DAPAT kunci 1")

    time.sleep(2)

    print("[Orang 1] mau ambil kunci 2...")
    kunci2.acquire()
    print("[Orang 1] DAPAT kunci 2")

    kunci2.release()
    kunci1.release()

def orang_kedua():
    print("[Orang 2] ambil kunci 2")
    kunci2.acquire()
    print("[Orang 2] DAPAT kunci 2")

    time.sleep(2)

    print("[Orang 2] mau ambil kunci 1...")
    kunci1.acquire()
    print("[Orang 2] DAPAT kunci 1")

    kunci1.release()
    kunci2.release()

orang1 = threading.Thread(target=orang_pertama, daemon=True)
orang2 = threading.Thread(target=orang_kedua, daemon=True)

orang1.start()
orang2.start()

orang1.join()
orang2.join()

print("Selesai tanpa macet.")  # gak akan pernah tercetak
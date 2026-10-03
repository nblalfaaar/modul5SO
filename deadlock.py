import threading
import time

kunci1 = threading.Lock()
kunci2 = threading.Lock()


def orang_pertama():
    print("[Orang 1] ambil kunci 1")
    kunci1.acquire()
    print("[Orang 1] dapat kunci 1")

    time.sleep(1)

    print("[Orang 1] mau ambil kunci 2...")
    kunci2.acquire()
    print("[Orang 1] dapat kunci 2")

    kunci2.release()
    kunci1.release()


def orang_kedua():
    print("[Orang 2] ambil kunci 2")
    kunci2.acquire()
    print("[Orang 2] dapat kunci 2")

    time.sleep(1)

    print("[Orang 2] mau ambil kunci 1...")
    kunci1.acquire()
    print("[Orang 2] dapat kunci 1")

    kunci1.release()
    kunci2.release()


t1 = threading.Thread(target=orang_pertama, daemon=True)
t2 = threading.Thread(target=orang_kedua, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()

print("Selesai tanpa macet yeyyy.")
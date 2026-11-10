import threading
import time

komputer = threading.Lock()
sesi_uji = threading.Lock()


def mahasiswa_pertama():
    print("[Mahasiswa 1] ambil komputer")
    komputer.acquire()
    print("[Mahasiswa 1] dapat komputer")

    time.sleep(1)

    print("[Mahasiswa 1] mau ambil sesi uji...")
    sesi_uji.acquire()
    print("[Mahasiswa 1] dapat sesi uji")

    sesi_uji.release()
    komputer.release()


def mahasiswa_kedua():
    print("[Mahasiswa 2] ambil sesi uji")
    sesi_uji.acquire()
    print("[Mahasiswa 2] dapat sesi uji")

    time.sleep(1)

    print("[Mahasiswa 2] mau ambil komputer...")
    komputer.acquire()
    print("[Mahasiswa 2] dapat komputer")

    komputer.release()
    sesi_uji.release()


t1 = threading.Thread(target=mahasiswa_pertama, daemon=True)
t2 = threading.Thread(target=mahasiswa_kedua, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()

print("Selesai tanpa macet yeyyy. Deadlock sangatlah mudah bukan.")
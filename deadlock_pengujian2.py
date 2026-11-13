import threading
import time

terminal = threading.Lock()
disk_virtual = threading.Lock()


def mahasiswa_pertama():
    print("[Mahasiswa 1] ambil terminal")
    terminal.acquire()
    print("[Mahasiswa 1] dapat terminal")

    time.sleep(1)

    print("[Mahasiswa 1] mau ambil disk virtual...")
    disk_virtual.acquire()
    print("[Mahasiswa 1] dapat disk virtual")

    disk_virtual.release()
    terminal.release()


def mahasiswa_kedua():
    print("[Mahasiswa 2] ambil disk virtual")
    disk_virtual.acquire()
    print("[Mahasiswa 2] dapat disk virtual")

    time.sleep(1)

    print("[Mahasiswa 2] mau ambil terminal...")
    terminal.acquire()
    print("[Mahasiswa 2] dapat terminal")

    terminal.release()
    disk_virtual.release()


t1 = threading.Thread(target=mahasiswa_pertama, daemon=True)
t2 = threading.Thread(target=mahasiswa_kedua, daemon=True)

t1.start()
t2.start()
t1.join()
t2.join()

print("Selesai tanpa macet yeyyy. Deadlock sangatlah mudah bukan?")
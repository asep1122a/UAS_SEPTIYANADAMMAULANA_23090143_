
from Soal_3_Modul import Antrian

class SistemAntrianRestoran:
    def __init__(self):
        self.antrian = Antrian()

    def tambah_pesanan(self, pesanan):
        self.antrian.enqueue(pesanan)
        print(f"Pesanan '{pesanan}' ditambahkan ke antrian.")

    def proses_pesanan(self):
        pesanan = self.antrian.dequeue()
        if pesanan:
            print(f"Memproses pesanan '{pesanan}'...")
        else:
            print("Tidak ada pesanan di antrian.")

    def tampilkan_antrian(self):
        print("Antrian saat ini:")
        print(self.antrian)

def main():
    sar = SistemAntrianRestoran()

    while True:
        print("\nSistem Antrian Restoran")
        print("1. Tambah pesanan")
        print("2. Proses pesanan")
        print("3. Tampilkan antrian")
        print("4. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            pesanan = input("Masukkan pesanan: ")
            sar.tambah_pesanan(pesanan)
        elif pilihan == "2":
            sar.proses_pesanan()
        elif pilihan == "3":
            sar.tampilkan_antrian()
        elif pilihan == "4":
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
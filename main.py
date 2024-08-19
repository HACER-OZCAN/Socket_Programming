import threading
import socket

SIZE = 50               # veri boyutu
SERVER = 'localhost'    #hangi agdan haberlesecez
PORT = 52369          #port numarasi 1000 den hatta 3000 den yukarıda bir sayı seçmeye çalis
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ip versiyon, protokol tipi (IPv4, TCP)
# eğer IPv6 kullanırsan=AF_INET6 , UDP kullanırsan= SOCK_DREAM
server.bind(ADDR)   # serveri bağlar. host AF_INET ile SOCK_STRAM PORT ile eşleşir


def istemci(baglanti, addr):
    kontrol = True
    print("[BAGLANAN] {} ile baglantı kuruldu".format(addr))
    while kontrol:
        mesaj = baglanti.recv(SIZE).decode()    #gelen mesajı metne dönüstur
        if mesaj != '':
            print(f"[{addr}] mesaj: ", mesaj)
            send = 'True' + (''*46)
            baglanti.send(send.encode())

        if mesaj == "q":    #q ya basinca cıkmayı sagliyor
            print("cikiliyor")
            kontrol = False

    baglanti.close()

def main():
    print(f"[DİNLEME] server {ADDR} adresini dinliyor")
    while True:
        server.listen()
        baglanti, addr = server.accept()

        threading.Thread(target=istemci, args=(baglanti, addr)).start()
        #t.start
        #istemci(baglanti, addr)

main()


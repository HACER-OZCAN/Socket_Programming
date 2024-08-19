import threading
import socket

SIZE = 50
SERVER= 'localhost' #server ile aynı agda olmasi gerekiyor
PORT = 52369
ADDR= (SERVER, PORT)

istemci = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #sever ile uygun yapida olmasi lazım
istemci.connect(ADDR)       # server ila baglantı kuruluyor

def send():
    while True:
        metin = input("[client] veri girin: ")
        metin_uzunluk = len(metin)
        istemci.send(metin.encode() + (b'' * ((SIZE) - (metin_uzunluk))))
        yazma = istemci.recv(SIZE)
        print("[veri girisi] mesaj yaziniz: {}".format(yazma))
        #return gonderilen_veri
        secim= input("cimak icin * a, devam etmek icin başka bi tusa basiniz ")
        if secim == '*':
            break


send()
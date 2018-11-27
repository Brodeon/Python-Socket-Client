import socket
from threading import Thread
import tkinter as tk

global active
active = True

HOST = '127.0.0.1'
PORT = 5002

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObject.connect((HOST, PORT))


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(ipadx=200, ipady=200)
        self.createWidgets()

    #Wysyłanie wiadomości do serwera
    def OnSendClicked(self):
        socketObject.send(b'wiadomosc z klienta')

    def createWidgets(self):
        self.Button1 = tk.Button(self, text='Send', bg='white', command=self.OnSendClicked)
        self.Button1.place(x=120, y=50)

root = tk.Tk()
aplikacja = Application(master=root)

#Wątek nasłuchujący danych przychodzących z serwera
def receive():
    print("Receiving is starting")
    while active:
        message = socketObject.recv(1024)
        print(message)

#Aktywacja wątku
receiveThread = Thread(target=receive)
if (receiveThread.is_alive() == False):
    receiveThread.start()

aplikacja.mainloop()

active = False
if(receiveThread.is_alive() == True):
    receiveThread.join()
del receiveThread


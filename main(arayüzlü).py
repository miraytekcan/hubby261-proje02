import time
from getURL import GetURL
from dataURL import DataURL

useDataURL = DataURL()
useGetURL = GetURL()

print("-: Miray Mini Örümceğine Hoş Geldiniz! :")
print("|------------------------------|")
print("")
time.sleep(2)

import tkinter as tk
from getURL import GetURL
from dataURL import DataURL
import time

useDataURL = DataURL()
useGetURL = GetURL()

# Pencere oluştur
window = tk.Tk()

def button1_clicked():
    useDataURL.dataRead()

def button2_clicked():
    useDataURL.dataWrite()

def button3_clicked():
    useGetURL.getWeb()

def button4_clicked():
    useGetURL.getList()

def button5_clicked():
    print("Program kapatılıyor...")
    window.destroy()

button1 = tk.Button(text="URL Listele", command=button1_clicked)
button1.pack()
button2 = tk.Button(text="URL Ekle", command=button2_clicked)
button2.pack()
button3 = tk.Button(text="Örümcek Gönder", command=button3_clicked)
button3.pack()
button4 = tk.Button(text="Sonuçları Listele", command=button4_clicked)
button4.pack()
button5 = tk.Button(text="Çıkış", command=button5_clicked)
button5.pack()

window.mainloop()



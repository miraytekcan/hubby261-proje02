import time
import urllib.request
from bs4 import BeautifulSoup
import os
from getURL import GetURL
from dataURL import DataURL
from tkinter import *
from tkinter import ttk

useDataURL = DataURL()
useGetURL = GetURL()

while True:

    pencere = Tk()
    pencere.title("Miray Mini Örümceği")
    pencere.geometry("750x250")

    def entry_update(text):
        entry.delete(0, END)
        entry.insert(0, text)

    entry = Entry(pencere, width=30, bg="white")
    entry.pack(pady=10)

    button_dict = {}
    option = ["Çıkış", "URL Listele", "URL Ekle", "Örümcek Gönder", "Sonuçları Listele"]

    for i in option:
        def func(x=i):
            quit, useDataURL.dataRead(), useDataURL.dataWrite(), useGetURL.getWeb(), useGetURL.getList()

        button_dict[i] = ttk.Button(pencere, text=i, command=func)
        button_dict[i].pack()
    pencere.mainloop()


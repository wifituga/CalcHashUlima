from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from index import MD5
import tkinter as tk
import hashlib
import os
window = tk.Tk()

window.title("HashCalc MD5 | E1 | RdC")
window.geometry("550x200")
window.iconbitmap("ulima.ico")

var1 = IntVar()
var2 = IntVar()


def whion():
    if (var1.get() == 1):
        hashing_md5()
    elif (var1.get() == 0):
        return 0
    if (var2.get() == 1):
        hashing_sha256()
    elif (var2.get() == 0):
        return 0
    if (var1.get() and var2.get() == 1):
        hashing()


def hashing():
    if (formato.get() == "Texto"):
        md5_hash = MD5.hash(input_txt.get())
        label_MD5 = tk.Label(width=57, bg="White",
                             text=md5_hash, borderwidth=2)
        label_MD5.place(x=120, y=80)

        sha256 = hashlib.sha256()
        contenido = input_txt.get()
        sha256.update(contenido.encode('utf-8'))

        label_SHA256 = tk.Label(width=60, bg="White",
                                text=sha256.hexdigest(), borderwidth=2)
        label_SHA256.place(x=100, y=110)

    elif(formato.get() == "Archivo"):
        file = r'ulima.ico'
        md5 = hashlib.md5()
        with open(file, 'rb') as archivo:
            contenido = archivo.read()
            md5.update(contenido)

            label_MD5 = tk.Label(width=57, bg="White",
                                 text=md5.hexdigest(), borderwidth=2)
            label_MD5.place(x=120, y=80)

        file = r'ulima.ico'
        sha256 = hashlib.sha256()
        with open(file, 'rb') as archivo:
            contenido = archivo.read()
            sha256.update(contenido)

            label_SHA256 = tk.Label(
                width=60, bg="White", text=sha256.hexdigest(), borderwidth=2)
            label_SHA256.place(x=100, y=110)


def hashing_md5():
    if (formato.get() == "Texto"):
        md5_hash = MD5.hash(input_txt.get())
        label_MD5 = tk.Label(width=57, bg="White",
                             text=md5_hash, borderwidth=2)
        label_MD5.place(x=120, y=80)

    elif(formato.get() == "Archivo"):
        file = r'ulima.ico'
        md5 = hashlib.md5()
        with open(file, 'rb') as archivo:
            contenido = archivo.read()
            md5.update(contenido)

            label_MD5 = tk.Label(width=57, bg="White",
                                 text=md5.hexdigest(), borderwidth=2)
            label_MD5.place(x=120, y=80)


def hashing_sha256():
    if (formato.get() == "Texto"):
        sha256 = hashlib.sha256()
        contenido = input_txt.get()
        sha256.update(contenido.encode('utf-8'))

        label_SHA256 = tk.Label(width=60, bg="White",
                                text=sha256.hexdigest(), borderwidth=2)
        label_SHA256.place(x=100, y=110)

    elif(formato.get() == "Archivo"):
        file = abrir_archivo()
        sha256 = hashlib.sha256()
        with open(file, 'rb') as archivo:
            contenido = archivo.read()
            sha256.update(contenido)

            label_SHA256 = tk.Label(
                width=60, bg="White", text=sha256.hexdigest(), borderwidth=2)
            label_SHA256.place(x=100, y=110)

def abrir_archivo():
    archivo_abierto = filedialog.askopenfilename(initialdir="/",
                                                 title="...", filetypes=((".jpg", ".txt"), ("all files", "*.*")))
def carpeta():
    directorio = filedialog.askdirectory()
    if directorio !="":
        os.chdir(directorio)
    print(os.getcwd())
    
recgen = tk.Frame(window, width=535, height=185,
                  borderwidth=1.5, bg="Light grey", relief="solid")
recgen.place(x=8, y=8)

formato = ttk.Combobox(
    state="readonly",
    values=["Archivo", "Texto"],
    width=7
)
formato.set("Texto")

formato.place(x=25, y=40)

input_txt = tk.Entry(width=65, borderwidth=1.5)
input_txt.place(x=100, y=40)

# Texto
formato_data = tk.Label(text="Formato:", background="Light grey")
formato_data.place(x=25, y=19)

Data = tk.Label(text="Data:", background="Light grey")
Data.place(x=100, y=19)
# ----------------------------------------------------------------------------- #

# Parte MD5
MD5_check = tk.Checkbutton(text="MD5", bg="Light grey",
                           variable=var1, onvalue=1, offvalue=0)
MD5_check.place(x=25, y=80)

label_MD5 = tk.Label(width=60, bg="White", borderwidth=2)
label_MD5.place(x=100, y=80)
# ----------------------------------------------------------------------------- #

# Parte SHA256
SHA256_check = tk.Checkbutton(
    text="SHA256", bg="Light grey", variable=var2, onvalue=1, offvalue=0)
SHA256_check.place(x=25, y=110)

label_SHA256 = tk.Label(width=60, bg="White", borderwidth=2)
label_SHA256.place(x=100, y=110)
# ----------------------------------------------------------------------------- #

Calc_button = tk.Button(text="Calcular", command=whion, bg="White")
Calc_button.place(x=465, y=160)

File_button = tk.Button(text="...", bg="white", command=abrir_archivo)
File_button.place(x=508, y=40)

window.mainloop()

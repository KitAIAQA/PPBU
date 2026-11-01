from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests



def update_currency_label(event):
    pass


def update_base_label(event):
    pass


def update_base2_label(event):
    pass


def exchange():
    pass


currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'RUB': 'Российский рубль',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курсы обмена валют')
root.geometry('360x300')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label(root)
base_label.pack()

Label(root, text='Вторая базовая валюта').pack()
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base2_combobox.pack(pady=3, padx=10)
base2_combobox.bind('<<ComboboxSelected>>', update_base2_label)
base2_label = ttk.Label(root)
base2_label.pack()

Label(root, text='Целевая валюта').pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)
target_label = ttk.Label(root)
target_label.pack()

Button(root, text='Получить курс обмена',
       command=exchange).pack(pady=10, padx=10)

root.mainloop()
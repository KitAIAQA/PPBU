from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
from tkmacosx import Button  # спец библиотека, которая обходит ограничения macOS, ставит любой цвет фона у кнопки



def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)


def update_base2_label(event):  # вторая валюта
    code = base2_combobox.get()
    name = currencies[code]
    base2_label.config(text=name)


def exchange():
    target_code = target_combobox.get().strip()
    base_code = base_combobox.get().strip()
    base2_code = base2_combobox.get().strip()  # вторая валюта
    if target_code and base_code and base2_code:  # вторая валюта
        try:
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response1.raise_for_status()
            data1 = response1.json()
            response2 = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}')  # вторая валюта
            response2.raise_for_status()  # вторая валюта
            data2 = response2.json()  # вторая валюта
            if target_code in data1['rates'] and target_code in data2['rates']:  # вторая валюта
                exchange_rate = data1['rates'][target_code]
                exchange_rate2 = data2['rates'][target_code]  # вторая валюта
                base = currencies[base_code]
                base2 = currencies[base2_code]  # вторая валюта
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс: {exchange_rate:.1f} {target} за 1 {base}\n'
                                     f'Курс: {exchange_rate2:.1f} {target} за 1 {base2}')  # вторая валюта
            else:
                mb.showerror('Ошибка',
                             f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', f'Ошибка: {er}')
    else:
        mb.showwarning('Внимание', 'Введите коды валют')


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

Button(root, text='Получить курс обмена', bg='#467ef0', fg='white',
       command=exchange).pack(pady=10, padx=10)

root.mainloop()

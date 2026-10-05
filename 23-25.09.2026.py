# def sumr(a, y):
#     global x
#     z = 12
#     z += 3
#     print('x =', x, y, 'z=', z)
#     return x

# z = 1000
# x = 5000
# res = sumr(10, 20)
# print(res)
# print('X =', x, 'Z =', z)
#
#
# def is_eval(n) -> bool:
#     """опредеояет четность числа
#     is_eval(2) -> True
#     is_eval(3) -> False"""
#     pass
#
#     return n % 2 == 0
#
# print(is_eval.__doc__)
#
# def choice_eval(x: int, y: int) -> None:
#     """Выбирает четные числа из последоваткоьности"""
#     for i in range(x, y + 1) :
#         if is_eval(i):
#             print(i, end=' ')


# for n in range(100, 200):
#     for i in range(2, n):
#         if n % i == 0:
#             break
#     else:
#         print(n, end=' ')








# def num2(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)
#
#
# def num1(n: int) -> None:
#     if n > 1:
#         num2(n - 1)
#     print(n)


# def num(n: int) -> None:
#     if n > 1:
#         num1(n - 1)
#     print(n)
#
# num(15)



"""
3! = 1 * 2 * 3 = 3 * 2!
2! = 1 * 2     = 2 * 1!
1! = 1
n! = n * (n-1)!
"""

# def fact(n: int) -> int:
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))

# def name(nm):
#     cnt = 1
#     def surname(snm):
#         nonlocal cnt
#         cnt += 1
#         print(cnt, nm, snm)
#     return surname

#name('Mary')('Petrova')

# sir = name('Mary')
# sir('Petrova')
# sir('Андреева')
# sir('Sidorova')

#-------------------tkinter----базовые виджеты некоторые-------------------25.09.2026

from tkinter import *


# def answer(event=None):  # если пишем присвоить по умолчанию (event=None) то аргументы в параметр не передаем
# если передаем то пишем (event)
#     answ = num.get().strip()
#     result.configure(text=answ)
#
# root = Tk()
# root.title('Старт')
# WIDTH = root.winfo_screenwidth()
# HEIGHT = root.winfo_screenheight()
# X = 300
# Y = 130
##print(WIDTH, HEIGHT)
# root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
#               f"+{HEIGHT // 2 - Y // 2 - 25}")
##root.geometry('300x100+400+200')

# prompt = Label(text='Введите значение', font='Arial 12')
# prompt.pack()

##prompt.pack(side=TOP)
##prompt.pack(side=LEFT)
##prompt.pack(side=RIGHT)
##prompt.pack(side=LEFT)
##prompt.pack(side=BOTTOM)

# num = Entry(width=5, font='Arial 12', justify='center')
# num.pack()
#
# result = Label(text='    ', font='Arial 15', bg = 'lightgray')
# result.pack(pady=10)
#
# btn = Button(text='Выполнить', command=answer)  # вызываем command= функцию answer
# btn.pack()
#
# num.bind('<Return>', answer)
#
# root.mainloop()




#----------изучаем-библиотеку-datetime-"дейтайм"----------------------------------------------------------------------
# from datetime import datetime, date, time, timedelta
## datetime это один тип данных, date, time, timedelta- тоже разные для операций со временем

# d = date(2024, 12, 31)  # порядок важен!! гггг, мм, дд (тут определяем дату не получаем)
# t = time(12, 31, 16)  # порядок важен!! чч, мм, сс
# print(d, type(d))  # 2024-12-31 <class 'datetime.date'> (дата в международном формате)
# print(t, type(t))  # 12:31:16 <class 'datetime.time'>
## нельзя сделать dt = d + t !!!
# dt = datetime.combine(d, t) # метод комбинирует дату и время
# print(dt, type(dt))  # 2024-12-31 12:31:16 <class 'datetime.datetime'>
# d = date.today()  # получить дату
# print(d, type(d))  # 2026-10-04 <class 'datetime.date'> (сегодняшняя дата)
# dt = datetime.now()  # берет поясное время из биос(на маке аппаратные часы в ядре, которые сверяются по сети)
# print(dt)  # 2026-10-04 23:26:50.911360 (с микросекундами)
# print(dt.time())  # 23:26:50.911360 (из dt вывели только время) обратились к объекту dt
# dt = datetime.now().replace(microsecond=0)  # реплейсом убираем микросекунды
# print(dt.time())  # 23:30:32  (на принт вывели только time без date)
# dt = datetime.now().replace(microsecond=0)  # соответственно выводим и дату и время
# print(dt)  # 2026-10-04 23:55:11
# dt = dt.replace(year=2020, month=10, day=30, hour=10, minute=30, second=30)  # делаем замену
# print(dt)  # 2020-10-30 10:30:30

# dtt = input('Введите дату (дд.мм.гггг): ')  # Введите дату (дд.мм.гггг): 20.10.2000  (будет тип строка)
# print(dtt, type(dtt))  # 20.10.2000 <class 'str'>
# datte = datetime.strptime(dtt, '%d.%m.%Y')  # введеное нами преобразуется в формат %d.%m.%Y(директивы strptime)
# print(datte, type(datte))  # 2000-10-20 00:00:00 <class 'datetime.datetime'>
##(!!переставилось местами как на международный формат по умолчанию потому что не указали парсер strptime)
# print(datte.date())  # 2000-10-20 (в международном формате по умолчанию потому что не указали парсер strptime)
# print(datte.strftime('%d.%m.%Y'))  # 20.10.2000 (ровно по обозначенным %d.%m.%Y с парсингом)
# print(datte.strftime('%A %d.%B.%Y %I:%M%p'))  # Friday 20.October.2000 12:00AM
# print(datte.strftime('%d.%m.%Y %X'))  # 20.10.2000 00:00:00
# print(datte.strftime('%d.%m.%Y %H:%M'))  # 20.10.2000 00:00

# dt = datetime.now().replace(microsecond=0)  # берем сегодняшнюю дату без микросекунд
# dtt = dt.timetuple()  # создаст кортеж 'таймтьюпл'
# print(dtt)  # time.struct_time(tm_year=2026, tm_mon=10, tm_mday=5, tm_hour=9, tm_min=53, tm_sec=57, tm_wday=0, .....
# for i in dtt:  # удобнее рассмотреть через цикл
#     print(i)  # ниже вывод
##= 2026
##= 10
##= 5
##= 9
##= 56
##= 54
##= 0   (tm_wday 0 это понедельник, 1 вторник, 2 среда....)
##= 278  (tm_yday по счету день в году)
##= -1   (обозначает что нет перехода на зимнее/летнее время)

# dt = datetime.now().replace(microsecond=0)  # берем сегодняшнюю дату без микросекунд
# dt = dt.isocalendar()
# print(dt)  # datetime.IsoCalendarDate(year=2026, week=41, weekday=1)  (41я неделя сейчас, 1й день недели пн)
##weekday можем использовать как с 0 так и с 1

# dt = datetime.now().replace(microsecond=0)  # берем сегодняшнюю дату без микросекунд
# print(dt.weekday())  # 0
# print(dt.isoweekday())  # 1 (пн по стандарту iso, отсчет с вс)
# days = ('Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс')  # задаем кортеж
##в библиотеке datetime нет русских обозначений недели
# print(days[dt.weekday()])  # Пн   (обращаемся к days из него вытаскиваем индекс [dt.weekday()] )

# расчитать кол-во дней до дня рождения:
# birthday = input('Введите дату рождения ("дд.мм.гггг"): ')  # вводим когда родились 10.3.1817
# birthday = datetime.strptime(birthday, '%d.%m.%Y').date()  # переводим в datetime только date 1817-03-10
# dt_now = date.today()  # получаем сегодняшнюю дату
# year_ = dt_now.year  # получаем этот год 2026
# birthday = birthday.replace(year=year_)  # заменяем в дате рождения год на сегодняшний 2026-03-10
# print(birthday, dt_now, year_)  # 2026-03-10 2026-10-05 2026
# if birthday < dt_now:  # если наш др меньше сегодняшней даты(т.е. прошло) (2026-03-10 < 2026-10-05) если нет то res
#     birthday = birthday.replace(year=year_ + 1)  # +1 к году если др уже прошло и дальше res
# res = birthday - dt_now  # (2027-03-10 минус 2026-10-05 равно до др 156 days, 0:00:00)
# if res.days == 0:  # если день и месяц как сегодня
#     print(f'С днём рождения!!!')
# else:
#     print(f'До Вашего дня рождения {res.days} дн.')  # До вашего дня рождения 156 дн.  (.days чтобы только день вывел)


#-------БУДИЛЬНИК-(скопировала в отдельный .ру без комментов для конвертации в .app)-------------------------------------------------------------

from tkinter import *  # подготавливаем среду
from tkinter import messagebox as mb  # прописываем сокращение
import time  # библиотека
import pygame as pg  # прописываем сокращение, библиотека для звучания музыки в будильник

pg.mixer.init()  # инициируем запуск метода mixer из pygame(pg)
pg.mixer.music.load('music.mp3')  # загружаем наш файл с музыкой


def tick():  # обозначаем функцию в ней делаем чтоб время сменялось каждую секунду
    global time_alarm
    current_time = time.strftime("%H:%M:%S")  # получаем настоящее время из библиотеки time
    if (time_alarm == current_time("%X") or  # условие когда время текущее совпадает с временем будильника
            time_alarm == time.strftime("%H:%M") or
            time_alarm == time.strftime("%H")):
        time_alarm = ''  # сбрасывается когда песня доиграет до конца
        pg.mixer.music.play()  # вызываем музыкальную композицию (запуск метода mixer из pygame(pg))
    screen_time.after(1000, tick)  # чтобы снять время прописываем задержку в 1 секунду(1000 милисекунд), мы видим
    ##движение секунд, рекурсия не кладется в стек, каждый вызов закончен, память не занимается
    screen_time.config(text=current_time)  # берем наш лейбл screen_time(время на экране) и присваеваем тексту


def on_click():  # обозначаем функцию ВКЛючить будильник
    global time_alarm  # указываем что time_alarm глобальная переменная и мы её изменяем ниже
    time_alarm = entry_time.get().strip()  # strip потому что у нас поле шире чем мы можем вводить(убрать пустоты)

    mb.showinfo('Включение будильника',  # берем библиотеку и метод, пишем заглавие окна(это всплывающее окно)
                f'Будильник включен на {time_alarm}')  #как уведомление


def off_click():  # обозначаем функцию ВЫКЛючить будильник
    global time_alarm
    time_alarm = ''  # сбрасываем(на кнопку) когда выключаем будильник
    entry_time.delete(0, END)  # удалить очистить поле, entry_time- поле ввода
    pg.mixer.music.stop()  # останавливаем музыкальную композицию (запуск метода mixer из pygame(pg))

    mb.showwarning('Выключение будильника',  # другой метод(всплывающее окно)
                f'Будильник выключен')


##прописываем общую переменную чтобы включить функцию(время)
time_alarm = ''

root = Tk()  # root это окно (с англ корень- главное окно)
root.title('Будильник')  # название окошка
root.config(background='black')  # весь фон в окне черным

# геометрия окна
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 210
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
              f"+{HEIGHT // 2 - Y // 2 - 25}")

##прописываем лейбл screen_time (время на экране)
screen_time = Label(root, text='00:00:00', font='Arial 50')  # отображение циферблата
screen_time.config(bg='black', fg='lime')  # фон у чисел черный, цифры зеленые
screen_time.pack()  # с помощью менеджера pack разместили в окне по центру вверху

##окно-поле для ввода будущего времени срабатывания будильника, width- ширина кол-во символов
##в него напрямую ничего положить нельзя работает с insert и delite (методы заполнения)
entry_time = Entry(root, width=10, font='Arial 20', justify=CENTER)  # root значит в окне
entry_time.pack()

on = Button(root, text='Включить', font=('Arial', 10), command=on_click)  # призываем функцию on_click
on.pack(pady=10)  # отступ по оси у 10 пикселей (между кнопкой и отображением времени)
##записывать можно и font='Arial 20' и font=('Arial', 10)

off = Button(root, text='Выключить', font=('Arial', 10), command=off_click)  # призываем функцию off_click
off.pack()  # написанный у on отступ и сюда распространится

tick()  # вызываем функцию из начала про текущее время

root.mainloop()
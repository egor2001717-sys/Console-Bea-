import time, random
from tkinter import*
print("Попробуйте новую облочку комманд языка Bea++ введите help() для списка комманд")
while True:
    a = input("---")
    if a == "text()":
        b = input("Какой текст вы хотели вывести")
        if b == b:
            print("(T)")
            time.sleep(3)
            print(b)
    elif a == "randomint()":
        c = int(input("Меньшее число"))
        time.sleep(1)
        d = int(input("Большое число"))
        if c == c and d ==d:
            print("(12?)")
            time.sleep(3)
            print(random.randint(c, d))
    elif a == "getwindow(tk)":
        print("[* ]")
        time.sleep(3)
        w = Tk()
        w.mainloop()
    elif a == ".afk=console()":
        print("(x)")
        time.sleep(3)
        break
    elif a == "help()":
        print("Список команд text() - Выводит текст \n randomint() - Выводит случайное указанное число \n getwindow(tk) - Включает окно \n .afk=console() - Выключает программу \n argum = - Выводит значение только оставте его пустым нажмите enter и нужно ответить на вопрос \n makeapp() - Включает навык создания приложений \n app.label() - Создаёт текстовое поле в приложении незабудьте написать makeapp() \n button.title() - Название кнопки в приложении незабудьте написать makeapp() \n onbuttontouch(label.config()) - Указывает что будет при нажатии кнопки незабудьте написать makeapp()")
    elif a == "argum =":
        e = input("Значение")
        if e == e:
            print(e)
    elif a == "makeapp()":
        time.sleep(1)
        m2 = input("Текст в приложении app.label("")")
        time.sleep(1)
        m3 = input("Название кнопки button.title("")")
        time.sleep(1)
        m4 = input("На какой текст изменяет кнопка при нажатии onbuttontouch(label.config(""))")
        print("[app]")
        print("Проверьте окна консоли оно может появится не на экране а в окнах консоли Bea++ в свёрнутом виде")
        time.sleep(3)
        w = Tk()
        l = Label(w, text=m2)
        b = Button(w, text=m3)
        def change(event):
            l.config(text=m4)
        b.bind("<Button-1>", change)
        l.pack()
        b.pack()
        w.mainloop()
        time.sleep(1)
    else:
        print("Ошибка неизвестная комманда или неправильно написаная")


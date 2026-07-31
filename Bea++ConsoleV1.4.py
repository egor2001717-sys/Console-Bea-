import time, random
from tkinter import*

print("Попробуйте новую оболочку команд языка Bea++ введите help() для списка команд")

while True:
    a = input("---")
    
    if a == "text()":
        b = input("Какой текст вы хотели вывести? ")
        print("(T)")
        time.sleep(3)
        print(b)
        
    elif a == "randomint()":
        try:
            c = int(input("Меньшее число: "))
            time.sleep(1)
            d = int(input("Большое число: "))
            print("(12?)")
            time.sleep(3)
            print(random.randint(c, d))
        except ValueError:
            print("Ошибка! Компьютер не может выполнить команду, так как вместо числа вы ввели текст.")
            
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
        print("Список команд:\n text() - Выводит текст\n randomint() - Выводит случайное указанное число\n getwindow(tk) - Включает окно\n .afk=console() - Выключает программу\n argum = - Выводит значение\n makeapp() - Включает навык создания приложений\n worldmap() - Запускает навык создания карт\n for argum in (int1+int2) give text(argum) - Считает от указанного число до другово")
              
    elif a == "argum =":
        e = input("Значение: ")
        print(e)
        
    elif a == "makeapp()":
        time.sleep(1)
        m2 = input("Текст в приложении app.label: ")
        time.sleep(1)
        m3 = input("Название кнопки button.title: ")
        time.sleep(1)
        m4 = input("На какой текст изменяет кнопка при нажатии: ")
        print("[app]")
        print("Проверьте окна консоли, оно может появиться в свёрнутом виде")
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
        
    elif a == "worldmap()":
        wm1 = input("Линия из земли как будет выглядеть, какой символ - ")
        time.sleep(1)
        wm2 = input("Как будет выглядеть дерево - ")
        print(wm1, wm1, wm1, wm2, wm1, "Карта мира")
    elif a == "for argum in (int1+int2) give text(argum)":
        try:
            aqq = int(input("int1 "))
            time.sleep(1)
            aqqq = int(input("int2 "))
            for intrun in range(aqq, aqqq):
                print(intrun)
                time.sleep(0.1)
        except ValueError:
            print("Ошибка! Компьютер не может выполнить команду, так как вместо числа вы ввели текст.")
            continue
        if aqqq>=300:
            print("ВЫ ПЕРЕВЫСИЛИ ЗНАЧЕНИЕ 300 ЗАПУСК НЕВОЗМОЖЕН КОНСОЛЬ МОГЛА ЗАВИСНУТЬ!")
    else: 
        print("Ошибка! Неизвестная команда или неправильно написанная.")

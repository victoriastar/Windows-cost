###Определение цены окон в зависимости от пожеланий клиента
###Для округления в большую сторону подключаем стандартный модуль match
import math

#Формула для рассчета стоимости окон
#От выбора профиля формула для расчета не меняется, следовательно выбранный профиль при расчете не учитываем
def GetWindowCost(wCasement, wFittings, lr, ss, ls):    
    errorText = "При расчете произошла ошибка. Пожалуйста, перезапустите программу."  

    if wCasement == "2":
        if wFittings == "1":
            wFittingsCost = 708
        elif wFittings == "2":
            wFittingsCost = 1237
        else:
            print(errorText)
        cost = (lr * ss * 2053) + ((lr + ss) * 2 * 487) + ((ss + ls) * 539) + (ss * 735) + wFittingsCost        
    elif wCasement == "3":
        if wFittings == "1":
            wFittingsCost = 457
        elif wFittings == "2":
            wFittingsCost = 987
        else:
            print(errorText)
        cost = (lr * ss * 2993) + ((lr + ss) * 2 * 588) + ((ss + ls) * 644) + (ss * 870) + wFittingsCost
    else:
        print(errorText)
    
    return math.ceil(cost)


#Определение пожеланий клиента и рассчет стоимости
def FinalWindowCost():   
    #Выбор профиля
    while True:
        wProfile = input("Какой оконный профиль вы бы хотели:(1 - IVAPER / 2 - REHAU)\n")
        if wProfile == "1" or wProfile == "2":
            break
        else:
            print("Введено некорректное значение. Пожалуйста, введите индекс профиля из предложенных!\n")

    #Выбор количества створок        
    while True:
        wCasement = input("Сколько створок будет у вашего окна: (2 / 3)\n")
        if wCasement == "2" or wCasement == "3":
            break
        else:
            print("Введено некорректное значение. Мы устанавливаем только 2х или 3х створчатые окна!\n")

    #Выбор фурнитуры
    while True:
        wFittings = input("Какая фурнитура вам нужна: (1 - поворотная / 2 - поворотно-откидная)\n")
        if wFittings == "1" or wFittings == "2":
            break
        else:
            print("Введено некорректное значение. Пожалуйста, выберите из предложенного!\n")

    #Выбор длины рамы
    while True:
        if wCasement == "2":
            start = 1.3
            end = 1.51
        else:
            start = 1.71
            end = 2.08        
        lr = input("Введите длину рамы (м): (от {0} до {1})\n\n".format(start, end))
        try:
            if float(lr) >= start and float(lr) <= end:
                break
            else:
                print("Пожалуйста, укажите значение из предложенного диапазона!\n")
        except ValueError:
            print("Введено некорректное значение. Пожалуйста, укажите числовое значение из предложенного диапазона!\n")

    #Выбор ширины створки
    while True:    
        ss = input("Введите ширину створки (м): (от 1.4 до 1.56)\n")
        try:
            if float(ss) >= 1.4 and float(ss) <= 1.56:
                break
            else:
                print("Пожалуйста, укажите значение из предложенного диапазона!\n")
        except ValueError:
            print("Введено некорректное значение. Пожалуйста, укажите числовое значение из предложенного диапазона!\n")

    #Выбор длины створки
    while True:    
        ls = input("Введите длину створки (м): (от 0.4 до 0.9)\n")
        try:
            if float(ls) >= 0.4 and float(ls) <= 0.9:
                break
            else:
                print("Пожалуйста, укажите значение из предложенного диапазона!\n")
        except ValueError:
            print("Введено некорректное значение. Пожалуйста, укажите числовое значение из предложенного диапазона!\n")

    #Рассчет стоимости
    finalCost = GetWindowCost(wCasement, wFittings, float(lr), float(ss), float(ls))
    return finalCost
       
            
#Main
print("Добро пожаловать в оконную мастерскую! Лучшие окна за минимальную цену!\n"
      "Для рассчета примерной стоимости ответьте на несколько вопросов.\n"
      "Внимание!!! При вводе дробных чисел используйте символ '.'\n")

if __name__ == '__main__':
    run = True
    while run:
        wCost = FinalWindowCost()
        print("Стоимость окон согласно указанным параметрам составляет {0} рублей.\n".format(wCost))
        while True:
            answer = input("Рассчитать заново? (1 - да / 2 - нет)\n")
            if answer == "1":
                break
            elif answer == "2":
                run = False
                break
            else:
                print("Введено некорректное значение. Пожалуйста, выберите из предложенного!\n")            
    
    



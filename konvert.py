week = {1:"Понедельник", 2:"Вторник", 3:"Среда", 4:"Четверг", 5:"Пятница", 6:"Суббота", 7:"Воскресенье"}

try:
    d=int(input("Введите номер дня недели: "))
    if d<=7 and d>0: print (week[d])
    else:
         print   ("Вы ошиблись. Попробуйте снова.")
       
except ValueError:
    print ("Вы ошиблись. Попробуйте снова.")
    




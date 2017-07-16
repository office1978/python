# -*- encoding: utf-8 -*-
month_ru = {"январь":1, "февраль":2, "март":3, "апрель":4, "май":5,
         "июнь":6, "июль":7, "август":8, "сентябрь":9,
         "октябрь":10, "ноябрь":11, "декабрь":12}
month_en = {"january":1, "february":2, "march":3, "april":4, "may":5,
         "june":6, "july":7, "august":8, "september":9,
         "october":10, "november":11, "december":12}
d=(input("Введите название месяца: ")).lower()
if month_ru.get(d) or month_en.get(d):
    if 'а' <= d[0] <= 'я':
        print(month_ru.get(d))
    else:
        print(month_en.get(d))
else:
    print ("Такого месяца нет.")


    




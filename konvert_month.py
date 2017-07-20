# -*- encoding: utf-8 -*-
year = {1:["январь","january"], 2:["февраль","february"], 3:["март", "march"], 4:["апрель", "april"], 5:["май", "may"],
         6:["июнь","june"], 7:["июль", "july"], 8:["август", "august"], 9:["сентябрь", "september"],
         10:["октябрь", "october"], 11:["ноябрь", "november"], 12:["декабрь", "december"]}

d=input("Введите название месяца: ").lower()

for k,v in year.items():
    if d in v:
        print (k)
        





    


    




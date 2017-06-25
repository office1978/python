# -*- encoding: utf-8 -*-
d = {}
with open("C:\\Users\\admin\\Desktop\\hosts.txt") as file:
    for line in file:
        key, value = line.split()
        d[key] = value
        
print (d)
file.close()

f = open ("C:\\Users\\admin\\Desktop\\hosts.txt", "a")
l = "\n"+input("Введите ip host: ")
f.writelines(l)
f.close()


s= input ("Введите строку для поиска: ")
with open("C:\\Users\\admin\\Desktop\\hosts.txt") as file:
    for line in file:
        if s in line:
            print (line)











        







    




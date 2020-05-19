# -*- coding: utf-8 -*-
"""
Created on Sun May 17 19:33:48 2020

@author: Jordi
"""

from src.User import User

a = User()

b = Hotels()
c = Hotels()
d = Hotels()

e = Flights()
f = Flights()
g = Flights()

a.afegirHotel(b)
a.afegirHotel(c)
a.afegirHotel(d)

a.afegirVol(e)
a.afegirVol(f)
a.afegirVol(g)

res = a.gestioMetodePagament(0,a)

print("Sense modificar el metode tenim: ")
print (res)

res = a.gestioMetodePagament(1,"VISA")

print("Si escollim VISA retorna: ")
print (res)
print("Que en la classe hi ha: ")
print(a.__dadesPagament__.__tipusTargeta__)

print("I si utilitzem el metode per consultar si es VISA: ")
res = a.gestioMetodePagament(0,a)
print(res)

res = a.gestioMetodePagament(1,"MASTERCARD")

print("Si escollim MASTERCARD retorna: ")
print (res)
print("Que en la classe hi ha: ")
print(a.__dadesPagament__.__tipusTargeta__)

print("si intentem utilitzar un tipus de tarjeta erroni retorna: ")
res = a.gestioMetodePagament(1,"MASTERCAR")
print(res)
print("Que en la classe hi ha l'anterior tipus: ")
print(a.__dadesPagament__.__tipusTargeta__)
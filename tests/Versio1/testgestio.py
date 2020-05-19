# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:43:53 2020

@author: Jordi
"""

from User import User


a = User()

b = Flights()
c = Hotels()
d = Flights()
e = Hotels()
f = Flights()
g = Hotels()

a.afegirVol(b)
a.afegirHotel(c)
a.afegirVol(d)
a.afegirHotel(e)
a.afegirVol(f)
a.afegirHotel(g)

a.gestioNumP(1,2)

res = 1

for v in a.__VolsReservar__:
    if(v.__numPassatgers__ != 2):
        res = -1
        
for h in a.__HotelsReservar__:
    if(h.__numHostes__ != 2):
        res = -1
        
print(res)
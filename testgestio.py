# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:43:53 2020

@author: Jordi
"""
#pagina de Tests


from User import User
from PaymentData import PaymentData
from Hotels import Hotels
from Flights import Flights
from Cars import Cars
from SkyScanner import SkyScanner

a = User()



##################Test 1#################

numP=2
a.gestioNumP(1,numP)

res = 1
print("Numero de viatgers esperat:")
print(numP)

comprovacio=a.gestioNumP(0,-1)

print("Numero de viatgers obtingut:")
print(comprovacio)
if(comprovacio!=numP):
    res=-1
        
print(res)

##################Test 2#################
res2=1

print("Numero de destins esperat:")
print(0)

print("Numero de destins obtinguts:")
print(a.NumeroDestins())

if  a.NumeroDestins()!=0:
    res2=-1
    
print(res2)

##################Test 3#################
res3=1

print("Numero de vols esperat:")
print(0)

print("Numero de vols obtinguts:")
print(a.NumeroVols())

if  a.NumeroDestins()==0:
    if a.NumeroDestins()!=a.NumeroVols():
        res3=-1
    
print(res3)

##################Test 4#################
res4=1

print("Preu esperat:")
print(0)

print("Preu obtinguts:")
print(a.calcularPreuTotal())

if  a.NumeroDestins()==0:
    if a.calcularPreuTotal()!=0:
        res4=-1

print(res4)

##################Test 5#################

res5=1
llista=["ROMA","PARIS"]

b=Flights()
b.__initp__("EF325F","ROMA",1,135,0)
a.afegirVol(b)
c=Flights()
c.__initp__("EY4325F","PARIS",1,170,0)
a.afegirVol(c)
    
destins=a.gestioDestins(0)

print("Destins esperat:")
print(llista)

print("Destins obtingut:")
print(destins)

if len(llista) == len(destins):
        for i in llista:
            for j in destins:
                if i != j:
                   res5=-1

print(res5)

#################Test 6#################
res6=1
llista2=["EF325F","EY4325F"]

codis=a.gestioDestins(1)

print("Vols esperat:")
print(llista)

print("Vols obtingut:")
print(destins)

if len(llista2) == len(codis):
        for i in llista2:
            for j in codis:
                if i != j:
                   res6=-1

print(res6)

##################Test 7#################

res7=1
preu_esperat=135*1+170*1
preu_obtingut=a.calcularPreuTotal()

print("Preu esperat:")
print(preu_esperat)

print("Preu obtinguts:")
print(preu_obtingut)

if preu_esperat != preu_obtingut:
	res7=-1

print(res7)

##################Test 8#################

res8=1
user2=User()

b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
user2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
user2.afegirVol(c2)

preu_esperat2=135*2+170*2
preu_obtingut2=user2.calcularPreuTotal()

print("Preu esperat:")
print(preu_esperat)

print("Preu obtinguts:")
print(preu_obtingut)

if preu_esperat2 != preu_obtingut2:
	res8=-1


print(res8)

##################Test 9#################

res9=1

user2.EliminarDestins(llista[0])
llista.pop(0)

destins_user2=user2.gestioDestins(0)

print("Destins esperat:")
print(llista)

print("Destins obtingut:")
print(destins_user2)

if len(llista) == len(destins_user2):
        for i in llista:
            for j in destins_user2:
                if i != j:
                   res9=-1

print(res9)

##################Test 10#################

res10=1
llista2.pop(0)

codis_user2=user2.gestioDestins(1)

print("Vols esperat:")
print(llista2)

print("Vols obtingut:")
print(destins)

if len(llista2) == len(codis_user2):
        for i in llista2:
            for j in codis_user2:
                if i != j:
                   res10=-1

print(res10)

##################Test 11#################

res11=1
preu_esperat3=170*2
preu_obtingut3=user2.calcularPreuTotal()

print("Preu esperat:")
print(preu_esperat3)

print("Preu obtinguts:")
print(preu_obtingut3)

if preu_esperat3 != preu_obtingut3:
	res11=-1

print(res11)


##################Test 12#################

res12=1
boolea=False
boolea=user2.PagamentViatge()
if boolea==False:
    res12=-1
print(res12)

##################Test 13#################

res13=1
boolea2=False
boolea2=user2.ConfirmarReservaVols()
if boolea2==False:
    res13=-1
print(res13)

import unittest
from src.User import User
from src.PaymentData import PaymentData
from src.Hotels import Hotels
from src.Flights import Flights
from src.Cars import Cars
from src.SkyScanner import Skyscanner
from src.Viatge import Viatge



##################Test 1#################

a = Viatge()
a.gestioNumP(1,2)
assert(a.__numPersones__==2)
assert(a.gestioNumP(0,-1)==a.__numPersones__)

##################Test 2#################

a = Viatge()
a.gestioNumP(1,2)
assert(a.NumeroDestins()==0)

##################Test 3#################

a = Viatge()
a.gestioNumP(1,2)
assert(a.NumeroDestins()==0)
assert(a.NumeroDestins()==a.NumeroVols())

##################Test 4#################

a = Viatge()
a.gestioNumP(1,1)
assert(a.NumeroDestins()==0)
assert(a.calcularPreuTotal()==0)

##################Test 5#################

a = Viatge()
a.gestioNumP(1,1)
llista=["ROMA","PARIS"]
b=Flights()
b.__initp__("EF325F","ROMA",1,135,0)
a.afegirVol(b)
c=Flights()
c.__initp__("EY4325F","PARIS",1,170,0)
a.afegirVol(c)
    
assert(a.gestioDestins(0)==llista)

#################Test 6#################

a = Viatge()
a.gestioNumP(1,1)
llista2=["EF325F","EY4325F"]
b=Flights()
b.__initp__("EF325F","ROMA",1,135,0)
a.afegirVol(b)
c=Flights()
c.__initp__("EY4325F","PARIS",1,170,0)
a.afegirVol(c)

assert(a.gestioDestins(1)==llista2)


##################Test 7#################

a = Viatge()
a.gestioNumP(1,1)
b=Flights()
b.__initp__("EF325F","ROMA",1,135,0)
a.afegirVol(b)
c=Flights()
c.__initp__("EY4325F","PARIS",1,170,0)
a.afegirVol(c)
preu_esperat=135*1+170*1
assert(a.calcularPreuTotal()==preu_esperat)

##################Test 8#################

a2=Viatge()
a.gestioNumP(1,2)
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)
preu_esperat2=135*2+170*2

assert(a2.calcularPreuTotal()==preu_esperat)

##################Test 9#################

a2=Viatge()
a.gestioNumP(1,2)
llista=["ROMA","PARIS"]
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)
a2.EliminarDestins(llista[0])
llista.pop(0)

assert(a2.gestioDestins(0)==llista)

##################Test 10#################

a2=Viatge()
a.gestioNumP(1,2)
llista=["ROMA","PARIS"]
llista2=["EF325F","EY4325F"]
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)
a2.EliminarDestins(llista[0])
llista2.pop(0)
llista.pop(0)

assert(a2.gestioDestins(1)==llista2)

##################Test 11#################

a2=Viatge()
a.gestioNumP(1,2)
llista=["ROMA","PARIS"]
llista2=["EF325F","EY4325F"]
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)
a2.EliminarDestins(llista[0])
llista2.pop(0)
llista.pop(0)
preu_esperat3=170*2

assert(a2.calcularPreuTotal()==preu_esperat)

##################Test 12#################

a2=Viatge()
a.gestioNumP(1,2)
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)

assert(a2.PagamentViatge()==True)

##################Test 13#################

a2=Viatge()
a.gestioNumP(1,2)
b2=Flights()
b2.__initp__("EF325F","ROMA",2,135,0)
a2.afegirVol(b2)
c2=Flights()
c.__initp__("EY4325F","PARIS",2,170,0)
a2.afegirVol(c2)

assert(a2.ConfirmarReservaVols()==True)
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 10:49:19 2020

@author: Jordi
"""


from src.PaymentData import PaymentData
from src.Hotels import Hotels
from src.Flights import Flights
from src.Cars import Cars
from src.User import User

from src.Booking import Booking
from src.Bank import Bank
from src.SkyScanner import Skyscanner
from src.Rentalcars import Rentalcars

class Viatge:

    __slots__ = {'__maxim__','__usuari__','__dadesPagament__','__VolsReservar__','__HotelsReservar__','__CotxesReservar__','__numPersones__'}
    
    def __init__(self):
        self.__usuari__ = User()
        self.__dadesPagament__ = PaymentData()
        self.__VolsReservar__ = list()
        self.__HotelsReservar__ = list()
        self.__CotxesReservar__ = list()
        self.__numPersones__ = -1
        self.__maxim__ = 4
        
    def afegirVol(self, v):
        if(self.NumeroVols() < 4):
            self.__VolsReservar__.append(v)
            return 1
        else:
            return -1
        
    def afegirHotel(self, v):
        if(self.NumeroHotels() < 4):
            self.__HotelsReservar__.append(v)
            return 1
        else:
            return -1
        
    def afegirCotxe(self, v):
        if(self.NumeroCotxes() < 4):
            self.__CotxesReservar__.append(v)
            return 1
        else:
            return -1
           
        
    def gestioNumP(self, gestio, x):
        if(gestio == 0):
            return(self.__numPersones__)
        else:
            if(gestio == 1):
                self.__numPersones__ = x
                for v in self.__VolsReservar__:
                    v.__numPassatgers__ = x
                for h in self.__HotelsReservar__:
                    h.__numHostes__ = x
                return x
            else:
                return -1
            
            
    def gestioMetodePagament(self, gestio, m):
        if(gestio == 0):
            return(self.__dadesPagament__.__tipusTargeta__)
        else:
            if(gestio == 1 and ((m == "VISA") or (m == "MASTERCARD"))):
                self.__dadesPagament__.__tipusTargeta__ = m
                return m
            else:
                return -1
            
                
    def gestioDestins(gestio,self): #al contrari del que has fet a dalt, no modifiquem la classe flight perque considerem que 
        if(gestio==0):                             #la búsqueda de vols es fa a un nivell superior amb l'algoritme
        	ldestins=[]
        	for v in self.__VolsReservar__:
        		ldestins.append(v.__desti__)             
        	return(ldestins)
        if(gestio==1):
            lvol=[]
            for v in self.__VolsReservar__:
                lvol.append(v.__codiVol__) 
            return lvol
       
    def calcularPreuTotal(self):
        Import=0
        for v in self.__VolsReservar__:
            Import=Import+v.__importv__*v.__numPassatgers__
            if(v.__taxav__>0):
                Import=Import+v.__taxav__
                
        for h in self.__HotelsReservar__:
            Import = Import+round((h.__numHostes__ / 3),0)*h.__importh__*h.__durada__
            if(h.__taxah__>0):
                Import=Import+h.__taxah__
                
        for c in self.__CotxesReservar__:
            Import=Import+c.__diesReserva__ * round((self.__numPersones__ / 4),0)*c.__importc__
            if(c.__taxac__>0):
                Import=Import+c.__taxac__
                
        self.__dadesPagament__.__import__=Import
        return Import
            
    def PagamentViatge(self): #falta implementacio d'errors pero no ens ho demanen encara    
        pag=Bank()
        res=pag.do_payment(self.__usuari__, self.__dadesPagament__)
        return res
         
    def ConfirmarReservaVols(self): #no considerem errors
        auxRes = Skyscanner()
        auxRes.confirm_reserve(self.__usuari__, self.__VolsReservar__) 

        
    def NumeroVols(self):
        return len(self.__VolsReservar__)
    
    def NumeroHotels(self):
        return len(self.__HotelsReservar__)
    
    def NumeroCotxes(self):
        return len(self.__CotxesReservar__)
    
    def NumeroDestins(self):
        return len(self.__VolsReservar__)
            
    def EliminarDestins(self, desti):
    	for v in range(self.NumeroVols()):
    		if self.__VolsReservar__[v].getDesti()==desti:
    			self.__VolsReservar__.pop(v)
    			break

    def ErrorPagament(self,isCorrect):
        if isCorrect==False:
            print("Se ha detectado un error en el pago")
            return -1
        else:
            return 1
        
    def gestioallotjaments(gestio, h,self): #0 per afegir un allotjament i 1 per treurel. h es un objecte de la classe hotel
        if(gestio==0):
        	self.afegirhotel(h)
        if(gestio==1):
           for i in range(self.NumeroHotels()):
               if self.__HotelsReservar__[i].getCodi()==h.getCodi():
                   self.__HotelsReservar__.pop(i)
    def gestiovehicles(gestio,c,self): #0 per afegir un vehicle i 1 per treurel. c es un objecte de la classe cotxe
        if(gestio==0):
        	self.afegirCotxe(c)
        if(gestio==1):
           for i in range(self.NumeroCotxes()):
               if self.__CotxesReservar__[i].getCodi()==c.getCodi():
                   self.__CotxesReservar__.pop(i)
            
    def GestionarConfirmacioReserva(self): #fem la reserva dels vols i mirem si hi han errors o no
        api_SkyScanner = Skyscanner()
        resultatConfirmacio = api_SkyScanner.confirm_reserve(self.__usuari__, self.__VolsReservar__)
        return resultatConfirmacio
    
    def ReservaVolsConsiderantErrors(self):
        api_SkyScanner = Skyscanner()
        resultatConfirmacio = api_SkyScanner.confirm_reserve(self.__usuari__, self.__VolsReservar__)
        i = 0
        while(resultatConfirmacio == False & i < 3):
            resultatConfirmacio = api_SkyScanner.confirm_reserve(self.__usuari__, self.__VolsReservar__)
            i = i + 1
        if(i == 3):
            api_banc = Bank()
            self.__dadesPagament__.__import__ = -1*self.__dadesPagament__.__import__
            api_banc.do_payment(self.__usuari__, self.__dadesPagament__)
            self.__dadesPagament__.__import__ = -1*self.__dadesPagament__.__import__
        return resultatConfirmacio
        
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
        if(len(self.__VolsReservar__) < 4):
            self.__VolsReservar__.append(v)
            return 1
        else:
            return -1
        
    def afegirHotel(self, v):
        if(len(self.__HotelsReservar__) < 4):
            self.__HotelsReservar__.append(v)
            return 1
        else:
            return -1
        
    def afegirCotxe(self, v):
        if(len(self.__CotxesReservar__) < 4):
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
        
        print("Introdueix el nom del titular de la targeta: \n")
        self.__nomTitular__ =input()
        
        print("Introdueix el tipus de targeta: \n")
        self.__tipusTargeta__ =input()
        
        print("Introdueix el codi de Seguretat de la targeta: \n")
        self.__codiSeguretat__ =input()
        
        pag=Bank()
        res=pag.do_payment(self,PaymentData())
        return res
         
    def ConfirmarReservaVols(self):
        auxRes = Skyscanner()
        resultat = auxRes.confirm_reserve(self, self.__VolsReservar__) 
        return resultat
        
    def NumeroVols(self):
        return len(self.__VolsReservar__)
    
    def NumeroHotels(self):
        return len(self.__HotelsReservar__)
    
    def NumeroCotxes(self):
        return len(self.__CotxesReservar__)
    
    def NumeroDestins(self):
        return len(self.__destins__)
        
    def EliminarDestins(self, desti):
    	for v in len(self.__VolsReservar__):
    		if self.__VolsReservar__[v].__desti__==desti:
    			self.__VolsReservar__.pop(v)
    			break
    	for l in len(self.__destins__):
    		if self.__destins__[l]==desti:
    			self.__destins__.pop(v)
    			break
    def ErrorPago(self,isCorrect):
        if isCorrect==False:
            print("Se ha detectado un error en el pago")
            return -1
        else:
            return 1
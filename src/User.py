# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:10:25 2020

@author: Jordi
"""



class User:

    __slots__ = {'__nom__','__DNI__','__DirPostal__','__NumTelef__','__Email__'}
    
    def __init__(self):
            self.__nom__ = ''
            self.__DNI__ = ''
            self.__DirPostal__ = -1
            self.__NumTelef__ = -1
            self.__Email__ = ''
    
    def AssignarDades(self, nom , DNI, DirPostal, NumTelef, Email):
            self.__nom__ = nom
            self.__DNI__ = DNI
            self.__DirPostal__ = DirPostal
            self.__NumTelef__ = NumTelef
            self.__Email__ = Email
            
    def getNom(self):
        return self.__nom__
    
    def getDNI(self):
        return self.__DNI__
    
    def getDirPostal(self):
        return self.__DirPostal__
    
    def getNumTelef(self):
        return self.__NumTelef__
    
    def getEmail(self):
        return self.__Email__
    
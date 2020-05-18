# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:16:20 2020

@author: Jordi
"""

class Cars:

    __slots__={'__codi__','__marca__','__recollida__','__diesReserva__'}
    
    def __init__(self):
        self.__codi__ = -1
        self.__marca__ = ''
        self.__recollida__ = ''
        self.__diesReserva__ = -1
        self.__taxac__ = -1
        self.__importc__ = -1
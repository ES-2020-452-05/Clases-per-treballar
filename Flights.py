# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:15:51 2020

@author: Jordi
"""

class Flights:

    __slots__ = {'__codiVol__','__desti__','__numPassatgers__'}
    
    def __init__(self):
        self.__codiVol__ = -1
        self.__desti__ = ''
        self.__numPassatgers__ = -1
        self.__taxav__ = -1
        self.__importv__ = -1
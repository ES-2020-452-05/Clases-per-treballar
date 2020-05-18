# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:10:25 2020

@author: Jordi
"""

from PaymentData import PaymentData
from Hotels import Hotels
from Flights import Flights
from Cars import Cars

class User:

    __slots__ = {'__nom__','__DNI__','__correu__','__altres__'}
    
    def __init__(self):
            self.__nom__ = ''
            self.__DNI__ = ''
            self.__correu__ = ''
            self.__altres__ = ''
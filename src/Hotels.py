# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:15:20 2020

@author: Jordi
"""

class Hotels:

    __slots__ = {'__codi__','__nom__','__numHostes__','__numHabitacions__','__durada__', '__taxah__','__importh__'}
    
    def __init__(self):
        self.__codi__=-1
        self.__nom__ = ''
        self.__numHostes__ = -1
        self.__numHabitacions__ = -1
        self.__durada__ = -1
        self.__taxah__ = -1
        self.__importh__ = -1
        
    def __initp__(self, a, b, c, d, e, f, g):
        self.__codi__= a
        self.__nom__ = b
        self.__numHostes__ = c
        self.__numHabitacions__ = d
        self.__durada__ = e
        self.__taxah__ = f
        self.__importh__ = g
        
    def getCodi(self):
        return self.__codi__
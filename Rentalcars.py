# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:17:55 2020

@author: Jordi
"""

from User import User
from Cars import Cars


class Rentalcars():

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, cars: Cars) -> bool:
        return True
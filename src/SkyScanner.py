# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:18:22 2020

@author: Jordi
"""

from src.User import User
from src.Flights import Flights


class Skyscanner():

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, flights: Flights) -> bool:
        return True
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:16:48 2020

@author: Jordi
"""

from User import User
from Hotels import Hotels


class Booking():

    def __init__(self):
        pass

    def confirm_reserve(self, user: User, hotels: Hotels) -> bool:
        return True
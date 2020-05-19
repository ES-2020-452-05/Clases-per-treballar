# -*- coding: utf-8 -*-
"""
Created on Sun May 17 12:18:58 2020

@author: Jordi
"""

from src.User import User
from src.PaymentData import PaymentData


class Bank:

    def __init__(self):
        pass

    def do_payment(self, user: User, payment_data: PaymentData):
        return True
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:26:25 2020

@author: Jordi
"""


import unittest
from src.Viatge import Viatge
from src.Bank import Bank
from unittest import mock
     
class TestPagamentViatge (unittest.TestCase):      

    def testCasFalse (self):
         copia_api_Bank = mock.create_autospec(Bank)
         viatge = Viatge()
         copia_api_Bank.do_payment.return_value = False
         res = viatge.GestionarErrorPagament(copia_api_Bank)
         self.assertFalse(res)        
            
if __name__ == '__main__':
    unittest.main()
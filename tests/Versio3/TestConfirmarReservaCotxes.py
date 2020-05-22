# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:55:20 2020

@author: Jordi
"""

import unittest
from src.Viatge import Viatge
from src.Rentalcars import Rentalcars
from unittest import mock
     
class TestConfirmarReservaCotxes (unittest.TestCase):      

    def testCasTrue (self):
         copia_api_Rentalcars = mock.create_autospec(Rentalcars)
         viatge = Viatge()
         copia_api_Rentalcars.confirm_reserve.return_value = True
         res = viatge.ConfirmarReservaCotxes(copia_api_Rentalcars)
         self.assertTrue(res)
    
    def testCasFalse (self):
         copia_api_Rentalcars = mock.create_autospec(Rentalcars)
         viatge = Viatge()
         copia_api_Rentalcars.confirm_reserve.return_value = False
         res = viatge.ConfirmarReservaCotxes(copia_api_Rentalcars)
         self.assertFalse(res)        
            
if __name__ == '__main__':
    unittest.main()
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:22:29 2020

@author: Jordi
"""

import unittest
from src.Viatge import Viatge
from src.SkyScanner import Skyscanner
from unittest import mock

class TestConfirmarVolBasic (unittest.TestCase):

    def testEsCridaSkyScanner (self):
         copia_api_Skyscanner = mock.create_autospec(Skyscanner)
         viatge = Viatge()
         copia_api_Skyscanner.confirm_reserve.return_value = True
         viatge.ConfirmarReservaVols(copia_api_Skyscanner)
         copia_api_Skyscanner.confirm_reserve.assert_called_once()



if __name__ == '__main__':
    unittest.main()
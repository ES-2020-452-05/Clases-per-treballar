import unittest
from src.Viatge import Viatge
from src.Bank import Bank
from unittest import mock
     
class TestPagamentViatge (unittest.TestCase):      

    def testEsCridaBanc (self):
         copia_api_Bank = mock.create_autospec(Bank)
         viatge = Viatge()
         copia_api_Bank.do_payment.return_value = True
         viatge.PagamentViatge(copia_api_Bank)
         copia_api_Bank.do_payment.assert_called_once()
         
            
            
if __name__ == '__main__':
    unittest.main()
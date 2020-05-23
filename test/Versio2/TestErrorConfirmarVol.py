import unittest
from src.Viatge import Viatge
from src.SkyScanner import Skyscanner
from unittest import mock
     
class TestGestioConfirmarVol (unittest.TestCase):      

    def testCasError (self):
         copia_api_Skyscanner = mock.create_autospec(Skyscanner)
         viatge = Viatge()
         copia_api_Skyscanner.confirm_reserve.return_value = False
         res = viatge.GestionarConfirmacioReserva(copia_api_Skyscanner)
         self.assertFalse(res)
         
            
            
if __name__ == '__main__':
    unittest.main()
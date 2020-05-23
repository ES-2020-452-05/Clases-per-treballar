import unittest
from src.Viatge import Viatge
from unittest import mock
from src.SkyScanner import Skyscanner
from src.Flights import Flights


class TestsReservaVolsConsiderantErrors (unittest.TestCase):
    
    def testCasUnFalse(self):
        copia_api_Skyscanner = mock.create_autospec(Skyscanner)
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        
        copia_api_Skyscanner.confirm_reserve.side_effect=[False,True]
        viatge.ReservaVolsConsiderantErrors(copia_api_Skyscanner)
        self.assertEqual(copia_api_Skyscanner.confirm_reserve.call_count, 2)
    
    def testCasTrue(self):
        copia_api_Skyscanner = mock.create_autospec(Skyscanner)
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        
        copia_api_Skyscanner.confirm_reserve.return_value=True
        res=viatge.ReservaVolsConsiderantErrors(copia_api_Skyscanner)
        self.assertTrue(res)
    
    def testCasFalse(self):
        copia_api_Skyscanner = mock.create_autospec(Skyscanner)
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        
        copia_api_Skyscanner.confirm_reserve.return_value = False
        viatge.ReservaVolsConsiderantErrors(copia_api_Skyscanner)
        self.assertEqual(copia_api_Skyscanner.confirm_reserve.call_count,4)
    
    
if __name__ == '__main__':
    unittest.main()
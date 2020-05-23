import unittest
from unittest import mock
from src.Flights import Flights
from src.Viatge import Viatge
from src.Rentalcars import Rentalcars
class TestReservaCarsConsiderantErrors(unittest.TestCase):
    
    def testReintentVehicle(self):
        copia_api_Rentalcars = mock.create_autospec(Rentalcars)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        copia_api_Rentalcars.confirm_reserve.return_value = False
        viatge.ReservaCarsConsiderantErrors(copia_api_Rentalcars)
        self.assertTrue((copia_api_Rentalcars.confirm_reserve.call_count != 1) & (copia_api_Rentalcars.confirm_reserve.called==True)) 

    def testCorrecteUnReintentVehicle(self):
        copia_api_Rentalcars = mock.create_autospec(Rentalcars)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        copia_api_Rentalcars.confirm_reserve.side_effect = [False, True]
        viatge.ReservaCarsConsiderantErrors(copia_api_Rentalcars)
        self.assertTrue(copia_api_Rentalcars.confirm_reserve.call_count == 2)
    
    def testMaximErrorsVehicle(self):
        copia_api_Rentalcars = mock.create_autospec(Rentalcars)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        copia_api_Rentalcars.confirm_reserve.return_value = False
        self.assertFalse(viatge.ReservaCarsConsiderantErrors(copia_api_Rentalcars))
        
    


if __name__ == '__main__': 
    unittest.main()
    
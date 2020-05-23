import unittest
from unittest import mock
from src.Flights import Flights
from src.Viatge import Viatge
from src.Booking import Booking
class TestReservaHotelsConsiderantErrors(unittest.TestCase):
    
    def testReintentHotel(self):
        copia_api_Booking = mock.create_autospec(Booking)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        copia_api_Booking.confirm_reserve.return_value = False
        viatge.ReservaHotelsConsiderantErrors(copia_api_Booking)
        self.assertTrue((copia_api_Booking.confirm_reserve.call_count != 1) & (copia_api_Booking.confirm_reserve.called==True)) 

    def testCorrecteUnReintentHotel(self):
        copia_api_Booking = mock.create_autospec(Booking)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        copia_api_Booking.confirm_reserve.side_effect = [False, True]
        viatge.ReservaHotelsConsiderantErrors(copia_api_Booking)
        self.assertTrue(copia_api_Booking.confirm_reserve.call_count == 2)
    
    def testMaximErrorsHotel(self):
        copia_api_Booking = mock.create_autospec(Booking)
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        copia_api_Booking.confirm_reserve.return_value = False
        self.assertFalse(viatge.ReservaHotelsConsiderantErrors(copia_api_Booking))


if __name__ == '__main__': 
    unittest.main()
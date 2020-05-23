import unittest
from src.Viatge import Viatge
from src.Booking import Booking
from unittest import mock
     
class TestConfirmarReservaHotels (unittest.TestCase):      

    def testCasTrue (self):
         copia_api_Booking = mock.create_autospec(Booking)
         viatge = Viatge()
         copia_api_Booking.confirm_reserve.return_value = True
         res = viatge.ConfirmarReservaHotels(copia_api_Booking)
         self.assertTrue(res)
    
    def testCasFalse (self):
         copia_api_Booking = mock.create_autospec(Booking)
         viatge = Viatge()
         copia_api_Booking.confirm_reserve.return_value = False
         res = viatge.ConfirmarReservaHotels(copia_api_Booking)
         self.assertFalse(res)        
            
if __name__ == '__main__':
    unittest.main()
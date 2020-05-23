import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestgestioMetodePagament(unittest.TestCase):
    
    def testMetodeCorrecte(self):
        viatge = Viatge()
        viatge.__numPersones__ = 2
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.gestioMetodePagament(1, "VISA")
        self.assertEqual(viatge.gestioMetodePagament(0, "VISA"), "VISA", viatge.__dadesPagament__.__tipusTargeta__)
        
if __name__ == '__main__':
    unittest.main()
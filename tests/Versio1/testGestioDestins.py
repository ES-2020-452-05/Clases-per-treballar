import unittest
from src.Viatge import Viatge
from src.Flights import Flights


class TestsGestioDestins(unittest.TestCase):

    def testLlistaDestinsEsperada(self):
        viatge = Viatge()
        viatge.gestioNumP(1,1)
        llistaDestins=["ROMA","PARIS"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        self.assertEqual(viatge.gestioDestins(0), llistaDestins)
        
    def testLlistaVolsEsperada(self):
        viatge = Viatge()
        viatge.gestioNumP(1,1)
        llistaVols=["EF325F","EY4325F"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        self.assertEqual(viatge.gestioDestins(1), llistaVols)
        
    def testLlistaDestinsTreient(self):
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        llistaDestins=["ROMA","PARIS"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        viatge.EliminarDestins(llistaDestins[0])
        llistaDestins.pop(0)
        self.assertEqual(viatge.gestioDestins(0), llistaDestins)
        
    def testLlistaVolsTreient(self):
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        llistaDestins=["ROMA","PARIS"]
        llistaVols=["EF325F","EY4325F"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        viatge.EliminarDestins(llistaDestins[0])
        llistaVols.pop(0)
        llistaDestins.pop(0)
        self.assertEqual(viatge.gestioDestins(1), llistaVols)
        
        
if __name__ == '__main__':
    unittest.main()
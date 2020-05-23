import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestCalcularPreu (unittest.TestCase):

    def testUnViatger (self):
        viatge = Viatge()
        viatge.gestioNumP(1,1)

        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        preu_esperat=135*1+170*1
        self.assertEqual(viatge.calcularPreuTotal(), preu_esperat)
    
    def testMesUnViatger (self):
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        preu_esperat=135*2+170*2
        self.assertEqual(viatge.calcularPreuTotal(), preu_esperat)
        
    
    def testTreureDestins (self):
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        llista=["ROMA","PARIS"]
        llista2=["EF325F","EY4325F"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        viatge.EliminarDestins(llista[0])
        llista2.pop(0)
        llista.pop(0)
        preu_esperat=170*2

        self.assertEqual(viatge.calcularPreuTotal(), preu_esperat)
if __name__ == '__main__':
    unittest.main()
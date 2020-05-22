# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestsVersió1_11 (unittest.TestCase):

    def test11 (self):
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

        assert(viatge.calcularPreuTotal()==preu_esperat)
if __name__ == '__main__':
    unittest.main()


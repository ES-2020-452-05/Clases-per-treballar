# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestsVersió1_8 (unittest.TestCase):

    def test8 (self):
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        preu_esperat=135*2+170*2

        assert(viatge.calcularPreuTotal()==preu_esperat)
if __name__ == '__main__':
    unittest.main()


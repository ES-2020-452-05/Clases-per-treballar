# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestsVersió1_7 (unittest.TestCase):

    def test7 (self):
        viatge = Viatge()
        viatge.gestioNumP(1,1)

        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        preu_esperat=135*1+170*1
        assert(viatge.calcularPreuTotal()==preu_esperat)
if __name__ == '__main__':
    unittest.main()


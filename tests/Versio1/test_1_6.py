# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge
from src.Flights import Flights

class TestsVersió1_6 (unittest.TestCase):

    def test6 (self):
        viatge = Viatge()
        viatge.gestioNumP(1,1)
        llista2=["EF325F","EY4325F"]
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)

        assert(viatge.gestioDestins(1)==llista2)
         
if __name__ == '__main__':
    unittest.main()


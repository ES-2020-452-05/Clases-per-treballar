# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge


class TestsVersió1_3 (unittest.TestCase):

    def test3(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        assert(viatge.NumeroDestins()==0)
        assert(viatge.NumeroDestins()==viatge.NumeroVols())
               
if __name__ == '__main__':
    unittest.main()
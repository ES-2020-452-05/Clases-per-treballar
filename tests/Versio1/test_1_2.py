# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge


class TestsVersió1_2 (unittest.TestCase):

    def test2(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        assert(viatge.NumeroDestins()==0)
        
if __name__ == '__main__':
    unittest.main()
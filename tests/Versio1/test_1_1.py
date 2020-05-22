# -*- coding: utf-8 -*-
import unittest
from src.Viatge import Viatge


class TestsVersió1_1 (unittest.TestCase):

    def test1(self):
         viatge = Viatge()
         viatge.gestioNumP(1,2)
         assert(viatge.__numPersones__== 2)
         assert(viatge.gestioNumP(0,-1)==viatge.__numPersones__)

if __name__ == '__main__':
    unittest.main()


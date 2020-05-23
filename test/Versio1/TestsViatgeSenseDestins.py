import unittest
from src.Viatge import Viatge


class TestsViatgeSenseDestins (unittest.TestCase):

    def testCapDesti(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        self.assertEqual(viatge.NumeroDestins(),0)
    
    def testCapVol(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        self.assertEqual(viatge.NumeroDestins(), viatge.NumeroVols())
        self.assertEqual(viatge.NumeroVols(), 0)
        
    def testPreuZero(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        self.assertEqual(viatge.calcularPreuTotal(),0)
               
if __name__ == '__main__':
    unittest.main()
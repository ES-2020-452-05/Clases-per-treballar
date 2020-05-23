import unittest
from src.Viatge import Viatge
from src.Flights import Flights
from src.Cars import Cars
     
class TestGestioallotjament (unittest.TestCase):      

    def testCasAfegir (self):
         vol = Flights() # 152,"Roma", 2, 50, 1 -> preu 101 
         vol.__codiVol__ = 152
         vol.__desti__ = "Roma"
         vol.__numPassatgers__ = 2
         vol.__importv__ = 50
         vol.__taxav__ = 1
         
         cotxe1 = Cars()
         cotxe2 = Cars()
         
         cotxe1.__codi__ = 24
         cotxe1.__diesReserva__ = 10
         cotxe1.__importc__ = 10
         cotxe1.__taxac__ = 25
         #preu 125
         
         cotxe2.__codi__ = 25
         cotxe2.__diesReserva__ = 5
         cotxe2.__importc__ = 10
         cotxe2.__taxac__ = 30
         #preu 80
         
         viatge = Viatge()
         
         viatge.__numPersones__ = 2
         viatge.__VolsReservar__.append(vol)

         
         viatge.gestioCotxes(0, cotxe1)
         self.assertEqual(viatge.__dadesPagament__.__import__, 226)
         
         viatge.gestioCotxes(0, cotxe2)
         self.assertEqual(viatge.__dadesPagament__.__import__, 306)
         
         

    def testCasEliminar (self):
         vol = Flights() # 152,"Roma", 2, 50, 1 -> preu 101 
         vol.__codiVol__ = 152
         vol.__desti__ = "Roma"
         vol.__numPassatgers__ = 2
         vol.__importv__ = 50
         vol.__taxav__ = 1
         
         
         cotxe1 = Cars()
         cotxe2 = Cars()
         
         cotxe1.__codi__ = 24
         cotxe1.__diesReserva__ = 10
         cotxe1.__importc__ = 8
         cotxe1.__taxac__ = 25
         #preu 105
         
         cotxe2.__codi__ = 25
         cotxe2.__diesReserva__ = 5
         cotxe2.__importc__ = 10
         cotxe2.__taxac__ = 30
         #preu 80
         
         viatge = Viatge()
         
         viatge.__numPersones__ = 2
         viatge.__VolsReservar__.append(vol)
         viatge.__CotxesReservar__.append(cotxe1)
         viatge.__CotxesReservar__.append(cotxe2)
         
         viatge.gestioCotxes(1, cotxe2)
         self.assertEqual(viatge.__dadesPagament__.__import__, 206)
         
         viatge.gestioCotxes(1, cotxe1)
         self.assertEqual(viatge.__dadesPagament__.__import__, 101)
                
            
if __name__ == '__main__':
    unittest.main()
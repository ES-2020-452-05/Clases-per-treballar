import unittest
from src.Viatge import Viatge
from src.Flights import Flights
from src.Hotels import Hotels
     
class TestGestioallotjament (unittest.TestCase):      

    def testCasAfegir (self):
         vol = Flights() # "EF325F","Roma", 2, 50, 1 -> preu 101 
         vol.__codiVol__ = "EF325F"
         vol.__desti__ = "ROMA"
         vol.__numPassatgers__ = 2
         vol.__importv__ = 50
         vol.__taxav__ = 1
#         hotel1 preu 250
         hotel1 = Hotels()
         
         hotel1.__codi__ = 34
         hotel1.__nom__ = "Hotel de la vila"
         hotel1.__numHostes__ = 2
         hotel1.__numHabitacions__ = 1
         hotel1.__durada__ = 10
         hotel1.__importh__ = 20
         hotel1.__taxah__ = 50
#         hotel2 preu 350
         
         hotel2 = Hotels()
         
         hotel2.__codi__ = 35
         hotel2.__nom__ = "Hotel de la vila"
         hotel2.__numHostes__ = 2
         hotel2.__numHabitacions__ = 1
         hotel2.__durada__ = 10
         hotel2.__importh__ = 30
         hotel2.__taxah__ = 50
         
         viatge = Viatge()
         
         viatge.__numPersones__ = 2
         viatge.__VolsReservar__.append(vol)
         viatge.gestioallotjaments(0, hotel1)
         self.assertEqual(viatge.__dadesPagament__.__import__, 351)
         
         viatge.gestioallotjaments(0, hotel2)
         self.assertEqual(viatge.__dadesPagament__.__import__, 701)
         
    def testCasEliminar (self):
         vol = Flights() # "EF325F","Roma", 2, 50, 1 -> preu 101 
         vol.__codiVol__ = "EF325F"
         vol.__desti__ = "ROMA"
         vol.__numPassatgers__ = 2
         vol.__importv__ = 50
         vol.__taxav__ = 1
#         hotel1 preu 250
         hotel1 = Hotels()
         
         hotel1.__codi__ = 34
         hotel1.__nom__ = "Hotel de la vila"
         hotel1.__numHostes__ = 2
         hotel1.__numHabitacions__ = 1
         hotel1.__durada__ = 10
         hotel1.__importh__ = 20
         hotel1.__taxah__ = 50
#         hotel2 preu 350
         
         hotel2 = Hotels()
         
         hotel2.__codi__ = 35
         hotel2.__nom__ = "Hotel de la vila"
         hotel2.__numHostes__ = 2
         hotel2.__numHabitacions__ = 1
         hotel2.__durada__ = 10
         hotel2.__importh__ = 30
         hotel2.__taxah__ = 50
         
         viatge = Viatge()
         
         viatge.__numPersones__ = 2
         viatge.__VolsReservar__.append(vol)
         viatge.__HotelsReservar__.append(hotel1)
         viatge.__HotelsReservar__.append(hotel2)
         viatge.__dadesPagament__.__import__ = 701
         
         viatge.gestioallotjaments(1, hotel2)
         self.assertEqual(viatge.__dadesPagament__.__import__, 351)
         
         viatge.gestioallotjaments(1, hotel1)
         self.assertEqual(viatge.__dadesPagament__.__import__, 101)
                
            
if __name__ == '__main__':
    unittest.main()
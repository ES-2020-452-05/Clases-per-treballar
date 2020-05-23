import unittest
from src.User import User
from src.Flights import Flights
from src.Viatge import Viatge

class TestGestionarDadesFacturacio(unittest.TestCase):
    
    def testDadesCorrectes(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        usuari=User()
        usuari.AssignarDades("vicente", "12345678N", 55555, 987654321, "vicente123@hotmail.com")
        self.assertTrue(viatge.GestionarDadesFacturacio(usuari))
        
    def testDadesIncorrectes(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        usuari=User()
        self.assertFalse(viatge.GestionarDadesFacturacio(usuari))
         

    def testInformacioCompleta(self):
        viatge = Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",1,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",1,170,0)
        viatge.afegirVol(vol2)
        usuari=User()
        usuari.AssignarDades("vicente", "12345678N", 55555, 987654321, "vicente123@hotmail.com")
        self.assertTrue(viatge.GestionarDadesFacturacio(usuari) & 
                        (viatge.__usuari__.__nom__ == "vicente") & 
                        (viatge.__usuari__.__DNI__ == "12345678N") & 
                        (viatge.__usuari__.__DirPostal__ == 55555) & 
                        (viatge.__usuari__.__NumTelef__ == 987654321) & 
                        (viatge.__usuari__.__Email__ == "vicente123@hotmail.com"))
            
            
if __name__ == '__main__': 
    unittest.main()
    






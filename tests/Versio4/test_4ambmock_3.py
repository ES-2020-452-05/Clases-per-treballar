# -*- coding: utf-8 -*-

import unittest
from src.Viatge import Viatge
from unittest import mock
from src.Bank import Bank
from src.Flights import Flights


class TestsVersió4_3 (unittest.TestCase):

    def test3(self):
        copia_api_banc = mock.create_autospec(Bank)
        viatge=Viatge()
        viatge.gestioNumP(1,2)
        vol1=Flights()
        vol1.__initp__("EF325F","ROMA",2,135,0)
        viatge.afegirVol(vol1)
        vol2=Flights()
        vol2.__initp__("EY4325F","PARIS",2,170,0)
        viatge.afegirVol(vol2)
        
        copia_api_banc.do_payment.side_effect=[False,False,False,False]
        res=viatge.ConfirmarPagamentConsiderantErrors(copia_api_banc)
        self.assertEqual(res,4)

if __name__ == '__main__':
    unittest.main()

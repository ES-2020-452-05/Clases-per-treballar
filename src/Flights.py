class Flights:

    __slots__ = {'__codiVol__','__desti__','__numPassatgers__', '__importv__', '__taxav__'}
    
    def __init__(self):
        self.__codiVol__ = ''
        self.__desti__ = ''
        self.__numPassatgers__ = -1
        self.__importv__ = -1
        self.__taxav__ = -1
        
    def __initp__(self, a,b,c,d,e):
        self.__codiVol__ = a
        self.__desti__ = b
        self.__numPassatgers__ = c
        self.__importv__=d
        self.__taxav__=e
        
    def getDesti(self):
        return self.__desti__
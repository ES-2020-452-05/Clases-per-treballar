class PaymentData:

    __slots__ = {'__tipusTargeta__','__nomTitular__','__codiSeguretat__','__import__'}
    
    def __init__(self):
        self.__tipusTargeta__ = ''
        self.__nomTitular__ = ''
        self.__codiSeguretat__ = -1
        self.__import__ = -1
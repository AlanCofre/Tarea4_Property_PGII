class CuentaBacaria:
    def __init__(self, titular, saldo, numero_cuenta, tipo_cuenta, tasa_interes, ):
        self.__titular = titular
        self.__saldo = saldo
        self.__numero_cuenta = numero_cuenta
        self._tasa_interes = tasa_interes
        self.tipo_cuenta = tipo_cuenta
        
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter

    @property
    def numero_cuenta(self):
        return self.__titular
    
    
    
cuenta_prueba = CuentaBacaria("Juan", 1000, "HOLA", "CHAO", 2)
cuenta_prueba.saldo = 100000
print(cuenta_prueba.saldo)
    
    
        











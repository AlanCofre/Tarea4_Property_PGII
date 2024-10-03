class CuentaBancaria:
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
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            print("El saldo no puede ser negativo")
    
    @property
    def numero_cuenta(self):
        return self.__numero_cuenta
    
    @property
    def tasa_interes(self):
        return self.tasa_interes


    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se han depositado {cantidad} en la cuenta.")
        else:
            print("La cantidad a depositar debe ser positiva.")
    
    def retirar(self, cantidad):
        if cantidad > self.__saldo:
            print("No es posible retirar más de lo que hay en la cuenta.")
        elif cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
        else:
            self.__saldo -= cantidad
            print(f"Se han retirado {cantidad} de la cuenta.")

    def aplicar_interes(self):
        interes_aplicado = self.__saldo * self._tasa_interes
        self.__saldo += interes_aplicado
        print(f"Se ha aplicado un interés de {self._tasa_interes * 100}%, aumentando el saldo en {interes_aplicado}.")
        return interes_aplicado

class CuentaVip(CuentaBancaria):
    def __init__(self, titular, saldo, numero_cuenta, tipo_cuenta, tasa_interes, limite_credito):
        super().__init__(titular, saldo, numero_cuenta, tipo_cuenta, tasa_interes)
        self._limite_credito = limite_credito
    
    @property
    def limite_credito(self):
        return self._limite_credito
    
    @limite_credito.setter
    def limite_credito(self, nuevo_limite):
        if nuevo_limite >= 0:
            self._limite_credito = nuevo_limite
        else:
            print("El límite de crédito no puede ser negativo.")

    def retirar(self, cantidad):
        saldo_disponible_total = self.saldo + self._limite_credito
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
        elif cantidad > saldo_disponible_total:
            print("No es posible retirar más de lo que hay disponible (saldo + crédito).")
        else:
            # Primero retiramos del saldo, luego del crédito si es necesario
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad} del saldo.")
            else:
                # Restamos todo el saldo y la diferencia del límite de crédito
                diferencia = cantidad - self.saldo
                self.saldo = 0  # se usa todo el saldo 
                self._limite_credito -= diferencia
                print(f"Se han retirado {self.saldo} del saldo y {diferencia} del crédito.")



# Ejemplo de uso de CuentaVip
cuenta_vip = CuentaVip("Maria Lopez", 500, "987654", "VIP", 0.03, 1000)

# Ver saldo y crédito disponible
print(f"Saldo: {cuenta_vip.saldo}")
print(f"Límite de crédito: {cuenta_vip.limite_credito}")

# Retirar una cantidad menor al saldo
cuenta_vip.retirar(400)  # Usa solo el saldo

# Retirar una cantidad mayor al saldo, usa el crédito
cuenta_vip.retirar(800)  # Usa el saldo y parte del crédito

# Ajustar el límite de crédito
cuenta_vip.limite_credito = 2000  # Nuevo límite de crédito

# Intentar retirar una cantidad mayor al disponible (saldo + crédito)
cuenta_vip.retirar(3000)
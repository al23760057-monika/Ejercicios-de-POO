class CuentaBancaria:
  def __init__(self,titular,numeroCuenta,saldo):
    self.titular = titular
    self.numeroCuenta = numeroCuenta
    self.saldo = saldo

  def depositar(self,cantidad):
    self.saldo = self.saldo + cantidad

  def depositar(self,cantidad,valor):
    return 

  def retirar(self,cantidad):
    if cantidad <= self.saldo:
      self.saldo = self.saldo - cantidad
      return cantidad
    else:
      return "Saldo insuficiente"


  def consultarSaldo(self):
    return self.saldo

  def mostrarInformacion(self):
    return f"{self.titular} tienes {self.saldo}"



cuenta1 = CuentaBancaria("Juan Pérez", "001234567", 1000.0)
print(cuenta1.mostrarInformacion())
cuenta1.depositar(500.0)
print(cuenta1.mostrarInformacion())
print(cuenta1.retirar(1500))
print(cuenta1.mostrarInformacion())
cuenta1.depositar(5500)
print(cuenta1.retirar(10))
print(cuenta1.mostrarInformacion())
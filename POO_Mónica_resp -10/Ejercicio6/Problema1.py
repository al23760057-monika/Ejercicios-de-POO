from abc import ABC, abstractmethod

class Mob(ABC):

    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida


    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        pass

    @abstractmethod
    def moverse(self) -> str:
        pass

  

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"❤️  Vida       : {self.vida} HP")
        print(f"🔊  Sonido     : {self.hacer_sonido()}")
        print(f"⚔️  Tipo       : {self.comportamiento()}")
        print(f"🏃  Movimiento : {self.moverse()}")
        print()



class Vaca(Mob):

    @abstractmethod
    def hacer_sonido(self) -> str:
        return "Muuuu"




@abstractmethod
def comportamiento(self) -> str:
        return "Pasivo"

print(Vaca.comportamiento)


@abstractmethod
def moverse(self) -> str:
        return "Camina lentamente por el prado"

print(Vaca.moverse)





class Creeper(Mob):

    @abstractmethod
    def hacer_sonido(self) -> str:
        return "Ssssss"

    Creeper = Creeper()

    print(Creeper.hacer_sonido)


@abstractmethod
def comportamiento(self) -> str:
    return "Agresivo"

print(Creeper.comportamiento)


@abstractmethod
def moverse(self) -> str:
    return "Camina lento"

print(Creeper.moverse)






class Enderman(Mob):

 @abstractmethod
 def hacer_sonido(self) -> str:
    return "Muuuu"

Vaca = Vaca()

print(Vaca.hacer_sonido)


@abstractmethod
def comportamiento(self) -> str:
        return "Neutral"

print(Vaca.comportamiento)


@abstractmethod
def moverse(self) -> str:
    return "Camina lentamente por el prado"

print(Vaca.moverse)





class Zombie(Mob):

     @abstractmethod
     def hacer_sonido(self) -> str:
        return "Lento"

Zombie = Zombie()

print(Zombie.hacer_sonido)


@abstractmethod
def comportamiento(self) -> str:
    return "Agresivo"

print(Zombie.comportamiento)


@abstractmethod
def moverse(self) -> str:
    return "Camina lento, muerde y ataca"

print(Zombie.moverse)


#Prueba de commit 2




    

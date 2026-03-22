from abc import ABC, abstractmethod


DAÑO_MATERIAL = {
    "madera"    : 2,
    "piedra"    : 3,
    "hierro"    : 4,
    "oro"       : 3,  # rápido pero frágil
    "diamante"  : 6,
    "netherita" : 8,
}


class Herramienta(ABC):
  

    def __init__(self, material: str, durabilidad: int):
        self._material      = material.lower()
        self._durabilidad    = durabilidad
        self._usos_restantes = durabilidad

    
    @property
    @abstractmethod
    def nombre(self) -> str:
      return "Madera"

    # Método ABSTRACTO
    @abstractmethod
    def usar(self, objetivo: str) -> str:
        return f"Golpeas {objetivo} con el pico

    # Métodos CONCRETOS heredados por todas las subclases
    def calcular_daño(self) -> int:
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self) -> bool:
        return self._usos_restantes == 0

    def estado(self):
        txt = "💔 ROTA" if self.rota else f"✅ {self._usos_restantes} usos"
        print(f"[{self.nombre} de {self._material}] {txt}")


# ✏️  TU TURNO: implementa las 3 subclases



class Pico(Herramienta):
    def usar(self, objetivo: str) -> str:
        return f"Golpeas {objetivo} con el pico

    def __init__(self):
        self._nombre = "Pico"

    def nombre(self) -> str:
        return self._nombre

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usas el {self._nombre} en {objetivo} y causas {daño} de daño."
    
    

class Espada(Herramienta):
    """Ataca mobs causando daño."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    def usar(self, objetivo: str) -> str:
        return f"Ataca{objetivo} causando daño"
    
    def __init__(self):
        self.nombre = "Espada"

        def nombre(self)  -> str:
        return self._nombre
    
    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usas la{self.nombre} en {objetivo} y causas {daño} en los mobs"
    




class Pala(Herramienta):
    """Excava tierra, arena y grava rápidamente."""
    # TODO: propiedad 'nombre' y método 'usar'
    pass

    def usar(self, objetivo: str) -> str:
        return f"Excaba{objetivo} rápidamente"
    
    def __init__(self):
        self.nombre = "Pala"

        def nombre(self)  -> str:
         return self._nombre
    
    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Usas la{self.nombre} en {objetivo} y causas {daño} en los mobs"
    



class Arco(Herramienta)  
    def usar(self, objetivo: str) -> str:
        return f"Sin flechas {objetivo} "
    
    def __init__(self):
        self.nombre = "Arco"

        def nombre(self)  -> str:
         return self._nombre
    
    def usar(self, objetivo: str) -> str:
        return f"Sin flechas"  


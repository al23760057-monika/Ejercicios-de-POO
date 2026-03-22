from abc import ABC, abstractmethod


class Animal(ABC):

  @abstractmethod
  def hablar(self):
    pass 


class Perro(Animal):

  def hablar(self):
    return "Guau!"


class Gato(Animal):

  def hablar(self):
    return "Miau!"


perro = Perro()
gato = Gato()
print(perro.hablar()) # Guau!
print(gato.hablar()) # Miau!
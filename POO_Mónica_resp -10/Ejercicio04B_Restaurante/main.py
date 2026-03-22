from Comida import Comida
from Bebida import Bebida
from Postre import Postre

sushi = Comida("sushi", 150,"comida-principal")
jugo_naranja = Bebida("jugo_naranja", 60, "Bebida-fría")
pie_limon = Postre("pie_limón", 50, "Sin gluten: No")


sushi.mostrar_info()
jugo_naranja.mostrar_info()
pie_limon.mostrar_info()

sushi.tipo()
jugo_naranja.tipo()
pie_limon.tipo()



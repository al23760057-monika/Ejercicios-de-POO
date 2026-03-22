if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
        Arco("oro", 6)
    ]
    objetivos = ["mena de diamante", "Creeper", "arena","dispara ágilmente"]

    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()

    while romper:
        print(f"romper: {{pico}}")
        romper +=1


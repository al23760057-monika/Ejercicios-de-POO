if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
        Zombie("Zelda",50),
    ]
    for mob in mobs:
        mob.presentarse()
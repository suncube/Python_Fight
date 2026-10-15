class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack
    pass

    @property
    def is_alive(self):
        return self.health > 0

    def attacking(self, enemy):
        pass

    def set_damage(self, enemy):
        pass

    def __str__(self):
        return f"{self.__class__.__name__}, Health: {self.health}, Attack:{self.attack}"


class Elf(Warrior):
    def __init__(self, health=45, attack=7, agility=3):
        super().__init__(health, attack)
        self.agility = agility
    pass

    def __str__(self):
        return f"{super().__str__()}, Agility: {self.agility}"


def fight(fighter1, fighter2):
    is_first_attack = True
    while fighter1.is_alive and fighter2.is_alive:
        if is_first_attack:
            fighter1.attacking(fighter2)
        else:
            fighter2.attacking(fighter1)
        is_first_attack = not is_first_attack

    return fighter1.is_alive


w = Warrior()
print(w)

e = Elf()
print(e)

print(fight(w, e))

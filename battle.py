class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0
# battle func

    def get_attack(self):
        return self.attack

    def set_damage(self, damage):
        self.health -= damage

    def fight_with(self, enemy):
        enemy.set_damage(self.get_attack())
#

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.health += other
        return self

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            self.health *= scalar
        return self

    def __str__(self):
        return f"{self.__class__.__name__}, Health: {self.health}, Attack:{self.attack}"


class Elf(Warrior):
    def __init__(self, health=45, attack=7, agility=3):
        super().__init__(health, attack)
        self.agility = agility
        self.current_agility = 0

    def set_damage(self, damage):
        if self.current_agility == self.agility:
            self.current_agility = 0
            return
        super().set_damage(damage)
        self.current_agility += 1

    def __str__(self):
        return f"{super().__str__()}, Agility: {self.agility}"


class Ork(Warrior):
    FURY_ATTACK_COUNT = 3

    def __init__(self, health=55, attack=6, fury=2):
        self.health = health
        self.attack = attack
        self.fury = fury
        self.current_fury_count = 0

    def get_attack(self):
        if self.current_fury_count == Ork.FURY_ATTACK_COUNT:
            self.current_fury_count = 0
            return super().get_attack() + self.fury

        return super().get_attack()

    def fight_with(self, enemy):
        self.current_fury_count += 1
        super().fight_with(enemy)


class Dragon(Warrior):
    def __init__(self, health=100, attack=10, fire_damage=4):
        self.health = health
        self.attack = attack
        self.fire_damage = fire_damage

# Следующий воин в армии противника получает только fire_damage.
# Если второго воина нет — урон получает только первый.
    def get_attack(self):
        return super().get_attack() + self.fire_damage


class Hobbit(Warrior):
    def __init__(self, health=35, attack=3, stealth=4):
        self.health = health
        self.attack = attack
        self.stealth = stealth
        self.current_attack_count = 0

    def get_attack(self):
        if self.current_attack_count == self.stealth:
            self.current_attack_count = 0
            return super().get_attack() * 2
        return super().get_attack()

    def fight_with(self, enemy):
        self.current_attack_count += 1
        super().fight_with(enemy)


class Dwarf(Warrior):
    def __init__(self, health=60, attack=4, defense=3):
        self.health = health
        self.attack = attack
        self.defense = defense

    def set_damage(self, damage):
        damage -= self.defense
        if damage >= 0:
            super().set_damage(damage)

##############################################


class Army:
    pass


class Battle:
    pass

##############################################


def fight(fighter1, fighter2):
    is_first_attack = True
    while fighter1.is_alive and fighter2.is_alive:
        if is_first_attack:
            fighter1.fight_with(fighter2)
        else:
            fighter2.fight_with(fighter1)
        is_first_attack = not is_first_attack

    return fighter1.is_alive


w = Warrior()
w = w + 10
print(w)

e = Elf()
print(e)

print(fight(w, e))

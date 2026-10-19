class Warrior:
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_alive(self):
        return self.health > 0

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def atk(self):
        return self.get_attack()

# battle func

    def get_attack(self):
        return self.attack

    def set_damage(self, damage):
        old = self.health
        self.health -= damage
        return old - self.health

    def do_fight(self, enemy):
        damage = enemy.set_damage(self.get_attack())
        self.on_attacked()
        return damage

    def on_attacked(self):
        pass

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
            return 0

        self.current_agility += 1
        return super().set_damage(damage)

    def do_fight(self, enemy):
        self.current_agility += 1
        return super().do_fight(enemy)

    def __str__(self):
        return f"{super().__str__()}, Agility: {self.agility}"


class Orc(Warrior):
    FURY_ATTACK_COUNT = 3

    def __init__(self, health=55, attack=6, fury=2):
        self.health = health
        self.attack = attack
        self.fury = fury
        self.current_fury_count = 0

    def get_attack(self):
        if self.current_fury_count == Orc.FURY_ATTACK_COUNT:
            return super().get_attack() + self.fury

        return super().get_attack()

    def on_attacked(self):
        if self.current_fury_count == Orc.FURY_ATTACK_COUNT:
            self.current_fury_count = 0

    def do_fight(self, enemy):
        self.current_fury_count += 1
        return super().do_fight(enemy)


class Dragon(Warrior):
    def __init__(self, health=100, attack=10, fire_damage=4):
        self.health = health
        self.attack = attack
        self.fire_damage = fire_damage

# todo
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
            return super().get_attack() * 2
        return super().get_attack()

    def on_attacked(self):
        if self.current_attack_count == self.stealth:
            self.current_attack_count = 0

    def do_fight(self, enemy):
        self.current_attack_count += 1
        return super().do_fight(enemy)


class Dwarf(Warrior):
    def __init__(self, health=60, attack=4, defense=3):
        self.health = health
        self.attack = attack
        self.defense = defense

    def set_damage(self, damage):
        damage -= self.defense
        if damage >= 0:
            return super().set_damage(damage)

        return 0

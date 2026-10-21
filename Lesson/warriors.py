from fighter import Fighter
# ============================================================
# base class


class Warrior(Fighter):
    def __init__(self, health=50, attack=5):
        self.health = health
        self.attack = attack

    @property
    def is_can_multi_attack(self) -> bool:
        return False

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    @property
    def current_health(self) -> int:
        return self.health

    @property
    def name(self) -> str:
        return self.__class__.__name__

    @property
    def atk(self) -> int:
        return self.get_attack_damage()

# battle func

    def get_attack_damage(self):
        return self.attack

    def set_damage(self, damage):
        self.health = max(0, self.health-damage)
        return damage

    def do_fight(self, enemy):
        damage = enemy.set_damage(self.get_attack_damage())
        return damage

    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.attack += other
        return self

    def __mul__(self, scalar):
        if isinstance(scalar, (int, float)):
            self.attack *= scalar
        return self

    def __str__(self):
        return f"{self.__class__.__name__}, Health: {self.health}, Attack:{self.attack}"

# ============================================================


class Elf(Warrior):
    def __init__(self, health=45, attack=7, agility=3):
        super().__init__(health, attack)
        self.agility = agility
        self._incoming = 0

    def set_damage(self, damage):
        self._incoming += 1
        if self._incoming % (self.agility+1) == 0:
            self._incoming = 0
            return 0

        return super().set_damage(damage)

    def __str__(self):
        return f"{super().__str__()}, Agility: {self.agility}"

# ============================================================


class Orc(Warrior):
    FURY_ATTACK_COUNT = 3

    def __init__(self, health=55, attack=6, fury=2):
        super().__init__(health, attack)
        self.fury = fury
        self._attack_count = 0

    def get_attack_damage(self):
       # print("ORK", self._attack_count % Orc.FURY_ATTACK_COUNT)
        if self._attack_count % Orc.FURY_ATTACK_COUNT == 0:
            return super().get_attack_damage() + self.fury

        return super().get_attack_damage()

    def do_fight(self, enemy):
        self._attack_count += 1
        return super().do_fight(enemy)

    def __str__(self):
        return f"{super().__str__()}, Fury: {self.fury}"

# ============================================================


class Dragon(Warrior):
    def __init__(self, health=100, attack=10, fire_damage=4):
        super().__init__(health, attack)
        self.fire_damage = fire_damage

    @property
    def is_can_multi_attack(self) -> bool:
        return True

    def get_attack_damage(self):
        return self.attack + self.fire_damage

    def do_fight(self, enemy, next_target=None):
        total = self.get_attack_damage()
        enemy.set_damage(total)

        if next_target is not None and next_target.is_alive:
            # total += self.fire_damage
            next_target.set_damage(self.fire_damage)

        return total

    def __str__(self):
        return f"{super().__str__()}, Fire Damage: {self.fire_damage}"

# ============================================================


class Hobbit(Warrior):
    def __init__(self, health=35, attack=3, stealth=4):
        super().__init__(health, attack)
        self.stealth = stealth
        self.current_attack_count = 0

    def get_attack_damage(self):
        if self.current_attack_count % self.stealth == 0:
            return super().get_attack_damage() * 2
        return super().get_attack_damage()

    def do_fight(self, enemy):
        self.current_attack_count += 1
        return super().do_fight(enemy)

    def __str__(self):
        return f"{super().__str__()}, Stealth: {self.stealth}"
# ============================================================


class Dwarf(Warrior):
    def __init__(self, health=60, attack=4, defense=3):
        super().__init__(health, attack)
        self.defense = defense

    def set_damage(self, damage):
        damage -= self.defense
        if damage >= 0:
            return super().set_damage(damage)

        return 0

    def __str__(self):
        return f"{super().__str__()}, Defense: {self.defense}"

# ============================================================

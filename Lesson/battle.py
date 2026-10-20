# from warriors import Warrior, Elf, Ork, Dragon, Hobbit, Dwarf
import warriors
##############################################


class Army:  # todo to interface
    def __init__(self):
        self._warriors = []
        pass

    @property
    def name(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.name
        return self.__class__.__name__

    @property
    def first_alive(self):
        for unit in self._warriors:
            if unit.is_alive:
                return unit
        return None

    @property
    def health(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.health
        return 0

    @property
    def is_alive(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.is_alive
        return False

    def add_members(self, warriorType, count):
        for i in range(count):
            self._warriors.append(warriorType())
        return self

    def do_fight(self, enemy):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.do_fight(enemy)
        return 0

    def get_attack(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.get_attack_damage()
        return 0

    def set_damage(self, damage):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.set_damage(damage)

    def __add__(self, n):
        for w in self.warriors:
            w.attack += n
        return self

    def __mul__(self, n):
        for w in self.warriors:
            w.attack *= n
        return self

    def __len__(self):
        return len(self.warriors)

    def __iter__(self):
        return iter(self.warriors)

    def __str__(self):
        return "\n".join(str(w) for w in self.warriors) or "<empty army>"


class Battle:

    def __init__(self):
        pass

    def fight(self, fighter1: (warriors.Warrior, Army), fighter2: (warriors.Warrior, Army)) -> bool:
        is_first_attack = True
        counter = 1
        self.log_head()
        while fighter1.is_alive and fighter2.is_alive:
            if is_first_attack:
                damage = fighter1.do_fight(fighter2)
                self.log_attack(counter, fighter1.name, damage, fighter1.health, fighter2.health)
            else:
                damage = fighter2.do_fight(fighter1)
                self.log_attack(counter, fighter2.name, damage, fighter1.health, fighter2.health)
                counter += 1
                # print("-"*50)

            is_first_attack = not is_first_attack

        return fighter1.is_alive

    def log_head(self):
        print(f"{"RND":4} {"ATTACKED":10} {"  DMG":5} {"  HP:":5} {"  EHP:":5}")

    def log_attack(self, counter, fighter_name, fighter_atk, health_first, health_second):
        print(f"{counter:4} {fighter_name:10} {fighter_atk:5} {health_first:5} {health_second:5}")

# one to one test
    def fight_one_to_one(self, first, second):
        attacker, defender = first, second
        self.log_head()
        counter = 1
        while True:
            damage = attacker.do_fight(defender)
            self.log_attack(counter, attacker.name, damage, first.health, second.health)

            if not defender.is_alive:
                return attacker is first
            attacker, defender = defender, attacker
            if attacker == first:
                counter += 1
                # print("-"*50)

# # test


elf = warriors.Elf()
print(elf)

orc = warriors.Orc()
print(orc)

battle = Battle()

print(battle.fight_one_to_one(elf, orc))

# #
print()
army1 = Army()
army1.add_members(warriors.Elf, 1)
army2 = Army()
army2.add_members(warriors.Orc, 1)

battle_army = Battle()
result = battle_army.fight(army1, army2)
print(result)

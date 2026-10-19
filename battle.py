# from warriors import Warrior, Elf, Ork, Dragon, Hobbit, Dwarf
import warriors
##############################################


class Army:
    def __init__(self):
        self._warriors = []
        pass

#     first_alive = next((w for w in self._warriors if w.is_alive), None)

# if first_alive is None:
#     # все мертвы — обрабатываем
#     print("Все воины мертвы")
#     return   # или raise, или что-то ещё

    @property
    def is_alive(self):
        warrior = self.first_alive
        if warrior is not None:
            return self.is_alive
        return False

    def add_members(self, warriorType, count):
        for i in range(count):
            self._warriors.append(warriorType())
        return self

    def do_fight(self, enemy):
        return enemy.set_damage(self.get_attack())

    def get_attack(self):
        warrior = self.first_alive
        if warrior is not None:
            return self.attack
        return 0

    @property
    def first_alive(self):
        for unit in self._warriors:
            if unit.is_alive:
                return unit
        return None


class Battle:

    def __init__(self):
        pass

    def fight(self, fighter1, fighter2):
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
            is_first_attack = not is_first_attack

        return fighter1.is_alive

    def log_head(self):
        print(f"{"RND":4} {"ATTACKED":10} {"  DMG":5} {"  HP:":5} {"  EHP:":5}")

    def log_attack(self, counter, fighter_name, fighter_atk, health_first, health_second):
        print(f"{counter:4} {fighter_name:10} {fighter_atk:5} {health_first:5} {health_second:5}")


# test

w = warriors.Elf()
print(w)

e = warriors.Orc()
print(e)

battle = Battle()

print(battle.fight(w, e))

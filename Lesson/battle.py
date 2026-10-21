from fighter import Fighter


class Army(Fighter):
    def __init__(self):
        self._warriors = []
        pass

    @property
    def is_can_multi_attack(self) -> bool:
        return False

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
    def next_alive_after(self):
        is_first_find = False
        for unit in self._warriors:
            if unit.is_alive:
                if is_first_find:
                    return unit
                else:
                    is_first_find = True
        return None

    @property
    def current_health(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.current_health
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
            if warrior.is_can_multi_attack:
                return warrior.do_fight(enemy, enemy.next_alive_after)

            return warrior.do_fight(enemy)
        return 0

    def get_attack_damage(self):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.get_attack_damage()
        return 0

    def set_damage(self, damage):
        warrior = self.first_alive
        if warrior is not None:
            return warrior.set_damage(damage)

    def __add__(self, n):
        for w in self._warriors:
            w.attack += n
        return self

    def __mul__(self, n):
        for w in self._warriors:
            w.attack *= n
        return self

    def __len__(self):
        return len(self._warriors)

    def __iter__(self):
        return iter(self._warriors)

    def __str__(self):
        return "\n".join(str(w) for w in self._warriors) or "<empty army>"


class Battle:

    def __init__(self):
        pass

    def fight(self, fighter1: (Fighter), fighter2: (Fighter)) -> bool:
        is_first_attack = True
        counter = 1
        self.log_head()
        while fighter1.is_alive and fighter2.is_alive:
            if is_first_attack:
                damage = fighter1.do_fight(fighter2)
                self.log_attack(counter, fighter1.name, damage, fighter1.current_health, fighter2.current_health)
            else:
                damage = fighter2.do_fight(fighter1)
                self.log_attack(counter, fighter2.name, damage, fighter1.current_health, fighter2.current_health)
                counter += 1
                # print("-"*50)

            is_first_attack = not is_first_attack

        return fighter1.is_alive

    def log_head(self):
        print(f"{"RND":4} {"ATTACKED":10} {"  DMG":5} {"  HP:":5} {"  EHP:":5}")

    def log_attack(self, counter, fighter_name, fighter_atk, health_first, health_second):
        print(f"{counter:4} {fighter_name:10} {fighter_atk:5} {health_first:5} {health_second:5}")

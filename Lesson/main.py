from warriors import Warrior, Elf, Orc, Dragon, Hobbit, Dwarf
from battle import Battle, Army

# # test
# -----------------
print("\n*** ALL CLASSES ***")
print(Warrior())
print(Elf())
print(Orc())
print(Dragon())
print(Hobbit())
print(Dwarf())
# -----------------
print("\n*** Warrior [add] [mul] ***")
w = Warrior()
print(w)
w = w + 10
print(w)
w = w * 2
print(w)
# -----------------
print("\n*** Elf vs Orc ***")
elf = Elf()
orc = Orc()
battle = Battle()
print(battle.fight(elf, orc))
# -----------------
print("\n*** ARMY Elf vs ARMY Orc ***")
army1 = Army()
army1.add_members(Elf, 1)
army2 = Army()
army2.add_members(Orc, 1)

battle_army = Battle()
result = battle_army.fight(army1, army2)
print("Win Army 1" if result else "Win Army 2")

# -----------------
print("\n*** DRAGON vs Dwarf ***")
a3 = Army()
a3.add_members(Dragon, 1)

a4 = Army()
a4.add_members(Dwarf, 3)

battle_army = Battle()
result = battle_army.fight(a3, a4)

print("Win Army 3" if result else "Win Army 4")
# # -----------------
# dragon = Dragon()
# orc = Orc(1000, 3, 2)
# battle = Battle()
# print(battle.fight(dragon, orc))

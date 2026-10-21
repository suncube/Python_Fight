from abc import ABC, abstractmethod


class Fighter(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def current_health(self) -> int:
        pass

    @property
    @abstractmethod
    def is_alive(self) -> bool:
        pass

    @property
    def is_can_multi_attack(self) -> bool:
        return False

    @abstractmethod
    def get_attack_damage(self) -> int:
        pass

    @abstractmethod
    def set_damage(self, damage: int) -> int:
        pass

    @abstractmethod
    def do_fight(self, enemy: "Fighter", next_target: "Fighter | None" = None) -> int:
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __mul__(self, scalar):
        pass

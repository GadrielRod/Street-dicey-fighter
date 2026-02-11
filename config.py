from enum import Enum


class Move(Enum):
    PEDRA = "PEDRA (Ataque/Combo)"
    PAPEL = "PAPEL (Especial/Defesa)"
    TESOURA = "TESOURA (Tatica/Counter)"


class ActionType(Enum):
    ATTACK = "Attack"
    SPECIAL = "Special"
    TACTIC = "Tactic"

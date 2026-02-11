import random
from config import Move

class Die:
    def __init__(self, value=None):
        self.value = value if value else random.randint(1, 6)

class DicePool:
    def __init__(self):
        self.dice = []

    def roll_new(self, count):
        for _ in range(count):
            self.dice.append(Die())
        self.dice.sort(key=lambda x: x.value)

    def get_values(self):
        return [d.value for d in self.dice]

    def remove_values(self, values_to_remove):
        """Remove a primeira ocorrência de cada valor na lista values_to_remove."""
        for val in values_to_remove:
            for d in self.dice:
                if d.value == val:
                    self.dice.remove(d)
                    break

class Character:
    """Classe Abstrata para os Lutadores."""
    def __init__(self, name, hp, speed, max_special):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.speed = speed
        self.max_special_dice = max_special
        self.special_pool = [] # Armazena valores inteiros (ex: [6, 1])
        self.description = ""  # Resumo dos combos

    def take_damage(self, amount):
        self.current_hp = max(0, self.current_hp - amount)

    def heal(self, amount):
        self.current_hp = min(self.max_hp, self.current_hp + amount)

    def get_best_combo(self, dice_values):
        """
        Analisa os dados e retorna o melhor combo possível.
        Return: (dano_causado, [lista_de_dados_usados])
        """
        return 0, []
    
    def perform_special(self, opponent=None):
        """
        Executa o especial.
        Return: (dano_causado, mensagem_log)
        """
        return 0, "Nada acontece."

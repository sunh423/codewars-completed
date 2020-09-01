#https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/python
def declare_winner(fighter1, fighter2, first_attacker):
        if first_attacker == fighter1.name:
            return combat(fighter1, fighter2)
        elif first_attacker == fighter2.name:
            return combat(fighter2, fighter1)


def combat(first, second):
    while True:
        second.health -= first.damage_per_attack
        if second.health <= 0:
            return first.name
        first.health -= second.damage_per_attack
        if first.health <= 0:
            return second.name

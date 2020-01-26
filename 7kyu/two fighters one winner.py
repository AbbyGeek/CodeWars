def declare_winner(one, two, first):
    if first == one.name:
        while one.health >= 0 or two.health >= 0:
            two.health = two.health - one.damage_per_attack
            if two.health <= 0:
                return one.name
            one.health = one.health - two.damage_per_attack
            if one.health <= 0:
                return two.name
    else:
        while two.health >= 0 or one.health >= 0:
            one.health = one.health - two.damage_per_attack
            if one.health <= 0:
                return two.name
            two.health = two.health - one.damage_per_attack
            if two.health <= 0:
                return one.name
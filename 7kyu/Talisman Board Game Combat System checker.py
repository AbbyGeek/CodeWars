def get_required(player,enemy):
    if sum(player) - sum(enemy) >= 6:
        return "Auto-win"
    if sum(enemy) - sum(player) >= 6:
        return "Auto-lose"
    if sum(enemy) == sum(player):
        return "Random"
    if sum(player) > sum(enemy):
        num = (sum(enemy)+6)- sum(player)+1
        return "(%s..6)" % (num)
    if sum(player) < sum(enemy):
        num = sum(player)+6 - sum(enemy) - 1
        if num !=0:
            return "(1..%s)" % (num)
        else: return "Pray for a tie!"
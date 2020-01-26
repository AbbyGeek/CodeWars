def mango(q, p):
    cost = int(q/3)*2*p
    if q % 3 == 1:
        cost += p
        return cost
    if q % 3 == 2:
        cost += (2*p)
        return cost
    else: return cost
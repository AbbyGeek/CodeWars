def rental_car_cost(d):
    if d > 6:
        return 40*d-50
    elif d > 2:
        return 40*d-20
    else: return 40*d
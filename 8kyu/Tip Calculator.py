import math
def calculate_tip(amount, rating):
    if rating.lower() == "terrible":
        return amount*0
    if rating.lower() == "poor":
        return math.ceil(amount*.05)
    if rating.lower() == "good":
        return math.ceil(amount * .1)
    if rating.lower() == "great":
        return math.ceil(amount * .15)
    if rating.lower() == "excellent":
        return math.ceil(amount * .2)
    if isinstance(rating, float):
        return 0.0
    else: return "Rating not recognised"
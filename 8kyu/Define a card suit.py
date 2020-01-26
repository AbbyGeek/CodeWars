def define_suit(card):
    if "C" in card:
        return 'clubs'
    elif "H" in card:
        return 'hearts'
    elif "D" in card:
        return 'diamonds'
    else:
        return 'spades'
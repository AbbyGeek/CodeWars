def whoseMove(lastPlayer, win):
    if win == True:
        return lastPlayer
    else:
        if lastPlayer == "white":
            return "black"
        else: return "white"
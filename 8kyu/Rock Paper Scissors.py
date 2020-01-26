def rps(p1, p2):
    r = "rock"
    p = "paper"
    s = "scissors"
    if p1 == p2:
        return "Draw!"
    if p1 == r:
        if p2 == p:
            return "Player 2 won!"
        if p2 == s:
            return "Player 1 won!"
    if p1 == s:
        if p2 == p:
            return "Player 1 won!"
        if p2 == r:
            return "Player 2 won!"
    if p1 == p:
        if p2 == s:
            return "Player 2 won!"
        if p2 == r:
            return "Player 1 won!"
def grader(score):
    if score > 1:
        return "F"
    if score >= .9:
        return "A"
    if score >= .8:
        return "B"
    if score >= .7:
        return "C"
    if score >= .6:
        return "D"
    else: return "F"
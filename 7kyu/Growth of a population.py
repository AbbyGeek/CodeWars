def nb_year(p0, percent, aug, p):
    pn = p0
    years = 0
    while pn < p:
        pn = pn + pn*(percent/100) + aug
        years += 1
    return years
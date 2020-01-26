def calculate_years(principal, interest, tax, desired):
    years = 0
    tot = principal
    while tot < desired:
        tot += (tot*interest)-(tot*interest*tax)
        years += 1
    return years
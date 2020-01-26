def human_years_cat_years_dog_years(human_years):
    A = human_years
    B = 0
    C = 0
    if human_years == 1:
       B = 15
    elif human_years == 2:
        B = 24
    else:
        B = 24 + (human_years-2)*4
    if human_years == 1:
       C = 15
    elif human_years == 2:
        C = 24
    else:
        C = 24 + (human_years-2)*5
    return [A,B,C]
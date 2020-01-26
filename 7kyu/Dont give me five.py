def dont_give_me_five(start,end):
    new = []
    for x in range(start,end+1):
        if "5" not in str(x):
            new.append(x)
    return len(new)
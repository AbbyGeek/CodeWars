def who_is_paying(name):
    x = [name]
    if len(name) > 2:
        x = [name, name[:2]]
        return x
    else: return x
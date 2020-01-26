def goto(level,button):
    if type(button) != str:
        return 0
    if level in range(0,4) and button.isdigit()== True and int(button) in range(0,4):
        return int(button) - level
    else: return 0
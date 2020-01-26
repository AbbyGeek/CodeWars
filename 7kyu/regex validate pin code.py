def validate_pin(pin):
    for x in pin:
        if x in "1234567890":
            return len(pin) == 4 or len(pin) == 6
        else: return False
def validate_code(code):
    code = [int(x) for x in str(code)]
    return code[0] in range(1,4)
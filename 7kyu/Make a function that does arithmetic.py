def arithmetic(a, b, operator):
    d = { "add": a+b ,
    "subtract": a-b ,
    "multiply": a*b ,
    "divide": a/b
    }
    return d[operator]
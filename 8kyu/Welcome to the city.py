def say_hello(name, city, state):
    name = str(" ".join(name))
    return "Hello, "+name+"! Welcome to %s, %s!" % (city, state)
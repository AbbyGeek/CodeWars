def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    if type(x) == int or type(x) == float:
        return "Who ate the last cookie? It was Monica!"
    if type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
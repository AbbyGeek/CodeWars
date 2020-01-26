def grow(arr):
        import functools
        import operator
        return functools.reduce(operator.mul, arr, 1)
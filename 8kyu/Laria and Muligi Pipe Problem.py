def pipe_fix(pipes):
    newish_pipes = []
    longest = pipes[len(pipes)-1]
    shortest = pipes[0]
    i = shortest
    while i <= longest:
        newish_pipes += [i]
        i += 1
#    new_pipes = newish_pipes[pipes[0]-1::]
    return newish_pipes
def enough(cap, on, wait):
    spaces_left =  cap - on
    ans = wait - spaces_left
    if ans < 0:
        return 0
    else: return ans
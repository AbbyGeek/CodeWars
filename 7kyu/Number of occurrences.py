def number_of_occurrences(e, s):
    ans = 0
    for x in s:
        if x == e:
            ans += 1
    return ans
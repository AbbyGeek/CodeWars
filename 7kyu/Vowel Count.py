def getCount(inputStr):
    num_vowels = 0
    for x in inputStr:
        if x in "aeiou":
            num_vowels += 1
    
    return num_vowels
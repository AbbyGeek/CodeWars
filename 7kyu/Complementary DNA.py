def DNA_strand(dna):
    new = ""
    for x in dna:
        if x == "A":
            new += "T"
        if x == "T":
            new += "A"
        if x == "G":
            new += "C"
        if x == "C":
            new += "G"
    return new
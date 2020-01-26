def identify_weapon(character):
    d ={"Laval":"Shado Valious",
"Cragger":"Vengdualize",
"Lagravis":"Blazeprowlor",
"Crominus":"Grandorius",
"Tormak":"Tygafyre",
"LiElla":"Roarburn"}
    if character not in d:
        return "Not a character"
    return character +"-" + d[character]
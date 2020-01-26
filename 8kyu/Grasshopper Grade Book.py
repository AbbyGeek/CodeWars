def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if avg >= 90 and avg <= 100:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    else: return "F"
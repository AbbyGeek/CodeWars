def check_exam(arr1,arr2):
    count = 0
    for x in range(len(arr1)):
        if arr2[x] == "":
            pass
        elif arr1[x] == arr2[x]:
            count += 4
        else:
            count -= 1
    if count < 0:
        count = 0
    return count
def count_positives_sum_negatives(arr):
    pos_tot = 0
    neg_sum = 0
    if arr ==[]:
        return []
    else:
        for x in arr:
            if x > 0:
                pos_tot += 1
            elif x < 0:
                neg_sum += x
        return [pos_tot, neg_sum]
def has_negatives(a):

    ht = {}

    for element in a:
        if element > 0 and element not in ht:
            ht[element] = 1
        elif element < 0 and abs(element) not in ht:
            ht[abs(element)] = 1
        elif element > 0 and element in ht:
            ht[element] += 1
        elif element < 0 and abs(element) in ht:
            ht[abs(element)] += 1
    
    result = []
    for k in ht:
        if ht[k] >= 2:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

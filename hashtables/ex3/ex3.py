def intersection(arrays):

    ht = {}

    for subarray in arrays:
        for element in subarray:
            if element not in ht:
                ht[element] = 0
            # else: <-- why doesn't this work???
            if element in ht:    
                ht[element] += 1
    
    result = []

    # for key in ht:
    #     if ht[key] == len(arrays):
    #         result += ht[key]

    # for key in ht:
    #     if ht.get(key) == len(arrays):
    #         result += ht[key]   

    for key, value in ht.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

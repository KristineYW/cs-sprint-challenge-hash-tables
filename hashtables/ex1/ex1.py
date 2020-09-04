def get_indices_of_item_weights(weights, length, limit):
    # weights is a list of integers representing weights
    # length is the number of weights in the list
    # limit is the sum of two weights that we need to reach
    # we need to return INDICES not weights

    ht = {}

    for index_1 in range(length):
        ht[weights[index_1]] = index_1

    for index_2, weight in enumerate(weights):
        difference = limit - weight
        if difference in ht:
            # indices = [index_2, ht[difference]]
            # return(indices.sort(reverse=True))
            return(sorted((index_2, ht[difference]), reverse=True))
    return None
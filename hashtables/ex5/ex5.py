# Your code here



def finder(files, queries):

    ht_queries = {}

    for x in queries:
        if x not in ht_queries:
            ht_queries[x] = x.split('/')[-1]

    ht_files = {}

    for y in files:
        if y not in ht_files:
            ht_files[y] = []
        ht_files[y].append(y) 

    result = []
    for x in ht_queries:
        if y in ht_files:
            result.append(ht_files[y]) 

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

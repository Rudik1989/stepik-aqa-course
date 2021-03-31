with open('e:\\test.txt') as dataset:
    data = dataset.read().lower().strip().split()
    b = set(data)
    d = {}
    val = []
    word = []
    for i in b:
        d[i] = data.count(i)
    for value in d.values():
        val.append(value)
    for key, value in d.items():
        if value == max(val):
            word.append(key)
    print(d)
    word.sort()
    print (word[0], max(val))



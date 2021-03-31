with open(r'e:\\dataset_3380_5.txt') as data:
    d = {}
    for line in data:
        line = line.strip().split()
        #print(line)
        if  line[0] not in d:
            d[line[0]] = [int(line[2])]
        else:
            d[line[0]].append(int(line[2]))
    #print(d)
    for i in range(1,12):
        if str(i) in d:
            l = d.get(str(i))
            l_avr = float(sum(l)/len(l))
            print(i, l_avr)
        else:
            print(i, '-')

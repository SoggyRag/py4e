name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            address = words[1]
            counts[address] = counts.get(address,0) + 1

    alist = list()
    for key, val in counts.items():
        newtup = (val, key)
        alist.append(newtup)
    alist = sorted(alist, reverse=True)
    for val, key in alist[:1]:
        print(key, val)

except:
    print('File not found:',name)

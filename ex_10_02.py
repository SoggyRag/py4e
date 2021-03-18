#Exercise 2: This program counts the distribution of the hour of the day for
#each of the messages. You can pull the hour from the "From" line by finding
#the time string and then splitting that string into parts using the colon
#character. Once you have accumulated the counts for each hour, print out the
#counts, one per line, sorted by hour as shown below.


name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            tods = words[5]
            tod = tods.split(':')
            hod = tod[0]
            counts[hod] = counts.get(hod,0) + 1

    alist = list()
    for key,val in counts.items():
        newtup = (key,val)
        alist.append(newtup)
    alist = sorted(alist)
    for key,val in alist:
        print(key,val)


except:
    print('File not found:',name)

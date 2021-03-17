#Exercise 1: Revise a previous program as follows: Read and parse the
#"From" lines and pull out the addresses from the line. Count the number
#of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who
#has the most commits.


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

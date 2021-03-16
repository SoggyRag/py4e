#Exercise 3: Write a program to read through a mail log,
#build a histogram using a dictionary to count how many messages
#have come from each email address, and print the dictionary.

name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            twords = words[1]
            #print(twords)
            counts[twords] = counts.get(twords,0) + 1
    print(counts)
except:
    print('File not found:',name)

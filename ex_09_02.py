#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for
#lines that start with "From", then look for the third word and
#keep a running count of each of the days of the week.
#At the end of the program print out the contents of your
#dictionary (order does not matter).

name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            twords = words[2]
            counts[twords] = counts.get(twords,0) + 1
    print(counts)
except:
    print('File not found:',name)

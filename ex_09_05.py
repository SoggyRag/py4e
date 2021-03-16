#Exercise 5: This program records the domain name (instead of the address)
#where the message was sent from instead of who the mail came from
#(i.e., the whole email address). At the end of the program,
#print out the contents of your dictionary.

name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        if line.startswith('From '):
            words = line.split()
            twords = words[1]
            swords = twords.split('@')
            ewords = swords[1]
            #print(ewords)
            counts[ewords] = counts.get(ewords,0) + 1
    print(counts)
except:
    print('File not found:',name)

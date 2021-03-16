#Exercise 4: Add code to the above program to figure out who has the most
#messages in the file.
#After all the data has been read and the dictionary has been created,
#look through the dictionary using a maximum loop (see Section [maximumloop])
#to find who has the most messages and print how many messages the person has.

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
    bigcount = None
    bigword = None
    for key,value in counts.items():
        if bigcount is None or value > bigcount:
            bigword = key
            bigcount = value
    print(bigword, bigcount)

except:
    print('File not found:',name)

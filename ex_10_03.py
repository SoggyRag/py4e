#Exercise 3: Write a program that reads a file and prints the letters in
#decreasing order of frequency. Your program should convert all the input
#to lower case and only count the letters a-z. Your program should not count
#spaces, digits, punctuation, or anything other than the letters a-z.
#Find text samples from several different languages and see how letter
#frequency varies between languages. Compare your results with the tables
#at wikipedia.org/wiki/Letter_frequencies.

name = input('Enter a file name: ')
counts = dict()
try:
    handle = open(name)
    for line in handle:
        words = line.lower().rstrip().split()
        for word in words:
            lol = list(word)
            for let in lol:
                counts[let] = counts.get(let,0) + 1

    alist = list()
    for key,val in counts.items():
        newtup = (val,key)
        alist.append(newtup)
    alist = sorted(alist, reverse=True)
    for k,v in alist:
        if v.isalpha():
            print(k,v)

except:
    print('File not found:',name)

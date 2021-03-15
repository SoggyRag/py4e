#Exercise 4: Download a copy of the file from www.py4e.com/code3/romeo.txt
#Write a program to open the file romeo.txt and read it line by line.
#For each line, split the line into a list of words using the split function.
#For each word, check to see if the word is already in a list.
#If the word is not in the list, add it to the list.
#When the program completes,
#sort and print the resulting words in alphabetical order.

wfile = input('Enter file: ')
alist = list()
try:
    ifile = open(wfile)
    for line in ifile:
        words = line.rstrip().split()
        for word in words:
            if word not in alist:
                alist.append(word)
except:
    print('File not found:',wfile)
    quit()
alist.sort()
print(alist)

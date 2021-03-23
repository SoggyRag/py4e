#Exercise 2: Write a program to look for lines of the form

#`New Revision: 39772`
#and extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average.

#Enter file:mbox.txt
#38549.7949721

#Enter file:mbox-short.txt
#39756.9259259

import re
regex = input('Enter file: ')
try:
    file = open(regex)
    alist = list()
    for line in file:
        line = line.rstrip()
        sin = re.findall('^New Revision: ([0-9.]+)',line)
        if len(sin) != 1 : continue
        sinf=float(sin[0])
        alist.append(sinf)
    avg = sum(alist)/len(alist)
    avg = round(avg,7)
    print('Average of numbers in file:',avg)
except:
    print('File not found:',regex)

#Finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#Data Files
#We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
#(There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_1182858.txt
#(There are 99 values and the sum ends with 903)

import re
regex = input('Enter file: ')

#Default ' ' becomes regex_sum_42.txt
if regex == ' ':
    regex = 'regex_sum_42.txt'

#Make a list and open file
alist = list()
file = open(regex)

#Analyze each line for [0-9]+ and add non zero results to alist
for line in file:
    line = line.rstrip()
    sin = re.findall('[0-9]+',line)
    if len(sin) > 0 :
        sin = [int(i) for i in sin]
        alist.extend(sin)

#print(alist)
#Print results
print('Sum of numbers:',sum(alist))
print('Amount of values:',len(alist))

#Exercise 1: Write a simple program to simulate the operation of the
#grep command on Unix. Ask the user to enter a regular expression and
#count the number of lines that matched the regular expression:

#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#Enter a regular expression: ^X-
#mbox.txt had 14368 lines that matched ^X-

#Enter a regular expression: java$
#mbox.txt had 4218 lines that matched java$

import re
regex = input('Enter a regular expression: ')
file = open('mbox.txt')
alist = list()
for line in file:
    sin = re.findall(regex,line)
    if len(sin) != 1 : continue
    alist.append(sin)
print('mbox.txt had',len(alist),'lines that matched',regex)

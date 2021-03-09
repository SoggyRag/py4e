str = 'X-DSPAM-Confidence: 0.8475 '
num = float(str[str.find(':')+1:])
print(num)

str = 'X-DSPAM-Confidence: 0.8475 '
pos = str.find(':')
npos = str[pos+1:]
fpos = float(npos)
print(fpos)

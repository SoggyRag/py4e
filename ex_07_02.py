fname = input('Enter the file name: ')
count = 0
total = 0
try:
    fhand = open(fname)
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
            line = line.rstrip()
            pos = line.find(':')
            nspam = line[pos+1:]
            fspam = float(nspam)
            total = total + fspam
    average = total / count
    print('Average spam confidence:', average)
except:
    if fname == 'dog':
        print('Ya dog you are cool af but that file not here')
    else:
        print('File not found:',fname)

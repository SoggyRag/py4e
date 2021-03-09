sum = 0
count = 0
while True:
    ival = input('Enter a number: ')
    if ival == 'done':
        break
    try:
        fval = float(ival)
        sum = sum + fval
        count = count + 1
    except:
        print('Invalid input')
        continue
print('Total: ',sum)
print('Count: ',count)
print('Average: ',sum/count)

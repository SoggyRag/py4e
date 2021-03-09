def computepay(hours, rate):
    #print('In computepay', hours, rate)
    try:
        if hours <= 40:
            pay = hours * rate
        elif hours > 40:
            pay = (rate * 40) + ((rate * 1.5) * (hours - 40))
        round(pay, 2)
        #print('Returning', pay)
        return pay
    except:
        print('Error, please enter numeric input')

fh = input('Enter hours: ')
fh = float(fh)
fr = input('Enter rate: ')
fr = float(fr)

xp = computepay(fh, fr)

print('Pay:',xp)

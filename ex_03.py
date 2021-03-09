hrs = input('Enter hours: ')
rate = input('Enter rate: ')
hrs = float(hrs)
rate = float(rate)
pay = hrs*rate
payrnd = round(pay, 2)
print('Pay: ',payrnd)

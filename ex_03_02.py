try:
    xh = input('Enter hours: ')
    xh = float(xh)
    xr = input('Enter rate: ')
    xr = float(xr)
    if xh <= 40:
        xp = xh * xr
    elif xh > 40:
        xp = (xr * 40) + ((xr * 1.5) * (xh - 40))
    round(xp, 2)
    print('Pay:',xp)
except:
    print('Error, please enter numeric input')

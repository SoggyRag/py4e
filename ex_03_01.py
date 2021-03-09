xh = input('Enter hours: ')
xr = input('Enter rate: ')
xh = float(xh)
xr = float(xr)
if xh <= 40:
    xp = xh * xr
elif xh > 40:
    xp = (xr * 40) + ((xr * 1.5) * (xh - 40))
round(xp, 2)
print('Pay:',xp)

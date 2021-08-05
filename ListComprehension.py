temps = [221,234,440,-999]
new_temps = [temp /10 for temp in temps if temp!=-999]
new_temps1 = [temp /10 if temp!=-999 else 0 for temp in temps]
print(new_temps)
print(new_temps1)

help(len)


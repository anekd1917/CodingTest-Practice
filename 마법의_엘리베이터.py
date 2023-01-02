storey = int(input('storey: '))
cipher = 1
result = 0


while 1:
    while storey // cipher >= 1:
        cipher *= 10
    
    if cipher - storey < storey - (cipher//10):
        result += 1
        storey = cipher - storey

    if((cipher // 10)<=0):
        break

    cipher //=10

    min = (storey // cipher) * cipher
    max = min + cipher


    if (-1 * (min-storey)) <= max-storey:
        result += min//cipher
        storey = -1 * (min-storey)
    else:
        result += max // cipher
        storey = max-storey

print(result)
 
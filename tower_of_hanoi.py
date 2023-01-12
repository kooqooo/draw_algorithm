n = int(input('num of disks : '))
stick1 = [x for x in range(n, 0, -1)]
stick2 = []
stick3 = []

def hanoi(num, start, end):
    if num > 1:
        hanoi(num - 1, start, 6-start-end)
    printHanoi(n, stick1, stick2, stick3)
    print()
    if start == 1 and end == 2: # 1 -> 2
        stick2.append(num)
        stick1.remove(num)
    elif start == 2 and end == 3: # 2 -> 3
        stick3.append(num)
        stick2.remove(num)
    elif start == 1 and end == 3: # 1 -> 3
        stick3.append(num)
        stick1.remove(num)
    elif start == 3 and end == 2: # 3 -> 2
        stick2.append(num)
        stick3.remove(num)
    elif start == 3 and end == 1: # 3 -> 1
        stick1.append(num)
        stick3.remove(num)    
    elif start == 2 and end == 1: # 2 -> 1
        stick1.append(num)
        stick2.remove(num)
    print(f'[{num}] : {start} -> {end}')
    if num > 1:
        hanoi(num - 1, 6-start-end, end)

def stars(max, star):
    for i in range(max-star):
        print(' ',end='')
    if star == 0:
        print('|', end='')
    else:
        for j in range(star):
            if j == 0:
                print(' * ', end='')
            else:
                if j == star-1:
                    print('* ', end='')
                    break
                else:
                    print('* ',end='')

    for i in range(max-star):
        print(' ',end='')

def printHanoi(floor, s1, s2, s3):
    temp1 = s1.copy()
    temp2 = s2.copy()
    temp3 = s3.copy()
    for i in range(floor, 0, -1):
        if len(temp1) != i:
            stars(floor, 0)
        elif len(temp1) == i:
            stars(floor, temp1.pop())

        if len(temp2) != i:
            stars(floor, 0)
        elif len(temp2) == i:
            stars(floor, temp2.pop())
            
        if len(temp3) != i:
            stars(floor, 0)
        elif len(temp3) == i:
            stars(floor, temp3.pop())
        print()

hanoi(n, 1, 3)
printHanoi(n, stick1, stick2, stick3)


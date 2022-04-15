id = input("")
if len(id) == 10:
    id = str(ord(id[0]) - 55) + id[1:]
    sum = 0
    for n , multiple in zip(id, [1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]):
        sum += int(n) * multiple
    if sum % 10 ==0:
        print('Correct ID')
    else:
        print('Wrong ID')
else:
    print("wrong ID")
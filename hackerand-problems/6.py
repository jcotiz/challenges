numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,30,60]

result = 0

for number in numbers:
    check = 10 / number
    if check == 1 or check < 1:
        result = 2
    else:
        result = 1
    print(f"ammount of digits : {result} number : {number}")
    

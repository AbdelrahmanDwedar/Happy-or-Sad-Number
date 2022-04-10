def findHappyAndSadNumbers(number):
    current_number = number
    sum = 0
    answer = False

    while sum != 1 and sum != 4:
        sum = 0
        
        while current_number > 0:
            digit = current_number % 10
            sum += digit**2
            current_number //= 10
        
        current_number = sum
        if sum == 1:
            answer = True

    if answer == True:
        return f"{number} is a happy number :D"
    else:
        return f"{number} is a sad number :("

print(findHappyAndSadNumbers(3))
print(findHappyAndSadNumbers(7))
print(findHappyAndSadNumbers(19))
print(findHappyAndSadNumbers(82))
print(findHappyAndSadNumbers(4))
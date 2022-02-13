def happyOrSad(number):
    seeen_numbers = []
    current = number

    while number != 1:
        sub = 0

        for i in range(len(str(number))):
            num = str(number)[i]
            sub += (int(num))**2

        if sub in seeen_numbers:
            return f"Sad number"
        else:
            seeen_numbers.append(sub)
            n = sub
    
    return f"Happy number"

print(happyOrSad(3))
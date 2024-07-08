def prime_checker(number):
    result = []
    for i in range(2,number):
        result.append(number % i)
    
    #print(result)
    number_zeros = result.count(0)

    if number_zeros > 1 or number == 1:
        print("It's not a prime")
    else:
        print("It's a prime")

#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)

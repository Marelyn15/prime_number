def is_prime(number):
    number = int(number)
    result = []
    for i in range(2,number + 1):
        result.append(number % i)
        number_zeros = result.count(0)
        
    if number_zeros > 1 or number == 1:
        return False
    else:
        return True
    
print(is_prime(75))
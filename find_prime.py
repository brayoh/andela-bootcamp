def find_prime_number(number):
    prime_numbers = []
    # check if the given input is an integer
    if isinstance(number, int):
        # check if value is negative
        if number < 0:
            raise ValueError("input should be a positive number")
        else:
            for num in range(0, number + 1):
                # prime numbers should be greater than 1
                if num > 1:
                    for i in range(2, num):
                        if num % i == 0:
                            break # skip optional else
                    else:
                        prime_numbers.append(num) # append the prime number to our list
            return prime_numbers

    else:
        raise TypeError("input should be of type integer")

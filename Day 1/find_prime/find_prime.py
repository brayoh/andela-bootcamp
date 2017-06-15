import time

def find_prime_number(number):
    start = time.time() # mark the start of our algorithm to measure time complexity
    prime_numbers = []
    # check if the given input is an integer
    if isinstance(number, int):
        # check if value is negative
        if number < 0:
            raise ValueError("input should be a positive number")
        elif number == 0:
            raise ValueError("input should be greater than 0")
        else:
            for num in range(0, number + 1):
                # prime numbers should be greater than 1
                if num > 1:
                    for i in range(2, num):
                        if num % i == 0:
                            break # skip optional else
                    else:
                        prime_numbers.append(num) # append the prime number to our list

            end = time.time()
            
            print("find_prime_number took {} to execute".format((end - start)))

            return prime_numbers

    else:
        raise TypeError("input should be of type integer")

    end = time.time()

    print(end - start, "this is the time taken to execute")

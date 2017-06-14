def find_max_min(numbers):
    if isinstance(numbers, list):
        min_number = min(numbers)
        max_number = max(numbers)
        if min_number == max_number:
            return [len(numbers)]
        return [min_number, max_number]
    else:
        raise TypeError("expected input should be a list of numbers")

def find_missing(list_one, list_two):
    missing = []
    # check if any list is empty
    if any(len(num) == 0 for num in [list_one, list_two]):
        return 0
     # check if all the elements in the list are the same
    elif any(len(set(nums)) == 1 for nums in [list_one, list_two]):
        return 0
    else:
        for num in list_one:
            if num not in list_two:
                missing.append(num)
        for num in list_two:
            if num not in list_one:
                missing.append(num)

        if len(missing) > 0:
            if len(missing) == 1:
                return missing[0]
            else:
                return missing

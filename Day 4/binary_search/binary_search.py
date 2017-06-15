
class BinarySearch(list):
    """ BinarySearch
        takes 2 paramaters:
        a = length of list to generate
        b = the step difference between consequtive numbers
    """
    def __init__(self, length, step_diff):
        result = []
        for num in self.get_item_list(length, step_diff):
            result.append(num)
            self.append(num)

        self.list = result

    def __getitem__(self, key):
        return list.__getitem__(self, key)

    @property
    def length(self):
        return len(self.list)

    # this method is a generator function,
    # its an iterator that generates values on the fly but doesn't keep them in memory
    # this will help improve the effiency of our program given a bigger input

    def get_item_list(self, item_range, step_diff):
        current = step_diff
        for i in range(item_range):
            yield current

            # assuming diff is 2, since a is 1 the yielded value will be 2 so you add 2 + 2
            # now a will be 4 then you call yield again and a is now equal to 4 so we add 4 + 2
            # now a = 6 and so on.....
            current = step_diff + current

    # this method takes number you want to find as a paramater
    # and returns { count: number_of_times_iterated, index: index_of_the_number }

    def search(self, number):
        numbers = self.list
        result = {'count':0, 'index': -1}
        first_index = 0
        last_index = len(numbers) - 1 # list indexes start from 0 so we minus 1 to cover for that
        found = False

        if number == numbers[first_index]:
            result['index'] = first_index
            return result
        elif number == numbers[last_index]:
            result['index'] = last_index
            return result
        else:
            while first_index <= last_index and not found:
                mid = (first_index + last_index)//2
                result['count'] = result['count'] + 1

                if numbers[mid] == number:
                    found = True
                    result['index'] = mid
                else:
                    if number < numbers[mid]: # lower half
                        numbers = numbers[first_index: mid] # remove the upper part
                        mid = (len(numbers)//2) - 1
                        if numbers[mid] == number:
                            found = True
                            result['index'] = self.list.index(number)

                        last_index = len(numbers) - 1
                    else:  # upper half
                        first_index = mid +1

            try:
                self.list.index(number)
                return result
            except ValueError:
                return { 'count': result['count'], 'index': -1 }

class BinarySearch(object):
    """ BinarySearch
        takes 2 paramaters:
        a = length of list to generate
        b = the step difference between consequtive numbers
    """
    def __init__(self, length, step_diff):
        result = []
        for num in self.get_item_list(length, step_diff):
            result.append(num)

        self.list = sorted(result)
        self.length = len(result);

    @property
    def length(self):
        return self.length

    # this method is a generator function,
    # its an iterator that generates values on the fly but doesn't keep them in memory
    # this will help improve the effiency of our program given a bigger input

    def get_item_list(self, item_range, step_diff):
        current = 1
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
        result = {'count':0}
        first_index = 0
        last_index = len(numbers) - 1 # list indexes start from 0 so we minus 1 to cover for that
        found = False
        find_middle = self.find_middle(numbers)

        while(first_index <= last_index and not found):
            mid = (first_index + last_index)//2
            result['count'] = result['count']  + 1
            if numbers[mid] == number:
                found = True
                result['index'] = mid
            else:
            	if number < numbers[mid]: # lower half
            		last_index = mid - 1
            	else:  # upper half
            		first_index = mid + 1
        return result

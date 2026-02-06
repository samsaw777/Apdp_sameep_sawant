import math
def median(x):
    """
    
    """
    start_index = 0
    end_index = len(x) - 1
    middle_index = (start_index + end_index) / 2
    if len(x) % 2 == 0:
        floor_index = math.floor(middle_index)
        ceil_index = math.ceil(middle_index)
        value = (x[floor_index] + x[ceil_index]) / 2
        return value
    else:
        return x[int(middle_index)]




print(median([1,2,3,4,5]))
print(median([1,2,3,4,5,6]))
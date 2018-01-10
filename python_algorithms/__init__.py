from datetime import datetime
import numpy as np
import pandas as pd

def get_execution_time(func):
    def wrapper(my_array):
        d0 = datetime.now()
        new_array = func(my_array)
        d1 = datetime.now()
        final_time = d1-d0
        return new_array, final_time
    return wrapper


@get_execution_time
def insertion_sort(my_array):
    #k is the index of the value we're looking at right now
    #i is the index of the last value of the previous subarray to which we're comparing the value of my_array[k]
    i = 0
    k = i + 1
    while (k < len(my_array)):
        if (my_array[k] >= my_array[i]):
            #if my_array[k] is bigger than the previous element (i.e. the biggest element in the previous subarray)
            #just move the i and k cursors to the right.
            k += 1
            i += 1
        elif (my_array[k] < my_array[i]):
            val_to_move = my_array[k]
            # we want to keep track of k, but also have a new k 'move' to sort the subarray
            new_k = k
            while (i>=0 and val_to_move < my_array[i]):
                #at i=0, we've looked at the whole subarray. We should quit at that point.
                my_array[new_k] = my_array[i]
                my_array[i] = val_to_move
                #move everything one to the right and the 'bigger value' to the current location
                #move two cursors to the left and repeat
                i -= 1
                new_k -= 1
            # once the subarray is sorted, move the main cursor one to the right and set the last element in the
            # subarray to one element prior
            k += 1
            i = k - 1
    return my_array

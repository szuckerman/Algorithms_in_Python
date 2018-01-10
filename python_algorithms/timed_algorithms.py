from python_algorithms import insertion_sort
import numpy as np
import pandas as pd

time_dict = {pow(10,i): 0 for i in range(5)}


for k in [pow(10,i) for i in range(5)]:
    _, sorted_time = insertion_sort([np.random.randint(k) for _ in range(k)])
    time_dict[k] = sorted_time


df=pd.DataFrame(time_dict, index=time_dict.keys())
df.iloc[1].plot()

my_list = [1,3,9,2,1,1,10,4]
sorted_list, sorted_list_time = insertion_sort(my_list)
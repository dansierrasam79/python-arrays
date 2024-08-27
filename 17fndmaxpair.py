# find highest product in array
from array import *
init_array = array('i', [1,2,3,4,5])
max_prod = []
max_pair = []
for item in init_array:
    for item2 in init_array:
        if init_array.index(item) != init_array.index(item2):
            max_prod.append(item*item2)
            max_pair.append([item,item2])
max_prod_idx =max_prod.index(max(max_prod))
print(max_pair[max_prod_idx])
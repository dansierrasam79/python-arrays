# no duplicates allowed
from array import *
init_array = array('i', [1,2,6,3,4,2,5,2,3])
init_array2 = array('i', [])
for item in init_array:
    if item not in init_array2:
        init_array2.append(item)
if init_array != init_array2:
    print("Yes")
else:
    print("No")
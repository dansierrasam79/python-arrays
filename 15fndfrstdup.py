# find first duplicate or return -1
from array import *
init_array = array('i', [1,2,6,3,4,5])
init_array2 = array('i', [])
duplicates = array('i', [])
for item in init_array:
    if item in init_array2:
        duplicates.append(item)
    init_array2.append(item)
if len(duplicates)==0:
    duplicates.append(-1)
print("First duplicate: ", duplicates[0])

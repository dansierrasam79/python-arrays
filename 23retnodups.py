# remove duplicates and return new array
from array import *
init_array = array("i",[1,2,3,4,5,2,3,4,5])
final_array = array("i",[])
for item in init_array:
    if item not in final_array:
        final_array.append(item)

print("Array without duplicates: ", final_array)

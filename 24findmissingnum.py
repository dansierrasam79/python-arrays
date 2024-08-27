# find missing number between 10 to 20
from array import *
all_nums_array = array("i",[10,11,12,13,14,15,16,17,18,19,20])
first_missing_array = array("i",[10,11,12,13,14,16,17,18,19,20])
sec_missing_array = array("i",[10,11,12,13,14,15,16,17,18,19])
for item in all_nums_array:
    if item not in first_missing_array:
        print("Missing value in first array: ", item)
    if item not in sec_missing_array:
        print("Missing value in second array: ", item)

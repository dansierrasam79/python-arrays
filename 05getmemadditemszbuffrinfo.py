# get mem add, size of items and total mem buffer size
from array import *
init_array = array('i', [2,4,6,8,10,12])
print(init_array.buffer_info())
print(init_array.buffer_info()[1]*init_array.itemsize)
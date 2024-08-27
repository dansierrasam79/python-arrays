# get itemsize of unsigned int and float arrays
from array import *
unsigned_int_array = array("I", [1,2,3,4,5,6])
float_array = array("f", [1.1,2.2,3.3,4.4,5.5])
print(unsigned_int_array.itemsize)
print(float_array.itemsize)

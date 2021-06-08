import ctypes
import pathlib
from albatrostools import get_data
import matplotlib.pyplot as plt

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "libccc.so"
    clib = ctypes.CDLL(libname)
    clib.cross_correlations.restype = ctypes.POINTER(ctypes.c_float)
    clib.cross_correlations.argtypes = ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_uint, ctypes.c_int, ctypes.c_int
    
    #ignore this for testing
    #header,data = get_data(r'../Baseband Data/1621961651.raw',unpack_fast=True,float=True,byte_delta=-8)
    
    #creating all the pointers
    length = 10 #this is the length of your input vectors
    
    A_real_pointer = (ctypes.c_float * length)()
    A_imaginary_pointer = (ctypes.c_float * length)()
    B_real_pointer = (ctypes.c_float * length)()
    B_imaginary_pointer = (ctypes.c_float * length)()
    
    #setting the value for each array
    for i in range(length):
        A_real_pointer[i] = 1
        
    for i in range(length):
        A_imaginary_pointer[i] = 0
        
    for i in range(length):
        B_real_pointer[i] = 1
        
    for i in range(length):
        B_imaginary_pointer[i] = 0
    
    #parameters determining how far we're shifting to each side. This is INCLUDING the startShift and stopShift. To only test one shift number, set these to both be the same.
    startShift = -10
    stopShift = 10
    
    #createing the ouput pointer. It is structured like [0_real, 0_imaginary, 1_real, 1_imaginary, ... (N-1)_real, (N-1)_imaginary]
    outputPointer = (ctypes.c_float * 2 * (stopShift - startShift + 1))
    
    outputPointer = clib.cross_correlations(A_real_pointer, A_imaginary_pointer, B_real_pointer, B_imaginary_pointer, length, startShift, stopShift)
    
    print(list(outputPointer))
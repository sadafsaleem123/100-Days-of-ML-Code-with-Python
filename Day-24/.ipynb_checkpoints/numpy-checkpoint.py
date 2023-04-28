'''
List is slow and numpy is fast. 

One reason is that numpy uses fixed types and list does not. 
Benefit: Because numpy has less bytes of memory so it is faster to read less bytes of memory

Second reason is that numpy has contiguous memory and list has chunks of bytes that are being allocated without sequentially. 
Benefit: It use SIMD Vector proccessing and has effective cache utilization

In list we do insertion, deletion, appending, concatenation. But numppy has much more to it as well.

Numpy can be used for Mathemattics, Plotting, Backend(store images) and Machine Learning stuff.
 
'''

import numpy as np

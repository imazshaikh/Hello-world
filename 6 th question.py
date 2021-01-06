#converting Array with the help of the ASCII-encoded
# I got stuck in import of binascii but when i read it out about it i got to know that contains a number of methods to convert between binary and various ASCII-encoded binary.

import array
import binascii
a = array.array('i', [1,2,3,4,5,6])
print("Original array:")
print('A1:', a)
bytes_array = a.tobytes()
print('Array of bytes:', binascii.hexlify(bytes_array))
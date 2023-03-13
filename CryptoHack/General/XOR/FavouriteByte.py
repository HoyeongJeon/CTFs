'''
1. for loop (0x01 ~ 0xFF)
2. hex_bytes 랑 xor
3. if crypto in 2. -> FLAG! break
'''

# with pwntool

from pwn import *
hex_bytes = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
for i in range(0xFF):
    xored_bytes = xor(hex_bytes, i).decode
    if 'crypto' in xored_bytes:
        print(xored_bytes)
        break
    
# without pwntool


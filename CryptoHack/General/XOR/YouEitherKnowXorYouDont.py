# b'crypto{' => format!

def decode(bytes_a, bytes_b):
    return bytes([a ^ b for a , b in zip(bytes_a, bytes_b)])


hex_bytes = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104') 

partial_flag = b'crypto{'
partial_key = b'myXORkey'

key = b''
for i in range(len(hex_bytes) // len(partial_key)): 
    key += partial_key 
key += partial_key[:2]

print(decode(hex_bytes, key))

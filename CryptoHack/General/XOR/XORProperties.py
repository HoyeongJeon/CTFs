def hex_to_bytes(hex_bytes):
    return bytes.fromhex(hex_bytes)

def xoring(KEY_A,KEY_B):
    return bytes(a ^ b for a , b in zip(KEY_A, KEY_B)) 

KEY1 = hex_to_bytes('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_KEY1 = hex_to_bytes('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
KEY2_KEY3 = hex_to_bytes('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_KEY1_KEY3_KEY2 = hex_to_bytes('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
FLAG = xoring(xoring(FLAG_KEY1_KEY3_KEY2, KEY2_KEY3), KEY1)


print(FLAG)
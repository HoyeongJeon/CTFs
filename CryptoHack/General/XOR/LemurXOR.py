#I've hidden two cool images by XOR with the same secret key so you can't see them!

'''
Lemur ^ S
Flag ^ S

'''
# import numpy as np
# import cv2

# lemur_png = './lemur.png'
# flag_png = './flag.png'

# print(type(lemur_png))
# xored = cv2.bitwise_xor(lemur_png, flag_png)
# cv2.imshow("xored",xored)

from PIL import Image

# Load the two PNG files
lemur = Image.open('./lemur.png')
flag = Image.open('./flag.png')

# Convert the images to raw data
lemur_tobytes = lemur.tobytes()
flag_tobytes = flag.tobytes()

# XOR the two sets of data
result = bytes(a ^ b for a, b in zip(lemur_tobytes, flag_tobytes))

# Save the result to a new PNG file
key = Image.frombytes(lemur.mode, lemur.size, result)

key.show()
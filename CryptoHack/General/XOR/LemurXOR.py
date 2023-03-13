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
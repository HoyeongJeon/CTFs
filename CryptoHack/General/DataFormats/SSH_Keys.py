from cryptography.hazmat.primitives import serialization

def get_modulus_from_pub(filepath):
    with open(filepath,'rb') as f:
        pub_key = serialization.load_ssh_public_key(f.read())
    return pub_key.public_numbers().n

filepath = '/Users/hoyoungjeon/Documents/CTFs/CryptoHack/General/DataFormats/bruce_rsa_public.pub'

modulus = get_modulus_from_pub(filepath)

print(modulus)
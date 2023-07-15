from Crypto.PublicKey import RSA

with open('/Users/hoyoungjeon/Documents/CTFs/CryptoHack/General/DataFormats/rsa_key.pem','r') as f:
    pem_data = f.read()
    
private_key = RSA.import_key(pem_data)

print(private_key.d)
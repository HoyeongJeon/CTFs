from cryptography import x509

with open('/Users/hoyoungjeon/Documents/CTFs/CryptoHack/General/DataFormats/der_file.der', 'rb') as f:
    cert = x509.load_der_x509_certificate(f.read())

modulus = cert.public_key().public_numbers().n

print(modulus)


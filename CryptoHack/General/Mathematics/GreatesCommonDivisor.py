# gcd = 최대공약수

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

print(gcd(66528, 52920))
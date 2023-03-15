def e_gcd(a, b):
    r0, r1 = a, b
    u0, u1, v0, v1 = 1, 0, 0, 1
    while r1:
        p = r0 // r1
        r0, r1 = r1, r0 - p*r1
        u0, u1 = u1, u0 - p*u1
        v0, v1 = v1, v0 - p*v1
    return r0, u0, v0


print(e_gcd(26513,32321))

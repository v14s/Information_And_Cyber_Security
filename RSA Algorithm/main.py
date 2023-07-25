import math
import random

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    msg = int(input("Enter a message msg: "))

    n = p * q
    z = (p - 1) * (q - 1)
    print("The value of z =", z)

    e = 2
    while e < z:
        if gcd(e, z) == 1:
            break
        e += 1
    print("The value of e =", e)

    for i in range(10):
        x = 1 + i * z
        if x % e == 0:
            d = x // e
            break
    print("The value of d =", d)

    c = pow(msg, e) % n
    print("Encrypted message is:", c)

    N = n
    C = c
    msgback = pow(C, d, N)
    print("Decrypted message is:", msgback)

if __name__ == "__main__":
    main()

if __name__ == '__main__':
    # Both the persons will be agreed upon the public keys G and P
    # A prime number P is taken
    print("Enter P:")
    P = int(input())

    # A primitive root for P, G is taken
    print("Enter G:")
    G = int(input())

    print('The Value of P is:', P)
    print('The Value of G is:', G)

    # Alice will choose the private key a
    print("Enter Private key for Alice:")
    a = int(input())
    print('The Private Key a for Alice is:', a)

    # gets the generated key
    x = pow(G, a, P)

    # Bob will choose the private key b
    print("Enter Private Key for Bob:")
    b = int(input())
    print('The Private Key b for Bob is:', b)

    # gets the generated key
    y = pow(G, b, P)
    
    # Secret key for Alice
    ka = pow(y, a, P)
    # Secret key for Bob
    kb = pow(x, b, P)

    print('Secret key for Alice is:', ka)
    print('Secret key for Bob is:', kb)

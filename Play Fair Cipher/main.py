def matrix(x, y, initial):
    return [[initial for _ in range(x)] for _ in range(y)]

def locindex(c):
    loc = []
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
    return loc

def encrypt():
    msg = input("Enter message: ")
    msg = msg.upper().replace(" ", "")
    if len(msg) % 2 != 0:
        msg += 'X'  # Add an extra character to make it even
    i = 0
    encrypted_msg = ""
    while i < len(msg):
        loc = locindex(msg[i])
        loc1 = locindex(msg[i+1])
        if loc[1] == loc1[1]:
            encrypted_msg += "{}{}".format(
                my_matrix[(loc[0] + 1) % 5][loc[1]],
                my_matrix[(loc1[0] + 1) % 5][loc1[1]]
            )
        elif loc[0] == loc1[0]:
            encrypted_msg += "{}{}".format(
                my_matrix[loc[0]][(loc[1] + 1) % 5],
                my_matrix[loc1[0]][(loc1[1] + 1) % 5]
            )
        else:
            encrypted_msg += "{}{}".format(
                my_matrix[loc[0]][loc1[1]],
                my_matrix[loc1[0]][loc[1]]
            )
        i += 2
    print("CIPHER TEXT:", encrypted_msg)

def decrypt():
    msg = input("Enter cipher text: ")
    msg = msg.upper().replace(" ", "")
    i = 0
    decrypted_msg = ""
    while i < len(msg):
        loc = locindex(msg[i])
        loc1 = locindex(msg[i+1])
        if loc[1] == loc1[1]:
            decrypted_msg += "{}{}".format(
                my_matrix[(loc[0] - 1) % 5][loc[1]],
                my_matrix[(loc1[0] - 1) % 5][loc1[1]]
            )
        elif loc[0] == loc1[0]:
            decrypted_msg += "{}{}".format(
                my_matrix[loc[0]][(loc[1] - 1) % 5],
                my_matrix[loc1[0]][(loc1[1] - 1) % 5]
            )
        else:
            decrypted_msg += "{}{}".format(
                my_matrix[loc[0]][loc1[1]],
                my_matrix[loc1[0]][loc[1]]
            )
        i += 2
    print("PLAIN TEXT:", decrypted_msg)

key = input("Enter key: ")
key = key.replace(" ", "").upper()

result = []
for c in key:
    if c not in result:
        if c == 'J':
            result.append('I')
        else:
            result.append(c)

flag = 0
for i in range(65, 91):
    if chr(i) not in result:
        if i == 73 and chr(74) not in result:
            result.append("I")
            flag = 1
        elif flag == 0 and i == 73 or i == 74:
            pass
        else:
            result.append(chr(i))

k = 0
my_matrix = matrix(5, 5, 0)
for i in range(0, 5):
    for j in range(0, 5):
        my_matrix[i][j] = result[k]
        k += 1

while True:
    choice = int(input("\n1. Encryption\n2. Decryption\n3. Exit\nChoose an option: "))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        break
    else:
        print("Choose a correct option.")

# You can Use this code to Encrypt and to decrypt
# To encryp

import math

choice = input("Do you want to encrypt or to Decrypt? Answer with E to encrypt and D to decrypt\n")
ecrypt = "E"


if choice == ecrypt:
    key = float(input("Enter the public key?\n"))
    n = float(input("Enter value of N (pq)\n"))
    m = float(input("Enter Value to encrypt\n"))


        # Encryption c = (msg ^ e) % n
    thec = pow(m, key)
    c = math.fmod(thec, n)
    print("The Modulus===" +str(c))
    print("Encrypted data = ", c)

else:
    key = float(input("Enter the private key?\n"))
    n = float(input("Enter value of N (pq)\n"))
    c = float(input("Enter Value to dencrypt\n"))

    # Decryption m = (c ^ d) % n
    theM = pow(c, key)
    print("The Power===" +str(theM))
    m = math.fmod(theM, n)
    print("The Modulus===" +str(m))
    print("Original Message Sent = ", m)




# This code is used when generating the value of Private and public key
# Run it in console. 

import math

# To check the gcd OF THE TWO NUMBERS
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

# TO CHECK If number is prime or not
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Get values from the user
theP = int(input("Enter p?\n"))
theQ = int(input("Enter q?\n"))
 
if theP !="" and theQ !="":
    if not is_prime(theP) or not is_prime(theQ):
           print("Value of p or q should be prime")
    else:
        p = theP #set value of p to be theP
        q = theQ #set value of q to be theQ

        n = p*q
        e=2
        phi = (p-1)*(q-1)

       
        def circulate(e):
            while (e < phi):
            
                # e must be co-prime to phi and
                # smaller than phi.
                if(gcd(e, phi) == 1):
                    return e
                else:
                    e = e+1
                    circulate(e)

        e= circulate(e)

        # k = 2
        # d = (1 + (k*phi))/e
        d = 1/(math.fmod(e, phi))

        print ("public key, x: " + str(e))
        print ("private key, y: " + str(d))
        print ("The modulo (pq): " + str(n))
else:
    print("Values cannot be null")

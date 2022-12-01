    # The Pseudocode, thinking behind the code generation:

    # Find Input
    # Calculate length of characters
    # check if length is even or odd
    # If even divide by 2 and encrypt
    # If odd, subtract by 1 to make it even and divide by two then encryp
    # Do the reverse to decrypt

def encrypt(firstEnd, secondEnd, theInput):
     firstEnd = int(firstEnd)+1
     secondEnd = int(secondEnd)+1
     firstPart = ""
     secondPart = ""
     for x in range(firstEnd):
        firstPart += theInput[x]
     for x in range(secondEnd-firstEnd):
        secondPart += theInput[firstEnd+x]
    #Now Encrypt by rearranging character appearances
     print("First Part" +firstPart)
     print("Second Part" +secondPart)
     final= secondPart+firstPart
     return ''.join(reversed(final))


def decrypt(firstEnd, secondEnd, theInput):
     firstEnd = int(firstEnd)+1
     secondEnd = int(secondEnd)+1
     firstPart = ""
     secondPart = ""
     for x in range(firstEnd):
        firstPart += theInput[x]
     for x in range(secondEnd-firstEnd):
        theIndex = firstEnd
        secondPart += theInput[theIndex+x]
    #Now Encrypt by rearranging character appearances
     print("First Part" +firstPart)
     print("Second Part" +secondPart)
     final= secondPart+firstPart
     return ''.join(reversed(final))


option = input("Do you want to Encrypt or to Decrypt? Reply with E to encrypt and D to decrypt\n")
if option=="E":
    theInput = input("Enter the value to encrypt?\n")
    Length = len(theInput)
    arrayLen = Length-1 #Last element index
    firstEnd = 0
    secondEnd = 0
    finalChar = ""
    theNewInput = ""

    if Length % 2 == 0:
        firstEnd = (Length/2) - 1
        secondEnd = Length - 1
    else:
        for x in range(Length-1):
            print("Length===" +str(Length-1))
            theNewInput += theInput[x]
            print("The new Input==" + theNewInput)

        finalChar = theInput[arrayLen]   
        theInput = theNewInput
        firstEnd = (len(theInput)/2) - 1
        secondEnd = len(theInput) - 1
        
    # Set Input Values to a string
    encryptedValue = encrypt(firstEnd, secondEnd, theInput)+finalChar
    print("Your Encrypted ciphertext Value====" +encryptedValue)
else:
    theInput = input("Enter the value to decrypt?\n")
    Length = len(theInput)
    arrayLen = Length-1 #Last element index
    firstEnd = 0
    secondEnd = 0
    finalChar = ""
    theNewInput = ""

    if Length % 2 == 0:
        firstEnd = (Length/2) - 1
        secondEnd = Length - 1
    else:
        for x in range(Length-1):
            print("Length===" +str(Length-1))
            theNewInput += theInput[x]
            print("The new Input==" + theNewInput)

        finalChar = theInput[arrayLen]   
        theInput = theNewInput
        firstEnd = (len(theInput)/2) - 1
        secondEnd = len(theInput) - 1

    dencryptedValue = decrypt(firstEnd, secondEnd, theInput)+finalChar
    print("Initial plainText Value ====" +dencryptedValue)
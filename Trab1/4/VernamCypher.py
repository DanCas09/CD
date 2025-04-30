def makeVernamCypher(plainText, theKey):
    if len(plainText) != len(theKey):
        raise ValueError("The length of the plainText and theKey must be the same")
    cipherText = ""
    for i in range(len(plainText)):
        cipherChar = chr(ord(plainText[i]) ^ ord(theKey[i]))
        cipherText += cipherChar
    return cipherText


plainText = "abcabcd"
theKey = "3333333"

cipherText = makeVernamCypher(plainText, theKey)
print("Cipher text:", cipherText)

decryptedText = makeVernamCypher(cipherText, theKey)
print("Decrypted text:", decryptedText)


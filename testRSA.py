import math as m

def rsa(plainText, n, e):
    cipherText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"

    for key in plainText:
        if key in codeChart:
            char = codeChart.index(key)
            c = str(int(m.pow(char, e) % n))
            cipherText += c + " "
    
    return cipherText.strip()


def dechRSA(messageChiffre, d, n):
    plainText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"
    cipherText = messageChiffre.split()

    for c in cipherText:
        char = int(m.pow(int(c), d) % n)
        if char < len(codeChart):
            plainText += codeChart[char]

    return plainText


plaintext = "hib"
n = 33
e = 3
d = 7

ciphertext = rsa(plaintext, n, e)
print(ciphertext)  # Output: "1 13 17"

decryptedText = dechRSA(ciphertext, d, n)
print(decryptedText)  # Output: "hib"


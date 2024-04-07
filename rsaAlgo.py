import math as m

import math as m

def rsa(plainText, n, e):
    cipherText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"

    for i in plainText:
        char = codeChart.index(i)
        c = int(m.pow(char, e) % n)
        cipherText += str(c) + " "
        
    return cipherText


import math as m

def dechRSA(messageChiffre, d, n):
    plainText = ""
    codeChart = "abcdefghijklmnopqrstuvwxyz"
    cipherTextList = messageChiffre.split()

    for i in cipherTextList:
        char = int(i)
        decrypted_char = codeChart[int(m.pow(char, d) % n)]
        plainText += decrypted_char

    return plainText


# def dechRSA(messageChiffre,d,n):
#     plainText = ""
#     codeChart = "abcdefghijklmnopqrstuvwxyz"
#     for i in messageChiffre:
#         # plainText += str(m.pow(i,d)%n)
#         char = m.pow(i,d)%n
#         for key in range(len(codeChart)):
#             if key == char:
#                 plainText += codeChart[key]
#     return plainText


# def dechRSA(cipherText, n, d):
#     plainText = ""
#     codeChart = "abcdefghijklmnopqrstuvwxyz"
#     length = len(cipherText)

#     for i in range(length):
#         char = cipherText[i]
#         decrypted_char = codeChart[int(rsa(char, n, d)) % 26]
#         plainText += decrypted_char

#     return plainText


plaintext = "hello"
n = 33
e = 3
d = 7

ciphertext = rsa(plaintext, n, e)
print(ciphertext)  # Output: "1 13 17"

decryptedText = dechRSA(ciphertext, d, n)
print(decryptedText)  # Output: "hello"

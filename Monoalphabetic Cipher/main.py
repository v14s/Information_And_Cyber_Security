import sys
import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = input("Enter the message: ")
    myKey = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    myMode = input("Enter the mode (encrypt/decrypt): ")
    
    checkValidKey(myKey)
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    
    print('Using key %s' % myKey)
    print('\nThe %sed message is:' % myMode)
    print(translated)

def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    
    if mode == 'decrypt':
        charsA, charsB = charsB, charsA
    
    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol
    
    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

main()

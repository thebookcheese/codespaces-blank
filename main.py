import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def CaesarCipher(text, key):
    newtext = ''
    print(len(alphabet))
    for i in text:
        index = alphabet.index(i)
        newIndex = index + key
        if newIndex <= len(alphabet):
            letter = alphabet[newIndex]
            newtext += letter
        else:
            newIndex = newIndex % len(alphabet)
            print(newIndex)
            letter = alphabet[newIndex]
            newtext += letter
    return newtext

def VigenereCipher(text, key):
    textList = []
    extendedKey = []
    newText = ''
    for i in text:
        Index = alphabet.index(i)
        textList.append(Index)

    for i in range(len(textList)):
        if i < len(alphabet) - 1 or i <= len(key):
            extendedKey.append(alphabet.index(key[i % len(key)]))
        else:
            extendedKey.append(alphabet.index(key[i % len(key)]))
    
    for i in range(len(textList)):
        LetterIndex = textList[i] + extendedKey[i]
        LetterActualIndex = LetterIndex % len(alphabet)
        Letter = alphabet[LetterActualIndex]
        newText = newText + Letter
    return newText

    
            

Cipher = input('What cipher do you want to use \n').lower()
CheckCaesar = re.search('caesar',Cipher)
if CheckCaesar:
    Input = input('What do you want to encrypt \n')
    key = int(input('With what key do you want to encrypt it \n'))
    a = CaesarCipher(Input, key)
    print(a)
else:
    CheckVigenere = re.search('vingenere', Cipher)
    if CheckVigenere:
        Input = input('What do you want to encrypt \n')
        key = input('With what key do you want to encrypt it \n')
        a = VigenereCipher(Input, key)
        print(a)
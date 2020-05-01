from secret import plaintext
import pprint, random, re, string

def decrypt(ciphertext):
    potentialCipherKey = {}

    for character in string.ascii_uppercase:
       potentialCipherKey[character] = set(string.ascii_lowercase)

    deduceAOrI(ciphertext, potentialCipherKey)
    deduceAEOrT(ciphertext, potentialCipherKey)
    deduceEHAndT(ciphertext, potentialCipherKey)

    pprint.pprint(potentialCipherKey)

    partialDecryption = ''

    for character in ciphertext:
        if character.isalpha() and len(potentialCipherKey[character]) == 1:
            partialDecryption += list(potentialCipherKey.get(character))[0]
        else:
            partialDecryption += character

    print(partialDecryption)

def deduceAEOrT(ciphertext, potentialCipherKey):
    frequencyTable = {}

    for character in ciphertext:
        if character.isalpha():
            frequencyTable.setdefault(character, 0)
            frequencyTable[character] += 1
    
    frequencies = list(frequencyTable.values())
    frequenciesCopy = frequencies.copy()
    frequenciesCopy.sort()
    
    threeHighestFrequencies = frequenciesCopy[-3:]
    threeMostCommonLetters = []

    for frequency in threeHighestFrequencies:
        threeMostCommonLetters.append(list(frequencyTable.keys())[frequencies.index(frequency)])

    for character in potentialCipherKey:
        if character in threeMostCommonLetters:
            potentialCipherKey[character] = potentialCipherKey[character].intersection({'a', 'e', 't'})
        else:
            potentialCipherKey[character] = potentialCipherKey[character].difference({'a', 'e', 't'})

def deduceAOrI(ciphertext, potentialCipherKey):
    oneLetterWords = []

    oneLetterWordRegex = re.compile(r' [A-Z] ')
    matchObject = re.findall(oneLetterWordRegex, ciphertext)

    for group in matchObject:
        oneLetterWords.append(str(group).strip())

    print(oneLetterWords)

    oneLetterWords = set(oneLetterWords)

    for character in potentialCipherKey:
        if character in oneLetterWords:
            potentialCipherKey[character] = potentialCipherKey[character].intersection({'a', 'i'})
        else:
            potentialCipherKey[character] = potentialCipherKey[character].difference({'a', 'i'})

def deduceEHAndT(ciphertext, potentialCipherKey):
    threeLetterWords = []

    threeLetterWordsRegex = re.compile(r'\b[A-Z]{3}\b')
    matchObject = re.findall(threeLetterWordsRegex, ciphertext)

    for group in matchObject:
        threeLetterWords.append(group)

    threeLetterWordsFrequencyTable = {}

    for threeLetterWord in threeLetterWords:
        threeLetterWordsFrequencyTable.setdefault(threeLetterWord, 0)
        threeLetterWordsFrequencyTable[threeLetterWord] += 1

    theCanidate = ''
    highestFrequency = 0

    for threeLetterWord, frequency in threeLetterWordsFrequencyTable.items():
        if frequency > highestFrequency:
            highestFrequency = frequency
            theCanidate = threeLetterWord
    
    for character in potentialCipherKey:
        if character in theCanidate:
            if character == theCanidate[0]:
                potentialCipherKey[character] = potentialCipherKey[character].intersection({'t'})
            elif character == theCanidate[1]:
                potentialCipherKey[character] = potentialCipherKey[character].intersection({'h'})
            else:
                potentialCipherKey[character] = potentialCipherKey[character].intersection({'e'})
        else:
            potentialCipherKey[character] = potentialCipherKey[character].difference({'e', 'h', 't'})

# Create random cipher key
def encrypt(plaintext):
    alphabet = string.ascii_lowercase
    cipherKey = list(alphabet)
    random.shuffle(cipherKey)
    cipherkey = ''.join(cipherKey)

    ciphertext = ''

    for character in plaintext.lower():
        if character.isalpha():
            ciphertext += cipherKey[ord(character) - ord('a')].upper()
        else:
            ciphertext += character

    return ciphertext

ciphertext = encrypt(plaintext)
print(ciphertext)
decrypt(ciphertext)
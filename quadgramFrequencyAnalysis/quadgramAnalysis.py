import math, random, re, string

print('What is your ciphertext?')
ciphertext = input().upper()
ciphertext = re.sub(r'[^A-Z]', '', ciphertext)

quadgramsFrequencies = {}
quadgramsTxt = open('english_quadgrams.txt')
quadgramsTxtLines = quadgramsTxt.readlines()

for quadgramsTxtLine in quadgramsTxtLines:
    quadgramsTxtLine = quadgramsTxtLine.split(' ')
    quadgramsFrequencies[quadgramsTxtLine[0]] = int(quadgramsTxtLine[1][:-1])

quadgramsTxt.close()

totalQuadgrams = sum(quadgramsFrequencies.values())

cipherKey = list(string.ascii_uppercase)
random.shuffle(cipherKey)
cipherKey = ''.join(cipherKey)

bestFitness = 0
bestCipherKey = cipherKey

for index in range(len(ciphertext) - 3):
    probability = 0.1 / totalQuadgrams
    logProbability = math.log(probability)
    bestFitness += logProbability

for iteration in range(2000):
    plaintext = ''

    for character in ciphertext:
        plaintext += chr(cipherKey.index(character) + ord('a'))

    fitness = 0
    for index in range(len(plaintext) - 3):
        quadgram = plaintext[index : index + 4].upper()
        
        if quadgram in quadgramsFrequencies:  
            probability = quadgramsFrequencies[quadgram] / totalQuadgrams
        else:
            probability = 0.1 / totalQuadgrams

        logProbability = math.log(probability)
        fitness += logProbability

    if fitness > bestFitness:
        bestFitness = fitness
        bestCipherKey = cipherKey
        print('Current best plaintext is %s with key %s' % (plaintext, cipherKey))

    cipherKey = bestCipherKey

    character1Index = random.randint(0, 25)
    character2Index = random.randint(0, 25)
    temp = cipherKey[character1Index]

    cipherKey = cipherKey[: character1Index] + cipherKey[character2Index] + cipherKey[character1Index + 1 :]
    cipherKey = cipherKey[: character2Index] + temp + cipherKey[character2Index + 1 :]

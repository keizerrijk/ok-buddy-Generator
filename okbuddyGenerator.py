import time
#logo
import logo
import random
#image dictionary
import images
#word dictionary
import leFunnyWords

#welcome message:
print('\n')
myInput = input('Ok, buddy retard, to generate a new epic meme press enter.' + '\n' + '\n')

#meme generation
def memeGeneration():
    time.sleep(1)
    
    #image choice
    imgChoice = input('\n' + 'Choose an image, type: "walter" "cheems" "coomer" "troll" "peter" or "doge" and press enter to continue.' + '\n' '\n')
    if imgChoice == 'cheems':
        img = images.cheems
    elif imgChoice == 'walter':
        img = images.walter
    elif imgChoice == 'doge':
        img = images.doge
    elif imgChoice == 'coomer':
        img = images.coomer
    elif imgChoice == 'peter':
        img = images.peter
    elif imgChoice == 'troll':
        img = images.troll
    else:
        print('Image not found')
        exit
        memeGeneration()
    
    #word generation
    wordGen1 = random.randint(1, 16)
    wordGen2 = random.randint(1, 9)
    wordGen3 = random.randint(1, 10)
    wordGen4 = random.randint(1, 15)
    wordGen5 = random.randint(1, 8)
    print('\n' + 'procemsing 25%')
    time.sleep(1)
    genWord1 = leFunnyWords.word1.get(str(wordGen1))
    genWord2 = leFunnyWords.word2.get(str(wordGen2))
    genWord3 = leFunnyWords.word3.get(str(wordGen3))
    genWord4 = leFunnyWords.word4.get(str(wordGen4))
    genWord5 = leFunnyWords.word5.get(str(wordGen5))

    #"processing" time
    print('procemsing 50%')
    time.sleep(1)
    print('procemsing 75%')
    time.sleep(1)
    print('procemsing 100%' + '\n')
    time.sleep(1)

    #meme displaying
    print(genWord1 + genWord2 + genWord3)
    print(img)
    print(genWord4 + genWord5 + '\n' + '\n')

    #restart or not
    restart = input('Generate another meme? type "yes" or "no"' + '\n')
    if restart == 'yes':
        memeGeneration()
    else:
        exit
    
        
memeGeneration()  





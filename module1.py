from ast import While
from random import randint
def choosing ():
    fhand= open("wordbank.txt" ,'r')
    L=list(fhand)
    while True:
        value = randint(0 ,len(L) - 1)
        phrase = L[value].rstrip()
        words = phrase.lower().replace(" ","")
        print(phrase+"\n"+words)
        if len(list(set(words))) <= 8:            
            print("choosing length is ",len(list(set(words))))
            return phrase
        else: 
            continue

def printing(wordsum,word1,word2,wordsub):
    x =  ' ' * (len(wordsum) - len(word1))
    re = (x,word1)
    x  = ''.join(re)

    y =  ' ' * (len(wordsum) - len(word2))
    rea = (y,word2)
    y  = ''.join(rea)

    z =  ' ' * (len(wordsum) - len(wordsub))
    reb = (z,wordsub)
    z  = ''.join(reb)

    print(wordsum)
    print(x)
    print(y)
    print(z)
    return (wordsum,x,y,z)

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
       ,'n','o','p','q','r','s','t','u','v','w','x','y','z']


word = choosing()
word1 = word.rsplit(" ")[0].replace(" ","").lower()
word2 = word.rsplit(" ")[1].replace(" ","").lower()
word3 = ''
wordsum = ''
wordsub = ''
space = '  '
space1 = '  '

g = list(set(word))
h = list(set(word1 + word2))
print ("set g length is :",len(g))
print ("set h length is :",len(h))

while True:
    dicts = {}
    for i in range(len(h)):#assigning digits to numbers
        while True:
            value = randint(0,9)
            if (value == 0 and (h[i] == word1[0] or h[i] == word2[0])) or (value in dicts.values()):
                continue
            else:
                break
        dicts.update({h[i]:value})#saving current itteration's letter/digit pair into a dictionary

    dictsorted = {}
    for value,key in dicts.items():#flipping key/value in our dictionary into digit/letter in 'dictsorted'
        dictsorted.update({key:value})

    num1 = '0'
    num2 = '0'

    for letter in word1:
        num1 = int(str(num1) + str(dicts[letter]))

    for letter in word2:
        num2 = int(str(num2) + str(dicts[letter]))

    num = int(str(num1)+ str(num2))
    num3 = 0
    flag = False
    if num2 > num1 :
        num3 = num1
        num1 = num2
        num2 = num3
        flag = True

    mysum = num1 + num2
    mysub = num1 - num2

    dictsorted = dict(sorted(dictsorted.items()))#sorting dicsorted into numerical order

    if len(set(str(mysum)+str(num1)+str(num2)+str(mysub))) != 9 :
        continue
    else:
        break

for digit in str(mysum) :#checking if mysum added new digits that don't exist in original expression (most likely do)
    if int(digit) in dictsorted.keys():   
        wordsum = wordsum + str(dictsorted[int(digit)]) #if current digit already exist add it to wordsum
    else :#if current digit do not exist assign new random letter to it from 'abc' list of letters
        while True:
            value = randint(0,25)
            if abc[value] in dictsorted.values():
                continue
            else:
                break
        dicts.update({int(digit):abc[value]})
        dictsorted.update({int(digit):abc[value]})
        dictsorted = dict(sorted(dictsorted.items())) 
        wordsum = wordsum + str(dictsorted[int(digit)])

for digit in str(mysub) :#checking if mysub added new digits that don't exist in original expression (most likely do)
    if int(digit) in dictsorted.keys():   
        wordsub = wordsub + str(dictsorted[int(digit)]) #if current digit already exist add it to wordsub
    else :#if current digit do not exist assign new random letter to it from 'abc' list of letters
        while True:
            value = randint(0,25)
            if abc[value] in dictsorted.values():
                continue
            else:
                break
        dicts.update({int(digit):abc[value]})
        dictsorted.update({int(digit):abc[value]})
        dictsorted = dict(sorted(dictsorted.items())) 
        wordsub = wordsub + str(dictsorted[int(digit)])

if flag:            
    word3 = word1
    word1 = word2
    word2 = word3
    flag = False
    
print("num is :",num,"dicts is :",dicts,"dictsorted is :",dictsorted)
print("length is :",len(set(str(mysum)+str(num1)+str(num2)+str(mysub))))
wordstuple = (printing(wordsum,word1,word2,wordsub))
print(wordstuple)


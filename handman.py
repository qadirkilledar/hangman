import random

def getsingleword():
    with open("words.txt",'r')as word:
        wordlist = word.readlines()
        impureword = wordlist[random.randint(0,len(wordlist)-1
                                             )]
        pureword = impureword.split('\n')
        return pureword[0]

word = getsingleword()
print(word)
    
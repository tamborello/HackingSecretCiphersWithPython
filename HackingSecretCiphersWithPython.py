# https://inventwithpython.com/hacking/
# http://inventwithpython.com/hacking/practice/

# Rather than following all of Al's instructions, I dump all the lesson code into one file (rather than saving a chapter's work into a module to later import) and occasionally change a variable name. Yes, I'm aware that dumping all of the code into one file, rather than writing and importing modules as Al instructs is bad coding practice: more bugs for me to chew on.



# python-shell-switch-to-shell to launch a python shell interactively to pick which shell. Use /usr/bin/python3
# Use shell interpreter args -i --simple-prompt or not?
# Make dedicated process or not?

# C-c C-r to python-shell-send-region

# Chapter 4
print('Hello world!')
print('What is thy name?')
myName=input() # Note this'll throw a NameError in python 2 if I don't surround my entry with quotes.
print('It is good to meet you, ' + myName)

print('Only this')



# Chapter 5
message = "Three can keep a secret if two of them are dead."
translated = ""

message = input('Enter a message to encrypt: ')
translated = ''

i = len(message) - 1
while i >= 0:
 translated = translated + message[i]
 i = i - 1

print(translated)



# Checking Your Source Code with the Online Diff Tool
# Even though you could copy and paste or download this code from this book’s website, it is very helpful to type in this program yourself. This will give you a better idea of what code is in this program. However, you might make some mistakes while typing it in yourself.

# To compare the code you typed to the code that is in this book, you can use the book’s website’s online diff tool. Copy the text of your code and open http://invpy.com/hackingdiff in your web browser. Paste your code into the text field on this web page, and then click the Compare button. The diff tool will show any differences between your code and the code in this book. This is an easy way to find typos that are causing errors.




# Chapter 6: The Caesar Cipher
import pyperclip

message = 'This is my secret message.'

key = 13
mode = 'encrypt' # set to 'encrypt' or 'decrypt'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

message = message.upper()

for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

print(translated)
# pyperclip.copy(translated)

# I got something wrong: The above code, which I transcription typed from the text, does not assign translated text to the variable translated. The below code, pasted from caesarCipher.py provided on the website, does.
# I got my indentation wrong, and that matters because whitespace has meaning in Python. So I'd grouped the latter parts of my code into wrong blocks.

# run the encryption/decryption code on each symbol in the message string
for symbol in message:
    if symbol in LETTERS:
        # get the encrypted (or decrypted) number for this symbol
        num = LETTERS.find(symbol) # get the number of the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # add encrypted/decrypted number's symbol at the end of translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# print the encrypted/decrypted string to the screen
print(translated)





# Now work with all typable ASCII  characters
message = 'This is my secret message.'

message='`uv!-v!-z\'-!rp r"-zr!!ntr;'
key = 13
mode = 'encrypt' # set to 'encrypt' or 'decrypt'
LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\] ^_`abcdefghijklmnopqrstuvwxyz{|}~'
translated = ''
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol
print(translated)





# Chapter 7

message = 'GUVF VF ZL FRPERG ZRFFNTR.'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Loop through every possible key, each time printing the tested key and its translation
for key in range(len(LETTERS)):
    translated = ''
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol
    print('Key #%s: %s' % (key, translated))




# Chapter 8
def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + '|')

def encryptMessage(key, message):
    ciphertext = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key

    return ''.join(ciphertext)

if __name__ == '__main__':
    main()



def addNumbers(a,b):
 return a + b

spam = addNumbers(2, 40)
print(spam)




# Chapter 9
import math #, pyperclip

def main():
 myMessage = 'Cenoonommstmme oo snnio. s s c'
 myKey = 8

 plaintext = decryptMessage(myKey, myMessage)
 print(plaintext + '|')

def decryptMessage(key, message):
 # Although Al's version, which is for Python 3, doesn't cast this value as an int, I found I must because python 2.7 won't do so automatically, and it's important that numOfColumns be an int when used to multiply the sequence that is plaintext.
 numOfColumns = int(math.ceil(len(message) / key))
 numOfRows = key
 numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
 plaintext = [''] * numOfColumns
 col = 0
 row = 0
 for symbol in message:
  plaintext[col] += symbol
  col += 1
  if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
   col = 0
   row += 1

 return ''.join(plaintext)

if __name__ == '__main__':
 main()




# Al's
# Transposition Cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math, pyperclip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the next
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()

# This doesn't decrypt correctly. Is this a python 2 vs 3 thing? Yup, although pyperclip importation breaks in 3. That may have something to do with the fact that I'm executing code by region rather than loading the entire file. If, however, I execute this following code first python shows the cwd as being this file's directory. Then if I execute transpositionDecrypt python will find pyperclip. 
import os
print(os.getcwd())





# Chapter 10
# transpositionTest
import random, sys #, transpositionEncrypt, transpositionDecrypt
def main():
 random.seed(42)
 for i in range(20):
  message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
  message = list(message)
  random.shuffle(message)
  message = ''.join(message)
  print('Test #%s: "%s..."' % (i+1, message[:50]))

  for key in range(1, len(message)):
   encrypted = encryptMessage(key, message)
   decrypted = decryptMessage(key, encrypted)

   if message != decrypted:
    print('Mismatch with key %s and message %s.' % (key, message))
    print(decrypted)
    sys.exit()

  print('Transposition cipher test passed.')

if __name__ == '__main__':
 main(
)




# Chapter 11
# Fun with files!
import time, os, sys # transpositionEncrypt, transpositionDecrypt

def main():
 inputFilename = 'frankenstein.encrypted.txt'
 outputFilename = 'frankenstein.decrypted.txt'
 # Can Python deal with variable names beginning with capital letters?
 Key = 10
 Mode = 'decrypt'

 if not os.path.exists(inputFilename):
  print('The file %s does not exist. Quitting...' % (inputfilename))
  sys.exit()

 if os.path.exists(outputFilename):
  print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
  response = input('> ')
  if not response.lower().startswith('c'):
   sys.exit()

 fileObj = open(inputFilename)
 content = fileObj.read()
 fileObj.close()

 print('%sing...' % (Mode.title()))

 startTime = time.time()
 if Mode =='encrypt':
  translated = encryptMessage(Key, content)
 elif Mode == 'decrypt':
  translated = decryptMessage(Key, content)
 totalTime = round(time.time() - startTime, 2)
 print('%sion time: %s seconds' % (Mode.title(), totalTime))

 outputFileObj = open(outputFilename, 'w')
 outputFileObj.write(translated)
 outputFileObj.close()

 print('Done %sing %s (%s characters).' % (Mode, inputFilename, len(content)))
 print('%sed file is %s.' % (Mode.title(), outputFilename))

if __name__ == '__main__':
 main()



# Chapter 12
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
 dictionaryFile = open('dictionary.txt')
 englishWords = {}
 for word in dictionaryFile.read().split('\n'):
  englishWords[word] = None # what's this = None business?
 dictionaryFile.close()
 return englishWords

ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
 message = message.upper()
 message = removeNonLetters(message)
 possibleWords = message.split()

 if possibleWords == []:
  return 0.0

 matches = 0
 for word in possibleWords:
  if word in ENGLISH_WORDS:
   matches += 1
 return float(matches) / len(possibleWords)

def removeNonLetters(message):
 lettersOnly = []
 for symbol in message:
  if symbol in LETTERS_AND_SPACE:
   lettersOnly.append(symbol)
 return ''.join(lettersOnly)

def isEnglish(message, wordPercentage=20, letterPercentage=85):
 wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
 numLetters = len(removeNonLetters(message))
 messageLettersPercentage = float(numLetters) / len(message) * 100
 lettersMatch = messageLettersPercentage >= letterPercentage
 return wordsMatch and lettersMatch


# Chapter 13
def main():
 TheMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri
ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu eacBoltaetee
oinebcdkyremdteghn.aa2r81a condari fmps" tad   l t oisn sit u1rnd stara nvhn fs
edbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h  a
ihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.
rteoh add e,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai. sl1rchdnheev sh
meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da' eN eMp a
ffn Fc1o ge eohg dere.eec s nfap yox hla yon. lnrnsreaBoa t,e eitsw il ulpbdofg
BRe bwlmprraio po  droB wtinue r Pieno nc ayieeto'lulcih sfnc  ownaSserbereiaSm
-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

 hackedMessage = hackTransposition(TheMessage)

 if hackedMessage == None:
  print('Failed to hack encryption.')
 else:
  print('Copying hacked message to clipboard:')
  print(hackedMessage)
  pyperclip.copy(hackedMessage)

def hackTransposition(message):
 print('Hacking...')
 print('(Press C-c, C-d, or C-g to quit at any time.)')

 # Attempt brute force
 for key in range(1, len(message)):
  print('Trying key #%s...' % (key))

  decryptedText = decryptMessage(key, message)

  if isEnglish(decryptedText):
   print()
   print('Possible encryption hack:')
   print('Key %s: %s' % (key, decryptedText[:100]))
   print()
   print('Enter D for done, or just press Enter to continue hacking:')
   response = input('> ')

   if response.strip().upper().startswith('D'):
    return decryptedText

 return None

if __name__ == '__main__':
 main()

# hackTransposition never finds a successful key, unlike Al's example, decrypting key=10 does not lead to an English message, although encrypt and decrypt pass their tests above. Is something else broken or is he messing with me?

msg = encryptMessage(42, """This chapter was short like the “Breaking the Caesar Cipher with the Brute-Force Technique” chapter because (also like that chapter) most of the code was already written in other programs. Our hacking program can import functions from these other programs by importing them as modules.

The strip() string method is useful for removing whitespace (or other) characters from the beginning or end of a string. If we use triple quotes, then a string value can span across multiple lines in our source code.

The detectEnglish.py program removes a lot of the work of inspecting the decrypted output to see if it’s English. This allows the brute-force technique to be applied to a cipher that can have thousands of keys.

... ... ... ... ... ... Our programs are becoming more sophisticated. Before we learn the next cipher, we should learn how to use Python’s debugger tool to help us find bugs in our programs.""")

# msg is now a suitably-encrypted version of the above text

decryptMessage(42, msg) # returns the original text




# Chapter 14
# cryptomath module
def gcd(a, b):
 while a != 0:
  a, b = b % a, a
 return b


def findModInverse(a, m): # via Euclid's Extended Algorithm
 if gcd(a, m) != 1:
  return None # no mod inverse exists if a & m aren't relatively prime
 u1, u2, u3 = 1, 0, a
 v1, v2, v3 = 0, 1, m
 while v3 != 0:
  q = u3 // v3 # // is the integer division operator
  v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
 return u1 % m


# Chapter 15
import pyperclip, random
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front... um, note that Al's version has space in it twice: once at 0 and once at 62, and that len(SYMBOLS) returns 96, not 95. I had trouble hacking anything until I deleted the space at position 62.

def main():
 TheMessage = """A computer would deserve to be called intelligent if it could deceive a human into beliving that it was human." -Alan Turing"""
 TheKey = getRandomKey()
 TheMode = 'encrypt' # set to 'encrypt' or 'decrypt'

 if TheMode == 'encrypt':
  translated = encryptMessage(TheKey, TheMessage)
 elif TheMode == 'decrypt':
  translated = decryptMessage(TheKey, TheMessage)
 print('Key: %s' % (TheKey))
 print('%sed text:' % (TheMode.title()))
 print(translated)
 pyperclip.copy(translated)
 print('Full %sed text copied to clipboard.' % (TheMode))

def getKeyParts(key):
 keyA = key // len(SYMBOLS)
 keyB = key % len(SYMBOLS)
 return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
# Why exit the python process? Just print instead.
 if keyA == 1 and mode == 'encrypt':
  print('The affine cipher becomes too weak when key A is 1. Choose a different key.')
 if keyB == 0 and mode == 'encrypt':
  print('The affine cipher becomes too weak when key B is 0. Choose a different key.')
 if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
  print('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
 if gcd(keyA, len(SYMBOLS)) != 1:
  print('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))
 else:
  return 'Key A and Key B are okay.'

def encryptMessage(key, message):
 keyA, keyB = getKeyParts(key)
 # I want this to stop execution and not exit the python shell process that I have running in an Emacs inferior mode if the keys are not okay
 if checkKeys(keyA, keyB, 'encrypt') != 'Key A and Key B are okay.':
  return None
 ciphertext = ''
 for symbol in message:
  if symbol in SYMBOLS:
   # encrypt this symbol
   symIndex = SYMBOLS.find(symbol)
   ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
  else:
   ciphertext += symbol # just append this symbol unencrypted
 return ciphertext

def decryptMessage(key, message):
 keyA, keyB = getKeyParts(key)
 checkKeys(keyA, keyB, 'decrypt')
 plaintext = ''
 modInverseOfKeyA = findModInverse(keyA, len(SYMBOLS))

 for symbol in message:
  if symbol in SYMBOLS:
   # decrypt this symbol
   symIndex = SYMBOLS.find(symbol)
   plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
  else:
   plaintext += symbol # just append this symbol undecrypted
 return plaintext

def getRandomKey():
 while True:
  keyA = random.randint(2, len(SYMBOLS))
  keyB = random.randint(2, len(SYMBOLS))
  if gcd(keyA, len(SYMBOLS)) == 1:
   return keyA * len(SYMBOLS) + keyB


# Chapter 16: Hacking the Affine Cipher
import pyperclip

SILENT_MODE = False

def main():
 TheMessage = """U&'<3dJ^Gjx'-3^MS'Sj0jxuj'G3'%j'<mMMjS'g{GjMMg9j{G'g"'gG '<3^MS'Sj<jguj'm'P^dm{'g{G3'%jMgjug{9'GPmG'gG'-m0'P^dm{LU'5&Mm{'_^xg{9"""

 hackedMessage = hackAffine(TheMessage)

 if hackedMessage != None:
  print('Copying hacked message to the clipboard:')
  print(hackedMessage)
  pyperclip.copy(hackedMessage)
 else:
  print('Failed to hack encryption.')

def hackAffine(message):
 print('Hacking...')
 print('(Press Ctrl-D or Ctrl-D to quit at any time.)')

 for key in range(len(SYMBOLS) ** 2):
  keyA = getKeyParts(key)[0]
  if gcd(keyA, len(SYMBOLS)) != 1:
   continue

  decryptedText = decryptMessage(key, message)
  if not SILENT_MODE:
   print('Tried Key %s... (%s)' % (key, decryptedText[:40]))

  if isEnglish(decryptedText):
   print()
   print('Possible encryption hack:')
   print('Key: %s' % (key))
   print('Decrypted message: ' + decryptedText[:200])
   print()
   print('Enter D for done, or just press Enter to continue hacking:')
   response = input('> ')

   if response.strip().upper().startswith('D'):
    return decryptedText

 return None



# Chapter 17: The Simple Substitution Cipher
# The simple substitution cipher simply subtitutes one symbol for another. How many potential combinations of plaintext & ciphertext alphabets are there? 26! = ...
def factorial(n):
 fact = 1
 while n > 1:
  fact, n = fact * n, n - 1
 return fact
# See http://invpy.com/factorial/

import pyperclip, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
 TheMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. -Bertrand Russell'
 TheKey = getRandomKey()
 TheMode = 'encrypt'

# Don't exit the python process if there's an error, instead exit the script and return to the python process shell prompt
 if checkValidKey(TheKey) != 'keyOkay':
  return None

 if TheMode =='encrypt':
  translated = encryptMessage(TheKey, TheMessage)
 elif TheMode == 'decrypt':
  translated = decryptMessage(TheKey, TheMessage)
 print('Using key %s' % (TheKey))
 print('The %sed message is:' % (TheMode))
 print(translated)
 pyperclip.copy(translated)
 print()
 print('Copied message to clipboard')

def checkValidKey(key):
 keyList = list(key)
 lettersList = list(LETTERS)
 keyList.sort()
 lettersList.sort()
 if keyList != lettersList:
  print('There is an error in the key or symbol set.')
  return 'keyError'
 else:
  return 'keyOkay'

def encryptMessage(key, message):
 return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
 return translateMessage(key, message, 'decrypt') # Whoops! I'd accidentally typed 'encrypt' here when In transcription typed the program from Ch 17!

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



# A longer character set would be more secure. How about encrypting all 95 typable ASCII characters? Note that the more secure version is apparently too secure for Chapter 18's hack method.
LETTERS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def translateMessage(key, message, mode):
 translated = ''
 charsA = LETTERS
 charsB = key
 if mode == 'decrypt':
  charsA, charsB = charsB, charsA

 for symbol in message:
  if symbol.upper() in charsA:
   symIndex = charsA.find(symbol)
   translated += charsB[symIndex]
  else:
   translated += symbol

 return translated






# Chapter 18
# First, make our word patterns and cipherletter mappings.
import pprint

def getWordPattern(word):
 word = word.upper()
 nextNum = 0
 letterNums = {}
 wordPattern = []

 for letter in word:
  if letter not in letterNums:
   letterNums[letter] = str(nextNum)
   nextNum += 1
  wordPattern.append(letterNums[letter])
 return '.'.join(wordPattern)

def makeWordPatterns():
 allPatterns = {}
 
 fo = open('dictionary.txt')
 wordList = fo.read().split('\n')
 fo.close()

 for word in wordList:
  pattern = getWordPattern(word)

  if pattern not in allPatterns:
   allPatterns[pattern] = [word]
  else:
   allPatterns[pattern].append(word)

 fo = open('wordPatterns.py', 'w')
 fo.write('allPatterns = ')
 fo.write(pprint.pformat(allPatterns))
 fo.close()

# Now use those word patterns and cipherletter mappings to hack the simple substitution cipher.
import os, re, copy, pprint, pyperclip

if not os.path.exists('wordPatterns.py'):
 makeWordPatterns()
import wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def simpleSubHacker():
 message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

 # Determine the possible valid ciphertext translations.
 print('Hacking...')
 letterMapping = hackSimpleSub(message)

 # Display the results to the user
 print('Mapping:')
 pprint.pprint(letterMapping)
 print()
 print('Original ciphertext:')
 print(message)
 print()
 print('Copying hacked message to clipboard:')
 hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
 pyperclip.copy(hackedMessage)
 print(hackedMessage)

def getBlankCipherletterMapping():
 # Returns a dictionary value that is a blank cipherletter mapping
 return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addLettersToMapping(letterMapping, cipherword, candidate):
 # The letterMapping parameter is a "cipherletter mapping" dictionary
 # value that the return value of this function starts as a copy of.
 # The cipherword parameter is a string value of the ciphertext word.
 # The candidate parameter is a possible English word that the
 # cipherword could decrypt to.

 # This function adds the letters of the candidate as potential
 # decryption letters for the cipherletters in the cipherletter
 # mapping.

 letterMapping = copy.deepcopy(letterMapping)
 for i in range(len(cipherword)):
  if candidate[i] not in letterMapping[cipherword[i]]:
   letterMapping[cipherword[i]].append(candidate[i])
 return letterMapping


def intersectMappings(mapA, mapB):
 # To interesect two maps, create a blank map, then add only the potential decryption letters if they exist in BOTH maps.
 intersectedMapping = getBlankCipherletterMapping()
 for letter in LETTERS:

  # An empty list means "any letter is possible". In this case just copy the other map entirely.
  if mapA[letter] == []:
   intersectedMapping[letter] = copy.deepcopy(mapB[letter])
  elif mapB[letter] == []:
   intersectedMapping[letter] = copy.deepcopy(mapA[letter])
  else:
   # If a letter in mapA[letter] exists in mapB[letter], add that letter to intersectedMapping[letter].
   for mappedLetter in mapA[letter]:
    if mappedLetter in mapB[letter]:
     intersectedMapping[letter].append(mappedLetter)

 return intersectedMapping


def removeSolvedLettersFromMapping(letterMapping):
 letterMapping = copy.deepcopy(letterMapping)
 loopAgain = True
 while loopAgain:
  loopAgain = False
  solvedLetters = []
  for cipherletter in LETTERS:
   if len(letterMapping[cipherletter]) == 1:
    solvedLetters.append(letterMapping[cipherletter][0])

  for cipherletter in LETTERS:
   for s in solvedLetters:
    if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
     letterMapping[cipherletter].remove(s)
     if len(letterMapping[cipherletter]) == 1:
      loopAgain = True
 return letterMapping


def hackSimpleSub(message):
 intersectedMap = getBlankCipherletterMapping()
 cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
 for cipherword in cipherwordList:
  newMap = getBlankCipherletterMapping()

  wordPattern = getWordPattern(cipherword)
  if wordPattern not in wordPatterns.allPatterns:
   continue

  for candidate in wordPatterns.allPatterns[wordPattern]:
   newMap = addLettersToMapping(newMap, cipherword, candidate)

  intersectedMap = intersectMappings(intersectedMap, newMap)

 return removeSolvedLettersFromMapping(intersectedMap)


def decryptWithCipherletterMapping(ciphertext, letterMapping):
 key = ['x'] * len(LETTERS)
 for cipherletter in LETTERS:
  if len(letterMapping[cipherletter]) == 1:
   keyIndex = LETTERS.find(letterMapping[cipherletter][0])
   key[keyIndex] = cipherletter
  else:
   ciphertext = ciphertext.replace(cipherletter.lower(), '_')
   ciphertext = ciphertext.replace(cipherletter.upper(), '_')
 key = ''.join(key) # Aha! I got the TypeError: 'str' object does not support item assignment error because this line was indented one too many whitespaces!

 return decryptMessage(key, ciphertext) # simpleSubCipher


def AlsDecryptWithCipherletterMapping(ciphertext, letterMapping):
    # Return a string of the ciphertext decrypted with the letter mapping,
    # with any ambiguous decrypted letters replaced with an _ underscore.

    # First create a simple sub key from the letterMapping mapping.
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext.
    return decryptMessage(key, ciphertext)



# How to get candidate translations for cipherword
candidates = wordPatterns.allPatterns[getWordPattern('PLQRZKBZB')]

# How to add mappings for multiple candidates to a letter mapping:
for candidate in candidates:
 letterMapping3 = addLettersToMapping(letterMapping3, 'MPBKSSIPLC', candidate)






# Chapter 19: The Vigenère Cipher
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenereCipher():
 TheMessage = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
# """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist. He was highly influential in the development of computer science, providing a formalisation of the concepts of "algorithm" and "computation" with the Turing machine. Turing is widely considered to be the father of computer science and artificial intelligence. During World War II, Turing worked for the Government Code and Cypher School (GCCS) at Bletchley Park, Britain's codebreaking centre. For a time he was head of Hut 8, the section responsible for German naval cryptanalysis. He devised a number of techniques for breaking German ciphers, including the method of the bombe, an electromechanical machine that could find settings for the Enigma machine. After the war he worked at the National Physical Laboratory, where he created one of the first designs for a stored-program computer, the ACE. In 1948 Turing joined Max Newman's Computing Laboratory at Manchester University, where he assisted in the development of the Manchester computers and became interested in mathematical biology. He wrote a paper on the chemical basis of morphogenesis, and predicted oscillating chemical reactions such as the Belousov-Zhabotinsky reaction, which were first observed in the 1960s. Turing's homosexuality resulted in a criminal prosecution in 1952, when homosexual acts were still illegal in the United Kingdom. He accepted treatment with female hormones (chemical castration) as an alternative to prison. Turing died in 1954, just over two weeks before his 42nd birthday, from cyanide poisoning. An inquest determined that his death was suicide; his mother and some others believed his death was accidental. On 10 September 2009, following an Internet campaign, British Prime Minister Gordon Brown made an official public apology on behalf of the British government for "the appalling way he was treated." As of May 2012 a private member's bill was before the House of Lords which would grant Turing a statutory pardon if enacted."""
 TheKey = 'ASIMOV'
 TheMode = 'decrypt'

 if TheMode == 'encrypt':
  translated = encryptMessage(TheKey, TheMessage)
 elif TheMode == 'decrypt':
  translated = decryptMessage(TheKey, TheMessage)

 print('%sed message:' % (TheMode.title()))
 print(translated)
 pyperclip.copy(translated)
 print()
 print('Message copied to clipboard')


def encryptMessage(key, message):
 return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
 return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
 translated = []

 keyIndex = 0
 key = key.upper()

 for symbol in message:
  num = LETTERS.find(symbol.upper())
  if num != -1:
   if mode == 'encrypt':
    num += LETTERS.find(key[keyIndex])
   elif mode == 'decrypt':
    num -= LETTERS.find(key[keyIndex])

   num %= len(LETTERS)

   if symbol.isupper():
    translated.append(LETTERS[num])
   elif symbol.islower():
    translated.append(LETTERS[num].lower())

   keyIndex += 1
   if keyIndex == len(key):
    keyIndex = 0

  else:
   translated.append(symbol)

 return ''.join(translated)




# Chapter 20: Frequency Analysis

# Frequency Finder
# frequency taken from http://en.wikipedia.org/wiki/Letter_frequency
englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getLetterCount(message):
 letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

 for letter in message.upper():
  if letter in LETTERS:
   letterCount[letter] += 1

 return letterCount


def getItemAtIndexZero(x):
 return x[0]

def getFrequencyOrder(message):
 letterToFreq = getLetterCount(message)

 freqToLetter = {}
 for letter in LETTERS:
  if letterToFreq[letter] not in freqToLetter:
   freqToLetter[letterToFreq[letter]] = [letter]
  else:
   freqToLetter[letterToFreq[letter]].append(letter)

 for freq in freqToLetter:
  freqToLetter[freq].sort(key=ETAOIN.find, reverse=True)
  freqToLetter[freq] = ''.join(freqToLetter[freq])

 freqPairs = list(freqToLetter.items())
 freqPairs.sort(key=getItemAtIndexZero, reverse=True)

 freqOrder = []
 for freqPair in freqPairs:
  freqOrder.append(freqPair[1])

 return ''.join(freqOrder)


def englishFreqMatchScore(message):
# print('Debug: message parameter passed to subroutine englishFreqMatchScore: %s' % message)
# print()
 freqOrder = getFrequencyOrder(message)
# print('Debug: freqOrder as computed by getFrequencyOrder on local variable message: %s' % freqOrder)
# print()

 matchScore = 0
 for commonLetter in ETAOIN[:6]:
  if commonLetter in freqOrder[:6]:
   matchScore += 1
 for uncommonLetter in ETAOIN[-6:]:
  if uncommonLetter in freqOrder[-6:]:
   matchScore += 1

 return matchScore


# Chapter 21: Hacking the Vigenère Cipher
# Dictionary Attack Program
def dictionaryAttack():
 ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
 hackedMessage = hackVigenere(ciphertext)

 if hackedMessage != None:
  print('Copying hacked message to clipboard:')
  print(hackedMessage)
  pyperclip.copy(hackedMessage)

 else:
  print('Failed to hack encryption.')

    
def hackVigenere(ciphertext):
 fo = open('dictionary.txt')
 words = fo.readlines()
 fo.close()

 for word in words:
  word = word.strip()
  decryptedText = decryptMessage(word, ciphertext) # vigenereCipher.decryptMessage
  if isEnglish(decryptedText, wordPercentage=40): # detectEnglish.isEnglish
   print()
   print('Possible encryption break:')
   print('Key ' + str(word) + ': ' + decryptedText[:1000])
   print()
   print('Enter D for done, or just press Return to continue breaking:')
   response = input('> ')
   
   if response.upper().startswith('D'):
    return decryptedText



import itertools, re
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False
NUM_MOST_FREQ_LETTERS = 4
MAX_KEY_LENGTH = 16
NONLETTERS_PATTERN = re.compile('[^A-Z]')

def vigenereCipherHacker():
 ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg (GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb a kbmhptgzk dvrvwz wa efiohzd."""
 hackedMessage = hackVigenere(ciphertext)

 if hackedMessage != None:
  print('Copying hacked message to clipboard:')
  print(hackedMessage)
  pyperclip.copy(hackedMessage)
 else:
  print('Failed to hack encryption.')


def findRepeatSequencesSpacings(message):
 message = NONLETTERS_PATTERN.sub('', message.upper())

 seqSpacings = {}
 for seqLen in range(3, 6):
  for seqStart in range(len(message) - seqLen):
   seq = message[seqStart:seqStart + seqLen]

   for i in range(seqStart + seqLen, len(message) - seqLen):
    if message[i:i + seqLen] == seq:
     if seq not in seqSpacings:
      seqSpacings[seq] = []

      seqSpacings[seq].append(i - seqStart)
 return seqSpacings


def getUsefulFactors(num):
 if num < 2:
  return[]
 factors = []

 for i in range(2, MAX_KEY_LENGTH + 1): 
  if num % i == 0:
   factors.append(i)
   factors.append(int(num / i))
  if 1 in factors:
   factors.remove(1)
  return list(set(factors))


def getItemAtIndexOne(x):
 return x[1]


def getMostCommonFactors(seqFactors):
 factorCounts = {}

 for seq in seqFactors:
  factorList = seqFactors[seq]
  for factor in factorList:
   if factor not in factorCounts:
    factorCounts[factor] = 0
   factorCounts[factor] += 1

 factorsByCount = []
 for factor in factorCounts:
  if factor <= MAX_KEY_LENGTH:
   factorsByCount.append( (factor, factorCounts[factor]) )

 factorsByCount.sort(key=getItemAtIndexOne, reverse=True)
  
 return factorsByCount


def kasiskiExamination(ciphertext):
 repeatedSeqSpacings = findRepeatSequencesSpacings(ciphertext)
 seqFactors = {}
 for seq in repeatedSeqSpacings:
  seqFactors[seq] = []
  for spacing in repeatedSeqSpacings[seq]:
   seqFactors[seq].extend(getUsefulFactors(spacing))
 factorsByCount = getMostCommonFactors(seqFactors)
 allLikelyKeyLengths = []
 for twoIntTuple in factorsByCount:
  allLikelyKeyLengths.append(twoIntTuple[0])
 return allLikelyKeyLengths


def getNthSubkeysLetters(n, keyLength, message):
 message = NONLETTERS_PATTERN.sub('', message)

 i = n - 1
 letters = []
 while i < len(message):
  letters.append(message[i])
  i += keyLength
 return ''.join(letters)


def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
# debug
# print('attemptHackWithKeyLength(%s, %s)' % (ciphertext, mostLikelyKeyLength))

 ciphertextUp = ciphertext.upper()
 allFreqScores = []
 for nth in range(1, mostLikelyKeyLength + 1):
  nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

  freqScores = []
  for possibleKey in LETTERS:
   decryptedText = decryptMessage(possibleKey, nthLetters)
   keyAndFreqMatchTuple = (possibleKey, englishFreqMatchScore(decryptedText))
   freqScores.append(keyAndFreqMatchTuple)

  freqScores.sort(key=getItemAtIndexOne, reverse=True)
  allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

 if not SILENT_MODE:
  for i in range(len(allFreqScores)):
   print('Possible letters for letter %s of the key: ' % (i + 1), end='')
   for freqScore in allFreqScores[i]:
    print('%s ' % freqScore[0], end='')
   print()

 for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=mostLikelyKeyLength):
  possibleKey = ''
  for i in range(mostLikelyKeyLength):
   possibleKey += allFreqScores[i][indexes[i]][0]

  if not SILENT_MODE:
   print('Attempting with key: %s' % (possibleKey))

  decryptedText = decryptMessage(possibleKey, ciphertextUp)

# debug
  print('decryptedText: %s' % decryptedText)

  if isEnglish(decryptedText):
   origCase = []
   for i in range(len(ciphertext)):
    if ciphertext[i].isupper():
     origCase.append(decryptedText[i].upper())
    else:
     origCase.append(decryptedText[i].lower())
   decryptedText = ''.join(origCase)

   print('Possible encryption hack with the key %s:' % (possibleKey))
   print(decryptedText[:200])
   print()
   print('Enter D for done or press Return to continue hacking:')
   response = input('> ')

   if response.strip().upper().startswith('D'):
    return decryptedText

 return None


def hackVigenere(ciphertext):
 allLikelyKeyLengths = kasiskiExamination(ciphertext)
 if not SILENT_MODE:
  keyLengthStr = ''
  for keyLength in allLikelyKeyLengths:
   keyLengthStr += '%s ' % (keyLength)
  print('Kasiski Examination results say the most likely key lengths are: ' + keyLengthStr + '\n')

 for keyLength in allLikelyKeyLengths:
  if not SILENT_MODE:
   print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
  hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
  if hackedMessage != None:
   break

 if hackedMessage == None:
  if not SILENT_MODE:
   print('Unable to hack message with likely key length(s). Brute-forcing key length...')
  for keyLength in range(1, MAX_KEY_LENGTH + 1):
   if keyLength not in allLikelyKeyLengths:
    if not SILENT_MODE:
     print('Attempting hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
    hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
    if hackedMessage != None:
     break
 return hackedMessage






# Chapter 22: The One-Time Pad Cipher


# Chapter 23: Finding Prime Numbers
# primeSieve module

import math

def isPrime(num):
 if num < 2:
  return False

 for i in range(2, int(math.sqrt(num)) + 1):
  if num % i == 0:
   return False
 return True


def primeSieve(sieveSize):
 sieve = [True] * sieveSize
 sieve[0] = False
 sieve[1] = False

 for i in range(2, int(math.sqrt(sieveSize)) + 1):
  pointer = i * 2
  while pointer < sieveSize:
   sieve[pointer] = False
   pointer += i

 primes = []
 for i in range(sieveSize):
  if sieve[i] == True:
   primes.append(i)

 return primes
# How does primeSieve(>=20) skip 9 and 15? Oh right, because it increments pointer by i, meaning it marks as false in multiples of i.

import random

def rabinMiller(num):
 s = num - 1
 t = 0
 while s % 2 == 0:
  s = s // 2
  t += 1

 for trials in range(5):
  a = random.randrange(2, num - 1)
  v = pow(a, s, num)
  if v != 1:
   i = 0
   while v != (num - 1):
    if i == t - 1:
     return False
    else:
     i = i + 1
     v = (v ** 2) % num
 return True



def isPrime(num):
 if (num < 2):
  return False

 lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]




 if num in lowPrimes:
  return True

 for prime in lowPrimes:
  if (num % prime ==0):
   return False

 return rabinMiller(num)


def generateLargePrime(keysize=1024):
 while True:
  num = random.randrange(2**(keysize-1), 2**(keysize))
  if isPrime(num):
   return num




# Chapter 24: Public Key Cryptography And The RSA Cipher
# rsaKeygen module
import random, sys, os

def rsaKeygen():
 print('Making key files...')
 makeKeyFiles('fpt', 1024)
 print('Key files made.')


def generateKey(keySize):
 print('Generating p prime...')
 p = generateLargePrime(keySize)
 print('Generating q prime...')
 q = generateLargePrime(keySize)
 n = p * q

# debug
 print('\nGenerateKey:\np: %s\nq: %s\nn: %s\n' % (p, q, n))

 print('Generating an e value that is relatively prime to (p - 1) * (q - 1)...')
 while True:
  e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
  if gcd(e, (p - 1) * (q - 1)) == 1:
   break

 print('Calculating a d value that is mod inverse of e...')
 d = findModInverse(e, (p - 1) * (q - 1))

#  publicKey = (n, 3) Haha! I was wondering if 3 was a reasonable value for e!

 publicKey = (n, e)
 privateKey = (n, d)

 print('Public key:', publicKey)
 print('Private key:', privateKey)

 return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
 if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_prikey.txt' % (name)):
  print('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))
  return None

# debug
 print('\nMakeKeyFiles\' KeySize: %s\n' % keySize) 

 publicKey, privateKey = generateKey(keySize)

 print()
 print('The public key is a pair of %s and %s digit numbers.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
 print('Writing public key to file %s_pubkey.txt...' % (name))
 fo = open('%s_pubkey.txt' % (name), 'w')
 fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
 fo.close()

 print()
 print('The private key is a pair of %s and %s digit numbers.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
 print('Writing private key to file %s_prikey.txt...' % (name))
 fo = open('%s_prikey.txt' % (name), 'w')
 fo.write('%s,%s,%s' % (keySize, privateKey[0], privateKey[1]))
 fo.close()



# rsaCipher module
import sys

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256

def rsaCipher():
 filename = 'encrypted_file.txt'
 mode = 'decrypt'

 if mode == 'encrypt':
  message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
  pubKeyFilename = 'fpt_pubkey.txt'
  print('encrypting and writing to %s...' % (filename))
  encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)
  print('Encrypted text:')
  print(encryptedText)

 elif mode == 'decrypt':
  priKeyFilename = 'fpt_prikey.txt'
  print('Reading from %s and decrypting...' % (filename))
  decryptedText = readFromFileAndDecrypt(filename, priKeyFilename)
  print('Decrypted text:')
  print(decryptedText)


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
 messageBytes = message.encode('ascii')

 blockInts = []
 for blockStart in range(0, len(messageBytes), blockSize):
  blockInt = 0
  for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
   blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
  blockInts.append(blockInt)
 return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
 message = []
 for blockInt in blockInts:
  blockMessage = []
# debug
#  print('\ngetTextFromBlocks: for blockInt in blockInts: message: %s\n' % message)
# debug
#  print('\ngetTextFromBlocks: for blockInt in blockInts: blockMessage: %s\n' % blockMessage)  
  for i in range(blockSize - 1, -1, -1):
# debug
#   print('\ngetTextFromBlocks: for blockInt in blockInts: message: %s\n' % message)
# debug
#   print('\ngetTextFromBlocks: for blockInt in blockInts: blockMessage: %s\n' % blockMessage)  
   if len(message) + i < messageLength:
    asciiNumber = blockInt // (BYTE_SIZE ** i)
    blockInt = blockInt % (BYTE_SIZE ** i)
    blockMessage.insert(0, chr(asciiNumber))
  message.extend(blockMessage)
 return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
 encryptedBlocks = []
 n, e = key

 for block in getBlocksFromText(message, blockSize):
  encryptedBlocks.append(pow(block, e, n))
 return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
 decryptedBlocks = []
 n, d = key
 for block in encryptedBlocks:
# debug
#  print('\ndecryptMessage: decryptedBlocks: %s\n' % decryptedBlocks)
  decryptedBlocks.append(pow(block, d, n))
 return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
 fo = open(keyFilename)
 content = fo.read()
 fo.close()
 keySize, n, EorD = content.split(',')
# debug
# print('\nreadKeyFile: keySize: %s, n: %s, EorD: %s\n' % ((int(keySize)), int(n), int(EorD)))
 return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
 keySize, n, e = readKeyFile(keyFilename)

 if keySize < blockSize * 8:
  print('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))
  return None

 encryptedBlocks = encryptMessage(message, (n, e), blockSize)

 for i in range(len(encryptedBlocks)):
  encryptedBlocks[i] = str(encryptedBlocks[i])
 encryptedContent = ','.join(encryptedBlocks)

 encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
 fo = open(messageFilename, 'w')
 fo.write(encryptedContent)
 fo.close()
 return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
 keySize, n, d = readKeyFile(keyFilename)

 fo = open(messageFilename)
 content = fo.read()
 messageLength, blockSize, encryptedMessage = content.split('_')
 messageLength = int(messageLength)
 blockSize = int(blockSize)

 if keySize < blockSize * 8:
  print('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))
  return None

 encryptedBlocks = []
 for block in encryptedMessage.split(','):
# debug
#  print('\nreadFromFileAndDecrypt: encryptedBlocks: %s\n' % encryptedBlocks)
  encryptedBlocks.append(int(block))

 return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)




# >>> I'm getting a weird result when I decrypt the example text, so I'll take a look at Al's diff tool on the book's website, http://inventwithpython.com/hacking/diff/index.html?p=rsaCipher#diff
# Decrypted text:
#  e he The "The  "The d "The nd "The and "The land "The tland "The stland "The estland "The iestland "The riestland "The Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The  Priestland "The 


# ...and I'll try executing Al's code: http://inventwithpython.com/rsaCipher.py

# RSA Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys

# IMPORTANT: The block size MUST be less than or equal to the key size!
# (Note: The block size is in bytes, the key size is in bits. There
# are 8 bits in 1 byte.)
DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def rsaCipher():
    # Runs a test that encrypts a message to a file or decrypts a message
    # from a file.
    filename = 'encrypted_file.txt' # the file to write to/read from
    mode = 'decrypt' # set to 'encrypt' or 'decrypt'

    if mode == 'encrypt':
        message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        pubKeyFilename = 'al_sweigart_pubkey.txt'
        print('Encrypting and writing to %s...' % (filename))
        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

        print('Encrypted text:')
        print(encryptedText)

    elif mode == 'decrypt':
        privKeyFilename = 'al_sweigart_privkey.txt'
        print('Reading from %s and decrypting...' % (filename))
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

        print('Decrypted text:')
        print(decryptedText)


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a string message to a list of block integers. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.

    messageBytes = message.encode('ascii') # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        # Calculate the block integer for this block of text
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts the message string into a list of block integers, and then
    # encrypts each block integer. Pass the PUBLIC key to encrypt.
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        # ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Decrypts a list of encrypted block ints into the original message
    # string. The original message length is required to properly decrypt
    # the last block. Be sure to pass the PRIVATE key to decrypt.
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    # Given the filename of a file that contains a public or private key,
    # return the key as a (n,e) or (n,d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    # Using a key from a key file, encrypt the message and save it to a
    # file. Returns the encrypted message string.
    keySize, n, e = readKeyFile(keyFilename)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


    # Encrypt the message
    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    # Convert the large int values to one string value.
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    # Write out the encrypted string to the output file.
    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    # Also return the encrypted string.
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    # Using a key from a key file, read an encrypted message from a file
    # and then decrypt it. Returns the decrypted message string.
    keySize, n, d = readKeyFile(keyFilename)


    # Read in the message length and the encrypted message from the file.
    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    # Convert the encrypted message into large int values.
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    # Decrypt the large int values.
    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


# If rsaCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()



# Al's version of the rsaCipher module does work. Compare the encrypted texts, since I used the same keys for both encryption operations. Diff says there's no difference between the two encrypted texts. Time to try some debug print statements around the decryption loops. This indicated a problem with my getTextFromBlocks subroutine. Running Al's version resulted in correctly decrypted text. Diff those two. The fault was that the message.extend(blockMessage) clause was indented by one too many whitespaces, causing getTextFromBlocks to extend the message by the same block over and over again. Indentation level is really hard to see when indentation is only a single space. That was certainly handy for creating bugs for me to hunt to get some extra experience. Now that I'm done with that, find how to reconfigure Emacs' python mode to use four spaces per tab. (;
# https://www.emacswiki.org/emacs/IndentingPython












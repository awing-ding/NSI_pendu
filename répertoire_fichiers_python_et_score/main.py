from random import randrange #to get a random word
from os import system # Used to clear the screen
from platform import system as platform # Used to know the OS to be able to clear the screen
import datetime #to get the date and time for the score file

# ----------------------------
# Global variables & constants
# ----------------------------
if platform() == 'Windows':
    COMMAND = 'cls'
elif platform() == 'Linux' or platform() == 'Darwin':
    COMMAND = 'clear'

SCORE_PATH = 'score.txt' # Path to the score file
WORD_PATH = '../répertoire_fichiers_texte_dictée/liste_mots.txt' # Path to the word list
                                                                 # words are separated by a new line
VSCODE_PATH = './répertoire_fichiers_texte_dictée/liste_mots.txt' #should only be used in dev mode with vsc

                #hangman scheme
                # ________
                # |/    |
                # |     O
                # |    /|\
                # |    / \
                # |_______

# It's a list that contains the drawing of the hangman.
ERROR_DRAWING = [
    [],
    [[' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','_','_','_','_','_','_','_'],
        ],
    [[' ',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [[' ',' ',' ',' ',' ',' ',' ',' '],
        ['|','/',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],   
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
        ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ',' ','|','\\'],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ','/','|','\\'],
        ['|',' ',' ',' ',' ',' ',' ',' '],
        ['|','_','_','_','_','_','_','_'],    
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ','/','|','\\'],
        ['|',' ',' ',' ',' ','/',' ',' '],
        ['|','_','_','_','_','_','_','_'],
    ],
    [['_','_','_','_','_','_','_','_'],
        ['|','/',' ',' ',' ',' ','|',' '],
        ['|',' ',' ',' ',' ',' ','O',' '],
        ['|',' ',' ',' ',' ','/','|','\\'],
        ['|',' ',' ',' ',' ','/',' ','\\'],
        ['|','_','_','_','_','_','_','_'],
    ],    
]

def ErrorPrinter(errorNumber):
    """
    It takes an integer between 0 and 11, and prints out the corresponding error drawing
    
    :param errorNumber: The drawing corresponding to the number of error to be printed
    :return type: str The drawing corresponding to the number of error to be printed
    """

    worklist = []
    if errorNumber < 0 or errorNumber > 11:
        raise ValueError()
    else:
        for line in ERROR_DRAWING[errorNumber]:
            worklist.append(''.join(line))
        return '\n'.join(worklist)

def FileOpenner(path):
    """
    It opens a file, reads it, splits it into a list of words, and returns the number of words and the
    list of words.
    
    :param path: The path to the file you want to open
    :return: type: tuple The number of words in the file and the list of words in the file into a tuple.
    """
    with open(path, 'r') as file:
        stredFile = file.read()
        wordList = stredFile.split('\n')
    return wordList


def WordSelector(numberOfWord, wordList):
    """
    Function that randomly choose a word from the wordList parameter of the length numberOfWord
    
    :param numberOfWord: the number of words in the wordList
    :param wordList: a list of words
    :return: a random word from the wordList parameter of the length numberOfWord.
    """
    word = wordList[randrange(0,numberOfWord)]
    wordList.remove(word)
    return (word, wordList)

def WordHidder(word):
    """
    > This function takes a word as input and returns a string of the same length with all characters
    replaced by underscores
    
    :param word: the word to be hidden
    :return: A string of '_' characters the same length as the word.
    """
    hiddenWord = ""
    for i in range(len(word)):
        hiddenWord += '_'
    return hiddenWord

def init(wordList):
    """
    It initializes all the variables for a game
    
    :param wordList: The list of words that the game will use
    :return: A dictionary with the word, the hidden word and the number of error done (here 0 bc it's
    the beginning of the game)
    """
    numberOfWord = len(wordList) 
    word, wordList = WordSelector(numberOfWord, wordList)
    hiddenWord = WordHidder(word)
    return {
        'wordList' : wordList,
        'word' : word,
        'workWord' : hiddenWord,
        'errorNumber' : 0
    }

def lackingLetterCounter(usedWord):
    """
    It counts how many letters we have to find
    
    :param usedWord: the word that we're using to play the game
    :return: The number of letters that are missing from the word.
    """
    count = 0
    for char in usedWord:
        if char == '_':
            count += 1
    return count

def printer(usedChar, errorNumber, usedWord, lackingLetter):
    """
    It prints the current state of the game
    
    :param usedChar: list of letters already used
    :param errorNumber: the number of errors the player has made
    :param usedWord: the word that is being guessed
    :param lackingLetter: the number of letters that are still missing in the word

    :return: type : str the current state of the game
    """
    return (ErrorPrinter(errorNumber) + "\nLettres qui ont déjà été dites : " + ' '.join(usedChar) + '\nmot actuel :' + usedWord + '\nnombre de lettre à trouver : ' + str(lackingLetter))

def discoverLetter(letter, word, usedWord):
    """
    It checks if the letter is in the word, and if it is, it replaces the corresponding underscores with the letter
    
    :param letter: type : str ; len = 1 the letter to be checked
    :param word: type : str the word to be checked
    :param usedWord: type : str the word that is being guessed
    :return: type : str the word that is being guessed with the letter added if it was in the word
    """
    for i in range(len(word)):
        if word[i].upper() == letter:
            usedWord = usedWord[:i] + letter + usedWord[i+1:]
    return usedWord

def game(wordList):
    """
    It prints the game's status, asks the user for a letter, checks if the letter is in the word, and if
    it is, it replaces the corresponding underscores with the letter
    
    :param wordList: the list of words that the game will choose from
    :return: a tuple containing the point gained by the player and the word list
    """
    usedChar = []
    var = init(wordList)
    lackingLetter = lackingLetterCounter(var['workWord'])

    while True:

        system(COMMAND)
        print(printer(usedChar, var['errorNumber'], var['workWord'], lackingLetter))
        letter = input("Quelle lettre pensez vous être dans le mot ?\n").upper()
        usedChar.append(letter)

        if not letter in var['word'].upper(): #checks if the letter is in the word
            var['errorNumber'] += 1 #if not, it adds one to the error counter
            if var['errorNumber'] >= 11: #if the error counter is 11 or more, the player loses
                print(ErrorPrinter(var['errorNumber']))
                print("vous avez perdu cette partie !\n le mot était: ", var['word'])
                return (0, var['wordList'])
            
        elif len(letter) == 1: #prevents the user from entering more than one letter
            var['workWord'] = discoverLetter(letter, var['word'], var['workWord'])
            lackingLetter = lackingLetterCounter(var['workWord'])
            if lackingLetter <= 0: #if the player has found all the letters, he wins
                print("vous avez gagné cette partie, le mot été bien: ", var['word'])
                return (1, var['wordList'])

def main():
    """
    The function main() is a while loop that calls the function game() and adds the returned value to
    the variable score
    """
    escape = False
    score = 0
    wordList = FileOpenner(WORD_PATH)
    #wordList = FileOpenner(VSCODE_PATH) #uncomment to go in debug mode
    while not escape :
        addscore, wordList  = game(wordList)
        score += addscore
        if len(wordList) ==  0:
            escape = True
        input("appuyez sur entrer pour continuer")
    system(COMMAND)
    print(f"l'exercice est fini, votre score est de: {score}")
    with open(SCORE_PATH, 'a') as file:
        file.write(f"\n{datetime.datetime.today()},{str(score)}" ) #writes the score in the score file with the date
        

main()
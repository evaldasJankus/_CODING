import random


#-------------------------BEYOND THE TASK--------------------------------------
"""
 Not only should you choose a random number, but you should also choose a
random number base, from 2 to 16, in which the user should submit their
input. If the user inputs “10” as their guess, you’ll need to interpret it in the
correct number base; “10” might mean 10 (decimal), or 2 (binary), or 16
(hexadecimal).
"""
def dec_to_base(num,base):  #Maximum base - 36
    if num == 0: return '0'
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)  #Using uppercase letters
        num //= base
    base_num = base_num[::-1]  #To reverse the string
    return base_num

"""
 Modify this program, such that it gives the user only three chances to guess the
correct number. If they try three times without success, the program tells them
that they didn’t guess in time and then exits.
"""
def guessing_number():
    # number = random.randint(0,16)
    bases = [x for x in range(2,17)]
    base_choice = random.choice(bases)

    number = random.randint(0,5)
    choice, counter = 1, 0

    while choice and not(choice == 'q'):
        if counter == 3:
            choice = input('You failed to guess in 3 times. You want to try again(y) or quit(q)?')
            counter = 0
            base_choice = random.choice(bases)
            continue
        choice = input(f'Guess number [0:16] in base {base_choice}({[dec_to_base(x, base_choice) for x in range(6)]}): ')
        if not choice.isalnum() or choice == 'q': continue
        counter += 1
        print(f'[GUESS {counter} OUT OF 3]')
        if int(choice, base=base_choice) > number: print('Too high')
        elif int(choice, base=base_choice) < number: print('Too low')
        else:
            print('Just right')
            choice = input('SUCCESS! You want to PLAY again(y) or quit(q)?')
            base_choice = random.choice(bases)
            counter = 0
    else:
        print(f'{"GAME END":-^25}')

"""
 Try the same thing, but have the program choose a random word from the dictionary,
and then ask the user to guess the word. (You might want to limit yourself to words
containing two to five letters, to avoid making it too horribly
difficult.) Instead of telling the user that they should guess a smaller or larger
number, have them choose an earlier or later word in the dict.
"""
def guessing_word():
    words = 'How are we going to add words to the vocabulary'.split()
    word = random.choice(words)

    choice, counter = 1, 0
    wrong_guesses = []

    while not choice == 'q':
        if counter == 3:
            choice = input('You failed to guess in 3 times. You want to try again(y) or quit(q)?')
            counter = 0
            word = random.choice(words)
            wrong_guesses = []
            continue
        choice = input(f'GUESS WORD FROM LIST[{words}]: ')
        if not (choice in words) or  choice == 'q' or (choice in wrong_guesses): continue
        counter += 1
        print(f'[GUESS {counter} OUT OF 3]')
        if choice == word:
            print('Just right')
            choice = input('SUCCESS! You want to PLAY again(y) or quit(q)?')
            word = random.choice(words)
            counter = 0
            wrong_guesses = []
        else:
            print('Correct word is:','longer' if len(choice) <len(word) else 'shorter' if len(choice) >len(word) else 'same length')
            wrong_guesses.append(choice)
    else:
        print(f'{"GAME END":-^25}')

if __name__=='__main__':
    # guessing_number()
    # print(dec_to_base(12, 8))
    guessing_word()

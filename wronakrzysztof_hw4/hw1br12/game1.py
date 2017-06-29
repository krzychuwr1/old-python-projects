ROADPICS = ('''

    0                                                    /\_______/\ 
    |                                                   |           |
   /|\                                                  |    AGH    |
__ / \__________________________________________________|___________|''', '''

         0                                               /\_______/\ 
         |                                              |           |
        /|\                                             |    AGH    |
_______ / \_____________________________________________|___________|''', '''

              0                                          /\_______/\ 
              |                                         |           |
             /|\                                        |    AGH    |
____________ / \________________________________________|___________|''', '''

                   0                                     /\_______/\ 
                   |                                    |           |
                  /|\                                   |    AGH    |
_________________ / \___________________________________|___________|''', '''

                        0                                /\_______/\ 
                        |                               |           |
                       /|\                              |    AGH    |
______________________ / \______________________________|___________|''', '''

                             0                           /\_______/\ 
                             |                          |           |
                            /|\                         |    AGH    |
___________________________ / \_________________________|___________|''', '''

                                  0                      /\_______/\ 
                                  |                     |           |
                                 /|\                    |    AGH    |
________________________________ / \____________________|___________|''', '''

                                       0                 /\_______/\ 
                                       |                |           |
                                      /|\               |    AGH    |
_____________________________________ / \_______________|___________|''', '''

                                            0            /\_______/\ 
                                            |           |           |
                                           /|\          |    AGH    |
__________________________________________ / \__________|___________|''', '''

                                                 0       /\_______/\ 
                                                 |      |           |
                                                /|\     |    AGH    |
_______________________________________________ / \_____|___________|''')

QUES = (
    'In which city is AGH located?', 'When was AGH established?', 'Who owns actually a position of University Rector?',
    'Whose name bears the University?', 'What colours includes AGH logo?', 'What is type of funding?',
    'What monument is placed in AGH area?', 'How many faculties work on AGH?', 'Who is AGH patron?',
    'How many different fields of study you can take on AGH?')
ANSA = (
    'Krakow', '1919', 'prof. Slomka', 'Stanislaw Staszic', 'green-black-red', 'public', 'locomotive', '16',
    'saint Barbara',
    '57')
ANSB = (
    'Warsaw', '1929', 'dr. Grzanka', 'Tadeusz Kosciuszko', 'white-green-black', 'private', 'tank', '12', 'santa Claus',
    '50')
ANSC = (
    'Wroclaw', '1909', 'dr. Gajecki', 'Adam Malysz', 'pink-yellow-orange', 'public-private', 'plane', '10',
    'saint tropez',
    '90')
ANSD = ('Zakopane', '1911', 'prof. Kakol', 'Robert Lewandowski', 'black-eyed-peas', 'private-public', 'ship', '20',
        'saint Christopher', '42')
CORRECT_ANS = ('a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a')


def displayBoard(ROADPICS, QUES, ANSA, ANSB, ANSC, ANSD, questNum, lifes):
    """
    This function displays the questions and ascii picture of tom
    :param ROADPICS: tuple
    :param QUES: tuple
    :param ANSA: tuple
    :param ANSB: tuple
    :param ANSC: tuple
    :param ANSD: tuple
    :param questNum: int
    :param lifes: int
    :return:
	"""

    print(ROADPICS[questNum])
    print()
    print()
    print('Lifes remaining: ' + '*' * lifes)
    print('Stage ' + str(questNum + 1) + ': ' + QUES[questNum])
    print(
        'A: ' + ANSA[questNum] + '   ' + 'B: ' + ANSB[questNum] + '   ' + 'C: ' + ANSC[questNum] + '   ' + 'D: ' + ANSD[
            questNum])


def getAnswer():
    """
	This function does the exact same thing as input() function
	:return:
	"""
    answer = input()
    return answer


def winFinalInfo():
    """
	This function prints the message after the game has been won
	:return:
	"""
    print('Congratulations ' + name + '! You did it! Now Tom has enough knowledge to study on AGH!!!')
    final = '''
	
		  /\\            /\\
		 /  \\__________/  \\
		|                  |
		|        AGH       |
		|                  |
		|   0   Thanks,    |
		|   |   my Friend! |
		|  /|\\             |
		|  / \\             |
		|__________________|
	
	'''
    print(final)


def defeatFinalInfo():
    """

	:return:
	"""
    print()
    print('Oh no!!!')
    print('You lost! Tom will NOT study on AGH!')
    print('Try again!')


name = ''
questNum = 0
lifes = 3

introduction = '''----------------------   HELLO !!!   ------------------------

This is Tom:
     0
     |
    /|\\
    / \\
His biggest dream is to join AGH University.
To make this dreams come true, he has to pass through 10 stages and answer 10 questions.
Help Tom join AGH!!!!
You have 3 lifes, so you can make 3 mistakes until failure. Be careful!
Good luck!

If ready, give me your name and enter. '''

print(introduction)
name = input()
print('Ok ' + name + ', lets go!')
while True:
    displayBoard(ROADPICS, QUES, ANSA, ANSB, ANSC, ANSD, questNum, lifes)
    answer = getAnswer()
    if answer == CORRECT_ANS[questNum]:
        if questNum == 9:
            winFinalInfo()
            break
        else:
            print('\n\nYes! Thats right! Tom is one step closer to AGH! Go on!')
            questNum += 1
    else:
        lifes = lifes - 1
        if lifes == -1:
            defeatFinalInfo()
            break
        print('\n\nNo! Try again!!!')
        print('You lost 1 life, ' + str(lifes) + ' remain!!')

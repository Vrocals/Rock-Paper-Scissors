import random,time,os

while True:

 choices = ['rock','paper','scissors']

 computer = random.choice(choices)

 player = '' or None

 while player not in choices:
    player = str(input('Rock, Paper or Scissors: '))

 print(f'Player: {player}')
 print(f'Computer: {computer}')


 if player == computer:
    print('Tie')

 if player == 'rock':
    if computer == 'paper':
     print('You Losed')

 if player == 'paper':
    if computer == 'rock':
        print('You Won')

 if player == 'rock':
    if computer == 'scissors':
        print('You Won')

 if player == 'scissors':
    if computer == 'rock':
        print('You Losed')

 if player == 'paper':
    if computer == 'scissors':
        print('You Losed')

 if player == 'scissors':
    if computer == 'paper':
        print('You Won')

 playAgain = str(input('Would you like to play again(y/n): ')).lower()

 if playAgain != 'y':
    break
time.sleep(1)
os.system('clear')
print('GOODBYE')
time.sleep(1)
os.system('clear')

#from os import system
from random import randint
from fxn import *
from time import sleep

#IPython.display library is used to implement clear_output fxn to clear screen on Jupyter file
#from IPython.display import clear_output

system('clear')
print('Welcome to Tic Tak Toe Game')

#Decide 'X' and 'O' for players
p1_symbol, p2_symbol = players_symbol()
    
print(f'''
Player 1 is {p1_symbol}
Player 2 is {p2_symbol}

Player 1 will go first...
''')


sleep(2)

l='1 2 3 4 5 6 7 8 9'.split()            # Array to store elements of the tic tac toe
print_board(l)                           #Print The Board

play_again = True
while play_again:
    # Ask if player is ready to play
    readiness = input('Ready to play (Y/N) ? ')
    if(readiness.upper()=='N'):
        input('Press Enter when you are ready !')
    print_board(l)
    readiness='Y'
   
    while readiness.upper()=='Y':
        l=player_choice('P1', p1_symbol, l)  #To Enter Player 1's choice on board and return the updated list 
        print_board(l)                       #To print the updated board
        if(check(l,p1_symbol)):                    #To check if player 1 has won
            print('Player 1 Won!')
            break
        
        if(l.count('X')+l.count('O')==9):    #To check if there's a TIE
            print('Game Tie')
            break
        
        l=player_choice('P2', p2_symbol, l)  #To Enter Player 2's choice on board and return the updated list
        print_board(l)    
        if(check(l,p2_symbol)):              #To check if player 2 has won
            print('Player 2 Won!')
            break
    
    play_again = input('Want to play Again(Y/N)? ')
    if play_again == 'y' or play_again=='Y':
        play_again=True
        l='1 2 3 4 5 6 7 8 9'.split()            # Array to store elements of the tic tac toe
        print_board(l)
    else:
        play_again=False

#**************************** END **************************#

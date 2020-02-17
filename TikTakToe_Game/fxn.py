from os import system           #To clear screen

def player_choice(player, symbol, l):
    choice = int(input(f'{player}, enter your position on board (1-9): '))
    l[choice-1]=symbol
    return l

def print_board(l):
    #clear_output()
    system('clear')
    print(
    '''
       |   |   
     {} | {} | {}
       |   |   
    -----------
       |   |   
     {} | {} | {}
       |   |   
    -----------
       |   |   
     {} | {} | {}
       |   |   
    '''.format(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
    )

def check(l, ch):
    z=lambda x:[x]*3                         # To return a 3 element array i.e. ['O','O',O] OR ['X','X','X']
    return ((l[0:3]==z(ch)) or (l[3:6]==z(ch)) or (l[6:9]==z(ch)) or    #All Horizontals
       (l[::3]==z(ch)) or (l[1::3]==z(ch)) or (l[2::3]==z(ch)) or  #All Verticals
       (l[::4]==z(ch)) or (l[2:8:2]==z(ch)))   # Diagonal 1 and 2

def players_symbol():
    p1_symbol = input("For Player-1 enter your symbol ('X' or 'O':): ").upper()
    if (p1_symbol=='X'): 
        return('X','O')
    
    return('O','X')


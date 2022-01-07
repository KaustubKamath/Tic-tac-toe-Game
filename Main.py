import random

player_one,player_two='',''

#Game Functions
def goFirst():
    if random.randint(0,1)==1:
        return 'Player 1'
    else:
        return 'Player 2'

def displayBoard(board):
    print('  |   |   ')
    print(board[7] +' | ' + board[8] + ' | ' + board[9])
    print('  |   |   ')
    print('----------')
    print('  |   |   ')
    print(board[4] +' | ' + board[5] + ' | ' + board[6])
    print('  |   |   ')
    print('----------')
    print('  |   |   ')
    print(board[1] +' | ' + board[2] + ' | ' + board[3])
    print('  |   |   ')

def chooseMarker():
    marker=''
    while not(marker=='X' or marker=='O'):
        marker=input('Please choose a marker "X" or "O": ').upper()
    if marker=='X':
        return ('X','O')
    else:
        return('O','X')

def checkSpace(board,position):
    return board[position]==' '

def nextPosition(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not checkSpace(board,position):
        position=int(input('Please choose a position between 1-9 to place your marker: '))
    return position
    
def placeMarker(board,marker,position):
    if board[position]!='X' or board[position]!='O':
        board[position]=marker
        displayBoard(board)

def boardFull(board):
    for i in range(1,10):
        if not checkSpace(board,i):
            return False
    return True

def checkWin(board,marker):
    return((board[7]==board[8]==board[9]==marker)or
    (board[4]==board[5]==board[6]==marker)or
    (board[1]==board[2]==board[3]==marker)or
    (board[1]==board[4]==board[7]==marker)or
    (board[2]==board[5]==board[8]==marker)or
    (board[9]==board[6]==board[3]==marker)or
    (board[1]==board[5]==board[9]==marker)or
    (board[7]==board[5]==board[3]==marker))

def playAgain():
    return input('Do you want to play again? Type "YES" or "NO". ').upper().startswith('Y')

print('Welcome to the TIC TAC TOE game!')

while True:
    #Reset the board
    the_board=[' ']*10
    turn=goFirst()
    player_one,player_two=chooseMarker()
    print(f'{turn} will go first!')
    play_game=input('Are you ready to begin? Type "YES" or "NO". ')
    if play_game.upper()[0]=='Y':
        play_on=True
    else:
        play_on=False
    
    while play_on:
        if turn=='Player 1':
            print('\n'*5) #Printing empty lines
            print('The board currently looks like this!')
            displayBoard(the_board)
            position=nextPosition(the_board)
            placeMarker(the_board,player_one,position)

            if checkWin(the_board,player_one):
                displayBoard(the_board)
                print('Congratulations Player 1! You have won!')
                play_on=False
            else:
                if boardFull(the_board):
                    displayBoard(the_board)
                    print('Game has been drawn!')
                    break
                else:
                    turn='Player 2'

        if turn=='Player 2':
            print('\n'*5) #Printing empty lines
            print('The board currently looks like this!')
            displayBoard(the_board)
            position=nextPosition(the_board)
            placeMarker(the_board,player_two,position)

            if checkWin(the_board,player_two):
                displayBoard(the_board)
                print('Congratulations Player 2! You have won!')
                play_on=False
            else:
                if boardFull(the_board):
                    displayBoard(the_board)
                    print('Game has been drawn!')
                    break
                else:
                    turn='Player 1'

    if not playAgain():
        print('Thank you for playing!')
        break
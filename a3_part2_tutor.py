import random

def create_board(size):
    '''int->list (of str)
       Precondition: size is even positive integer between 2 and 52    
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    random.shuffle(board)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def wait_for_player():
    '''(None)->None
    Pauses the program until the user presses enter
    '''
    try:
        input("Press enter to continue ")
    except SyntaxError:
        pass

def hidden_board(board,discovered):
    for i in range(len(board)):
        if discovered[i]==True:
            print('{0:4}'.format(board[i]), end=' ')
        else:
            print('*   ', end=' ')
    print()
    for i in range(len(board)):
        print('{0:4}'.format(str(i+1)), end=' ')
    print()
    
def play_game(board):
    '''(list of str)->None'''
    
    # The following line of code creates a list indicating what locations are paired, i.e., discovered
    # At the begining none are, so default initializaiton to False is ok
    # You may find this useful
    count=0
    discovered=[False]*len(board)
    size = len(board)
    # Loop until all characters are revealed
    while discovered!=[True]*len(board):
        hidden_board(board,discovered)
        guess1=int(input('Enter two distinct locationson the board that you want to revealed.\ni.e two integers in the range [1, {}]\n'.format(size)))
        guess2=int(input(''))
        # validate the user input
        # if not valid, prompt for retry
        if guess1 == guess2:
            continue
        if guess1 > size:
            continue
        if guess2 > size:
            continue	
        if discovered[guess1-1]:
            continue
        if discovered[guess2-1]:
            continue
	# assume user get the pair right so
	# the character at the location can be displayed
        discovered[guess1-1]=True
        discovered[guess2-1]=True
        hidden_board(board,discovered)
        wait_for_player()
        # if the two locations are not same, revert the flags back to original
        if board[guess1-1]!=board[guess2-1]:
            discovered[guess1-1]=False
            discovered[guess2-1]=False
        print('\n'*40)
        count=count+1
    print('Congratulations, you finished in {} guesses. \nThat is {} more than the best possible'.format(count, count-len(board)/2))


# MAIN
i=0
while i==0:
    rawInput=input('How many cards do you want to play with?\nEnter an even number between 2 and 52:\n')
    try:
        val=int(rawInput)
    except ValueError:
        print(' ')
        continue
    val=int(rawInput)
    if val>=2 and val<=52:
        valEven=val%2
        if valEven!=1:
            i=1
            size=val

    
# this creates the board for you of the given size
board=create_board(size)

# this calls your play_game function that plays the game
play_game(board)




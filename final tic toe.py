board=['-','-','-',
       '-','-','-',
       '-','-','-']

def display_board():
    print(board[0]+'  |  '+board[1]+'  |  '+board[2])
    print(board[3]+'  |  '+board[4]+'  |  '+board[5])
    print(board[6]+'  |  '+board[7]+'  |  '+board[8])
    
display_board()




def player1_turn():
    player1=int(input("ENTER THE POSITION OF 'X' : "))
    player1=player1-1
    board[player1]='x'
    print(display_board())


def player2_turn():
    player2=int(input("ENTER THE POSITION OF 'o' : "))
    player2=player2-1
    board[player2]='o'
    print(display_board())
    check_rows()
    check_diagonals()
    check_columns()



def check_rows():
    row1=board[0]==board[1]==board[2]!='-'
    if row1=='x':
        print('player 1 win')
    elif row1=='o':
        print('player 2 win')
    elif row1=='-':
        print('continue')
    

    row2=board[3]==board[4]==board[5]!='-'
    if row2=='x':
        print('player 1 win')
    elif row2=='o':
        print('player 2 win')
    elif row2=='-':
        print('continue')

    row3=board[6]==board[7]==board[8]!='-'
    if row3=='x':
        print('player 1 win')
    elif row3=='o':
        print('player 2 win')
    elif row3=='-':
        print('continue')


def check_columns():
    col1=board[0]==board[3]==board[6]!='-'
    if col1=='x':
        print('player 1 win')
    elif col1=='o':
        print('player 2 win')
    elif col1=='-':
        print('continue')
    

    col2=board[1]==board[4]==board[7]!='-'
    if col2=='x':
        print('player 1 win')
    elif col2=='o':
        print('player 2 win')
    elif col2=='-':
        print('continue')

    col3=board[2]==board[5]==board[8]!='-'
    if col3=='x':
        print('player 1 win')
    elif col3=='o':
        print('player 2 win')
    elif col3=='-':
        print('continue')


def check_diagonals():
    diag1=board[0]==board[4]==board[8]!='-'
    if diag1=='x':
        print('player 1 win')
    elif diag1=='o':
        print('player 2 win')
    elif diag1=='-':
        print('continue')

    diag2=board[6]==board[4]==board[2]!='-'
    if diag2=='x':
        print('player 1 win')
    elif diag2=='o':
        print('player 2 win')
    elif diag2=='-':
        print('continue')




n=False


while n==False:

    player1_turn()
    player2_turn()





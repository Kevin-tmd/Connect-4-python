board=[[' ']*7,
       [' ']*7,
       [' ']*7,
       [' ']*7,
       [' ']*7,
       [' ']*7]
fin=False
valid=True
r=0

def display():
    global board
    row=' '
    for i in range(6):
        row='ㅣ'+board[i][0]
        for j in range(6):
            row=row+'ㅣ'+board[i][j+1]
        row=row+'ㅣ'
        print(row)

def check_horizontal():
    global board
    global fin
    for i in range(6):
        for j in range(4):
            if board[i][j]!=' ':
                if board[i][j]==board[i][j+1] and board[i][j+1]==board[i][j+2] and board[i][j+2]==board[i][j+3]:
                    fin=True

def check_vertical():
    global board
    global fin
            
    for j in range(7):
        for i in range(3):
            if board[i][j]!=' ':
                if board[i][j]==board[i+1][j] and board[i+1][j]==board[i+2][j] and board[i+2][j]==board[i+3][j]:
                    fin=True
            
def check_diagnal_right():
    global board
    global fin
            
    for i in range(3):
        for j in range(4):
            if board[i][j]!=' ':
                if board[i][j]==board[i+1][j+1] and board[i+1][j+1]==board[i+2][j+2] and board[i+2][j+2]==board[i+3][j+3]:
                    fin=True

def check_diagnal_left():
    global board
    global fin
            
    for i in range(3):
        for j in range(4):
            if board[5-i][j]!=' ':
                if board[5-i][j]==board[4-i][j+1] and board[4-i][j+1]==board[3-i][j+2] and board[3-i][j+2]==board[2-i][j+3]:
                    fin=True        

def check_win():
    global board
    global fin
    check_horizontal()
    check_vertical()
    check_diagnal_right()
    check_diagnal_left()
    

def enter(x,lim):
    while True:
        try:
            x=int(input('type column(1~7):'))
            if x>=0 and x<=lim:
                x-=1
                break
            else:
                print('out of range')
        except ValueError:
            print('wrong format')
    return x

def put(x,n):
    global board
    global valid
    found=False
    i=0
    while not(found) and i<=5:
        if board[5-i][x]==' ':
            found=True
        else:
            i+=1
            
    if found:
        if n==1:
            board[5-i][x]='R'
        else:
            board[5-i][x]='Y'
        valid=True
    else:
        print('column already full')
        
while not(fin):

    display()
    check_win()
    if fin:
        print('player 2 win')
        break
    valid=False
    turn=1
    print('player 1 turn (Red)')
    while not(valid):
        put(enter(r,7),1)
    

    display()
    check_win()
    if fin:
        print('player 1 win')
        break
    valid=False
    turn=2
    print('player 2 turn (Yellow)')
    while not(valid):
        put(enter(r,7),2)
    
        





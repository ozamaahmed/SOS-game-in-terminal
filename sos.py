# hi imma make SOS game for two players

# modify this mfing code!!!! i forgot to add the checking conditions if the current letter is O in only did that for S so do that me


def SpaceLeft(board): 
    for i in board:
        for j in i:
            if j == "-":
                return True 
    return False

def display(board): 
    for i in board: 
        print(i)

def final(): 
    if player1[0]>player2[0]:
        print(f"Player 1 is the WINNER!!!")
    else:
        print(f"player 2 is the WINNER!!!")

def scores(): 
    print(f"player 1: {player1[0]}, player 2: {player2[0]}")
    
def checkS(x,y,turn):
    
    c = 0
     
    i,j = x,y
    # write 8 if conditions here
    
    # eliminating the corners
    top,bottom,right,left = True,True,True,True 
    if i in (0,1):
        top = False
        # dont check for top three conditions
    
    elif i in (len(board)-1,len(board)-2):
        bottom = False 
        # dont check for bottom three conditions 
    
    if j in (0,1):
        left = False 
        # dont check for left three conditions 

    elif j in (len(board)-1,len(board)-2):
        right = False
        # dont check for right three conditions 
    
    # now do the checking (checkings array in clock wise direction from top-left)
    checkings = [0 for i in range(8)] 
    if not top or not left:
        #eliminate the top left
        checkings[0] = -1
    
    if not top:
        checkings[1] = -1
    
    if not top or not right:
        checkings[2] = -1
    
    if not right:
        checkings[3] = -1
    
    if not bottom or not right:
        checkings[4] = -1

    if not bottom:
        checkings[5] = -1
    
    if not bottom or not left:
        checkings[6] = -1
    
    if not left:
        checkings[7] = -1
        
    # now its time for actual if conditions where 
    # top left checking
    if ((i,j),(i-1,j-1),(i-2,j-2)) not in marked and checkings[0]!=-1 and board[i][j] == "S" and board[i-1][j-1] == "O" and board[i-2][j-2] == "S":
        marked.add(((i,j),(i-1,j-1),(i-2,j-2)))
        marked.add(((i-2,j-2),(i-1,j-1),(i,j)))
        c+=1
    # top up
    if ((i,j),(i-1,j),(i-2,j)) not in marked and checkings[1]!=-1 and board[i][j] == "S" and board[i-1][j] == "O" and board[i-2][j] == "S":
        marked.add(((i,j),(i-1,j),(i-2,j)))
        marked.add(((i-2,j),(i-1,j),(i,j)))
        c+=1
    # top right
    if ((i,j),(i-1,j+1),(i-2,j+2)) not in marked and checkings[2]!=-1 and board[i][j] == "S" and board[i-1][j+1] == "O" and board[i-2][j+2] == "S": 
        marked.add(((i,j),(i-1,j+1),(i-2,j+2)))
        marked.add(((i-2,j+2),(i-1,j+1),(i,j)))
        c+=1
    # to right 
    if ((i,j),(i,j+1),(i,j+2)) not in marked and checkings[3]!=-1 and board[i][j] == "S" and board[i][j+1] == "O" and board[i][j+2] == "S":
        marked.add(((i,j),(i,j+1),(i,j+2)))
        marked.add(((i,j+2),(i,j+1),(i,j)))       
        c+=1
    # bottom right
    if ((i,j),(i+1,j+1),(i+2,j+2)) not in marked and checkings[4]!=-1 and board[i][j] == "S" and board[i+1][j+1] == "O" and board[i+2][j+2] == "S":
        marked.add(((i,j),(i+1,j+1),(i+2,j+2)))
        marked.add(((i+2,j+2),(i+1,j+1),(i,j)))
        c+=1
    # top down
    if ((i,j),(i+1,j),(i+2,j)) not in marked and checkings[5]!=-1 and board[i][j] == "S" and board[i+1][j] == "O" and board[i+2][j] == "S":
        marked.add(((i,j),(i+1,j),(i+2,j)))
        marked.add(((i+2,j),(i+1,j),(i,j)))
        c+=1
    # right to left
    if ((i,j),(i,j-1),(i,j-2)) not in marked and checkings[7]!=-1 and board[i][j] == "S" and board[i][j-1] == "O" and board[i][j-2] == "S":
        marked.add(((i,j),(i,j-1),(i,j-2)))
        marked.add(((i,j-2),(i,j-1),(i,j)))
        c+=1
    # bottom left
    if ((i,j),(i+1,j-1),(i+2,j-2)) not in marked and checkings[6]!=-1 and board[i][j] == "S" and board[i+1][j-1] == "O" and board[i+2][j-2] == "S":
        marked.add(((i,j),(i+1,j-1),(i+2,j-2)))
        marked.add(((i+2,j-2),(i+1,j-1),(i,j)))
        c+=1


    if turn == 1: 
        player1[0]+=c 
    else: 
        player2[0]+=c 

    if c>0:
        return 1
    else:
        return 0

def checkO(x,y,turn):
    c = 0
    i,j = x,y

    vertical,cross,horizontal = True,True,True 
    # if the O is in corners
    if x == 0 or x == len(board)-1:
        vertical = False
        cross = False
    if y == 0 or y == len(board)-1:
        horizontal = False 
        cross = False

    checkings = [0 for i in range(3)] 
    if not horizontal:
        checkings[0] = -1
    if not cross:
        checkings[1] = -1 
    if not vertical:
        checkings[2] = -1


    #checking corners now 
    # vertical check 
    if checkings[0]!=-1 and ((i,j-1),(i,j),(i,j+1)) not in marked and board[i][j-1] == "S" and board[i][j] == "O" and board[i][j+1] == "S":
        marked.add(((i,j-1),(i,j),(i,j+1))) 
        marked.add(((i,j+1),(i,j),(i,j-1))) 
        c+=1 
    # cross checks 
    #we need to do two cross checks 
    if checkings[1]!=-1 and (((i-1,j-1),(i,j),(i+1,j+1)) not in marked and board[i-1][j-1] == "S" and board[i][j] == "O" and board[i+1][j+1] == "S"):
        marked.add(((i,j),(i,j),(i,j))) 
        marked.add(((i,j),(i,j),(i,j))) 
        c+=1

    if checkings[1]!=-1 and (((i+1,j-1),(i,j),(i-1,j+1)) not in marked and board[i+1][j-1] == "S" and board[i][j] == "O" and board[i-1][j+1] == "S"):
        marked.add(((i+1,j-1),(i,j),(i-1,j+1))) 
        marked.add(((i-1,j+1),(i,j),(i+1,j-1))) 
        c+=1
    
    # top checks 
    if checkings[2]!=-1 and ((i-1,j),(i,j),(i+1,j)) not in marked and board[i-1][j] == "S" and board[i][j] == "O" and board[i+1][j] == "S":
        marked.add(((i-1,j),(i,j),(i+1,j))) 
        marked.add(((i+1,j),(i,j),(i-1,j))) 
        c+=1 
    
    
    if turn == 1: 
        player1[0]+=c 
    else: 
        player2[0]+=c 

    if c>0:
        return 1
    else:
        return 0



marked = set([])
player1 = [0]
player2 = [0]

size = int(input("Enter the number of rows and columns: "))
board = [["-" for i in range(size)] for j in range(size)]

print("Welcome to SOS game there are two players, p1 goes first and p2 goes next. select (X Y S/O) in this format to insert. enter E to exit") 

turn = 1
visited = set([])
while SpaceLeft(board):
    print(f"player {turn} turn: ")

    position = input("enter the X and Y: ")
    if position == "exit":
        display(board)
        scores()
        final()
        break
    else:
        row,col = map(int,position.split())
    

    so = input("S/O: ") 
    #if no so is there insert and check 
    if (row,col) in visited:
        print("element already there choose other place!")
        continue
    else:
        if so in "Ss":
            board[row][col] = "S"
            point = checkS(row,col,turn)
        elif so in "Oo":
            board[row][col] = "O"
            point = checkO(row,col,turn)
        elif so == "exit":
            display(board)
            scores()
            final()
            break
        else:
            print("you can only choose S or O! ")
            continue
        
        display(board)
        print(f"placed {so} at {row} {col}")
        scores()
        if point == 1:
            continue
    
    #changing of turns
    if turn == 1:
        turn = 2
    else:
        turn = 1 
    
print("thanks for the play we out!")




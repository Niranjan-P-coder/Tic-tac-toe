turn = True
game = True

# above grid represents coordinate system, top left is (0,0) bottom right is (2,2)
gameboard = [[" "," "," "],
             [" "," "," "], 
             [" "," "," "]]
def print_board():
    print(" " + gameboard[0][0] +  " | " + gameboard[0][1] + " | " + gameboard[0][2] + " ")
    print("-----------")
    print(" " + gameboard[1][0] +  " | " + gameboard[1][1] + " | " + gameboard[1][2] + " ")
    print("-----------")
    print(" " + gameboard[2][0] +  " | " + gameboard[2][1] + " | " + gameboard[2][2] + " ")
#check board for winners
def check_board():
    pass
#creates new board per turn
def new_turn():
    pass
def reset_game():
    pass
def take_input():
    global turn
    global gameboard
    global game
    user_input_row = input("Enter a value from 0 to 2 inclusive as : ")
    x = int(user_input_row.strip())
    #print(x)
    user_input_column = input("Enter a value from 0 to 2 inclusive: ")
    y = int(user_input_column.strip())
    #print(y)
    if turn: 
        gameboard[x][y] ="X"
    else:
        gameboard[x][y] = "O"
    turn = not turn
while True:
    take_input() 
    #check wins
    print_board()

#Maze Structure
maze = [
    ["#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".",".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", "#", "#", "#", ".", "#","#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "O", "#", ".", "#","#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", "#", ".", ".", ".", "#","#", "#", "#", "O", "#", ".", "#"],
    ["#", ".", "#", "#", "#", "#", "#","#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", ".", ".", "#","#", "#", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", "#", ".",".", "#", "#", ".", "#", ".", "#"],
    ["#", ".", "#", "#", "#", ".", ".",".", ".", "#", ".", "#", "O", "#"],
    ["#", ".", ".", ".", ".", ".", "O","#", ".", ".", "#", "#", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#","#", ".", ".", ".", ".", ".", "."],
    ["#", "#", "#", "#", "#", "#", "#","#", ".", "#", "#", "#", "#", "#"]
]

#Starting position
start_row = 1
start_col = 1
sr = 1
sc = 1

#Ending position
end_row = 10
end_col = 13

#Printing maze
def print_maze():
    for row in maze:
        print(" ".join(row))
print_maze()

#Solve
current_row = start_row
current_col = start_col
tries=3
while (current_row, current_col) != (end_row, end_col):
    move = input("Enter your move (up, down, left, right): ")
    if move == "u":
        current_row -= 1
    elif move == "d":
        current_row += 1
    elif move == "l":
        current_col -= 1
    elif move == "r":
        current_col += 1
    else:
        print("Invalid move. Try again.")
        continue
    if maze[current_row][current_col] == "#":
        print("You hit a wall. Try again.")
        if move== "u":
            current_row+=1
        elif move == "d":
            current_row -= 1
        elif move == "l":
            current_col += 1
        elif move == "r":
            current_col -= 1
        #current_row = start_row
        #current_col = start_col
        #print_maze()
    elif maze[current_row][current_col] == "O":
        print("You have been killed")
        tries-=1
        if tries==1:
            print(str(tries)+" life remaining")
        else:
            print(str(tries)+" lives remaining")
        if(tries==0):
            print("You lost!")
            break
        current_row = start_row
        current_col = start_col
        maze[sr][sc]="."
    else:
        maze[sr][sc] = "."
        sr = current_row
        sc = current_col
        maze[sr][sc] = "X"
    for row in maze:
        print(" ".join(row))
if(tries!=0):
    print("Congrats! You finally escaped the maze!")

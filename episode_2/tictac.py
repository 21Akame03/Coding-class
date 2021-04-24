X_wins = 0
O_wins = 0

def draw(grid) :
    print(f"      1       2       3")

    
    print(f"1     {grid[0][0]}  |    {grid[0][1]}   |  {grid[0][2]}")
    print(f"  ------------------------")
    print(f"2     {grid[1][0]}  |    {grid[1][1]}   |  {grid[1][2]}")
    print(f"  ------------------------")
    print(f"3     {grid[2][0]}  |    {grid[2][1]}   |  {grid[2][2]}")


def main() :
    rows, cols = 3, 3
    gridpositions = [[" " for i in range(cols)] for j in range(rows)]

    # gridpostions = [[" ", " ", " "], [" ", " ", " "]]
    winner = ""
    player_turn = "X"
    turn_count = 0

    # start of code to manage the game
    print("Welcome to the game of Tic Tac Toe")
    
    while winner == "" :
        input_check = False
        row = 0
        col = 0

        print (f"Player's turn : {player_turn} \n")
        #draw the grid
        draw(gridpositions)


        # validate input
        while input_check == False:
            col_num = input("\nEnter the index of the column: ")
            row_num = input("Enter the index of the row: ")
            
            row = int(row_num)
            col = int(col_num)

            if (row < 4 and row > 0 ) and (col < 4 and col > 0) :
                selected_box = gridpositions[row -1][col -1]

                if selected_box == " ":
                    input_check = True
                else :
                    print(f"\nThat spot is already taken by {selected_box}")
        

        # assigning to the chosen position
        gridpositions[row-1][col-1] = player_turn

        # check in the columns
        for i in range(3):
            if gridpositions[i][0] == gridpositions[i][1] and gridpositions[i][1] == gridpositions[i][2] and gridpositions[i][0] != " " :
                winner = gridpositions[i][0]

        # check in the rows
        for j in range(3):
            if gridpositions[0][j] == gridpositions[1][j] and gridpositions[1][j] == gridpositions[2][j] and gridpositions[0][j] != " " :
                winner = gridpositions[0][j]

        #check the diagonals down
        if gridpositions[0][0] == gridpositions[1][1] and gridpositions[1][1] == gridpositions[2][2] and gridpositions[0][0] != " ":
                winner = gridpositions[0][0]

        # check for diagonal up
        if gridpositions[0][2] == gridpositions[1][1] and gridpositions[1][1] == gridpositions[2][0] and gridpositions[0][2] != " ":
                winner = gridpositions[0][0]
        
        # turn increment
        turn_count += 1

        # change of player
        if player_turn == "X":
            player_turn = "O"
        else : 
            player_turn ="X"

        print("\n\n")
    

    draw(gridpositions)
    print(f"\nCongratulations, the Winner is {winner}!")


if __name__ == "__main__":
    main()
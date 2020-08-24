# Initialize the player
player = 1

# Initial number of objects in the state to play
while True:
    state = input("Enter the number of objects you want to play with : ")
    if state > 50:
        print("The number of objects must to less than 50.")
    else:
        break

print("The number of objects you are playing with are ", state)

# Get valid moves to start the game
while True:
    print("Player", player)
    while True:
        move = input("What is your move?")
        if move in [1,2,3] and move<state:
            break
        print("Illegal move!!!")

    # Update the state and print it
    state = state - move
    print("The number of objects remaining ", state)

    # Winner
    if state == 1:
        print("Player ", player, " wins!!!" )
        break

    # Switch Players
    if player == 1:
        player = 2
    else:
        player = 1

print("GAME OVER!!!")

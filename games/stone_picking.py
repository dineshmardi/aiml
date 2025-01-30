def minimax(stones, is_maximizing):
    if stones == 0:
        return -1 if is_maximizing else 1

    if is_maximizing:
        best_value = -float('inf')
        for move in range(1, 4):
            if stones >= move:
                value = minimax(stones - move, False)
                best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for move in range(1, 4):
            if stones >= move:
                value = minimax(stones - move, True)
                best_value = min(best_value, value)
        return best_value

def best_move(stones):
    best_value = -float('inf')
    best_move = 0
    for move in range(1, 4):
        if stones >= move:
            value = minimax(stones - move, False)
            if value > best_value:
                best_value = value
                best_move = move
    return best_move

def play_game():
    stones = int(input("Enter the initial number of stones (1-20): "))
    while stones < 1 or stones > 20:
        stones = int(input("Invalid input. Enter the initial number of stones (1-20): "))

    player_turn = True  
    
    while stones > 0:
        if player_turn:
            print(f"\nStones left: {stones}")
            move = int(input("Your turn! Pick 1, 2, or 3 stones: "))
            while move < 1 or move > 3 or move > stones:
                move = int(input("Invalid move. Pick 1, 2, or 3 stones: "))
        else:
            move = best_move(stones)
            print(f"\nStones left: {stones}")
            print(f"AI picks {move} stones.")
        
        stones -= move
        player_turn = not player_turn
    
    if player_turn:
        print("\nAI wins!")
    else:
        print("\nYou win!")


play_game()

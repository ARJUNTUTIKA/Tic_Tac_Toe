import random

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"

def print_board(board):
    print("\n" + BOLD + "      Current Board:" + RESET + "\n")
    for i in range(3):
        row = board[i]
        print("      " + " | ".join(color_symbol(cell) for cell in row))
        if i < 2:
            print("     ---+---+---")
    print()

def color_symbol(symbol):
    if symbol == "X":
        return BOLD + RED + "X" + RESET
    elif symbol == "O":
        return BOLD + BLUE + "O" + RESET
    else:
        return " "

def check_win(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]): return True
        if all(board[j][i] == symbol for j in range(3)): return True
    if all(board[i][i] == symbol for i in range(3)): return True
    if all(board[i][2 - i] == symbol for i in range(3)): return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_position(choice):
    mapping = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
    }
    return mapping.get(choice, None)

def show_grid_numbers():
    print("\n" + BOLD + MAGENTA + "      Grid Positions:" + RESET)
    print("      1 | 2 | 3")
    print("     ---+---+---")
    print("      4 | 5 | 6")
    print("     ---+---+---")
    print("      7 | 8 | 9\n")

def get_available_moves(board):
    return [i for i in range(1, 10) if board[get_position(i)[0]][get_position(i)[1]] == " "]

def computer_move(board):
    return random.choice(get_available_moves(board))

def get_symbol_choice(player_name):
    while True:
        symbol = input(BOLD + f"\n{player_name}, choose your symbol (X or O): " + RESET).strip().upper()
        if symbol in ['X', 'O']:
            return symbol
        else:
            print(RED + "❌ Invalid symbol. Please choose X or O." + RESET)

def play_game():
    print(BOLD + GREEN + "\n🎮 Welcome to Tic-Tac-Toe!\n" + RESET)
    print(YELLOW + "1. Play with Player")
    print("2. Play with Computer" + RESET)

    mode = input(BOLD + "\nChoose mode (1 or 2): " + RESET).strip()

    if mode == "1":
        player1 = input(BOLD + "\nEnter Player 1 name: " + RESET)
        player2 = input(BOLD + "Enter Player 2 name: " + RESET)
    elif mode == "2":
        player1 = input(BOLD + "\nEnter your name: " + RESET)
        player2 = "Computer"
    else:
        print(RED + "\n❌ Invalid selection. Exiting.\n" + RESET)
        return

    player1_symbol = get_symbol_choice(player1)
    player2_symbol = "O" if player1_symbol == "X" else "X"

    symbols = {player1: player1_symbol, player2: player2_symbol}
    players = [player1, player2]
    scores = {player1: 0, player2: 0, "Draws": 0}

    print(GREEN + f"\n✅ {player1} will be '{player1_symbol}' and {player2} will be '{player2_symbol}'." + RESET)

    round_number = 1

    while True:
        print(BOLD + CYAN + f"\n🔁 Starting Round {round_number}..." + RESET)
        board = [[" " for _ in range(3)] for _ in range(3)]
        turn = 0
        show_grid_numbers()

        while True:
            print_board(board)
            current_player = players[turn % 2]
            symbol = symbols[current_player]
            print(BOLD + f"👉 {current_player}'s turn ({color_symbol(symbol)}):" + RESET)

            if current_player == "Computer":
                move = computer_move(board)
                print(YELLOW + f"🤖 Computer chose: {move}" + RESET)
            else:
                try:
                    move = int(input("Choose position (1-9): "))
                except ValueError:
                    print(RED + "❌ Enter a valid number (1–9)." + RESET)
                    continue

            pos = get_position(move)
            if pos:
                row, col = pos
                if board[row][col] == " ":
                    board[row][col] = symbol
                    if check_win(board, symbol):
                        print_board(board)
                        print(GREEN + f"🎉 {current_player} wins this round!" + RESET)
                        scores[current_player] += 1
                        break
                    elif is_draw(board):
                        print_board(board)
                        print(MAGENTA + "🤝 It's a draw!" + RESET)
                        scores["Draws"] += 1
                        break
                    turn += 1
                else:
                    if current_player != "Computer":
                        print(RED + "❗ That spot is taken. Try again." + RESET)
            else:
                if current_player != "Computer":
                    print(RED + "❗ Invalid position. Use 1–9." + RESET)

        print(BOLD + "\n📊 Scoreboard:" + RESET)
        print(f"{player1}: {scores[player1]} wins")
        print(f"{player2}: {scores[player2]} wins")
        print(f"Draws : {scores['Draws']}")

        again = input(BOLD + "\nPlay another round? (yes/no): " + RESET).strip().lower()
        if again not in ["yes", "y"]:
            print(BOLD + "\n👋 Thanks for playing Tic-Tac-Toe! Goodbye!\n" + RESET)
            break

        round_number += 1

# Run the game
play_game()

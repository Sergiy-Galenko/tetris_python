def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input("Введіть номер рядка (0, 1 або 2): "))
        col = int(input("Введіть номер стовпця (0, 1 або 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Гравець '{current_player}' виграв!")
                break
            elif all(cell != " " for row in board for cell in row):
                print_board(board)
                print("Гра закінчилася в нічию!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Ця клітинка вже зайнята. Оберіть іншу.")

if __name__ == "__main__":
    main()
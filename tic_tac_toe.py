main_board = [["-", "-", "-"] for _ in range(3)]


def check_win(signature):
    first_diagonal = [main_board[i][i] for i in range(3)]
    second_diagonal = [main_board[0][2], main_board[1][1], main_board[2][0]]

    for i in range(len(main_board)):
        row = main_board[i]
        col = [row[i] for row in main_board]
        if row.count(signature) == 3 or col.count(signature) == 3:
            return True

    return first_diagonal.count(signature) == 3 or second_diagonal.count(signature) == 3


def update_board(board, board_place, user_signature):
    if board_place > 8 or board_place < 0:
        return "incorrect place"
    col = board_place % 3
    row = board_place // 3
    if board[row][col] != "-":
        return "Already taken"

    board[row][col] = user_signature
    return draw_board(board)


def draw_instructions():
    instruction = [[k, k + 1, k + 2] for k in range(0, 9, 3)]
    print("Numbers corresponding to places")
    for k in instruction:
        print(*k, sep="|")


def draw_board(board):
    for j in board:
        print(*j, sep='|')


def turns(t):
    if t % 2 == 0:
        return "X"
    return "O"



def play():
    turn = 0
    while True:

        sig = turns(turn)
        print(f"Player: {sig}'s turn")

        get_input = int(input())
        next_turn = update_board(main_board, get_input, sig)
        if next_turn:
            print(f"{next_turn}")
            turn -= 1

        if check_win(sig):
            print(f"Player: {sig} Won!")

            return
        turn += 1
        if turn == 9:
            print("Tie")
            return





def main():
    draw_instructions()
    play()


main()

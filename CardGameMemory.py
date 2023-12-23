import random
def create():
    cards = list(range(1, 9)) * 2
    random.shuffle(cards)
    board = [["*" for i in range(4)] for i in range(4)]
    return board, cards
def show(board):
    for row in board:
        print(" ".join(str(card) if card is not None else '*' for card in row))
    print()
def cardzzz(facedup):
    while True:
        row, col = map(int, input("Enter the row (1 to 4) and col (1 to 4) position of the pair separated by space (ex: 4 1): ").split())
        if 1 <= row <= 4 and 1 <= col <= 4:
            if facedup[row - 1][col - 1]:
                print("Card at this position is already faced up. Select position again.")
            else:
                return row - 1, col - 1
        else:
            print("Invalid position.")
def play():
    board, cards = create()
    facedup = [[False] * 4 for i in range(4)]
    pairsfound = 0
    while pairsfound < 8:
        show(board)
        firstrow, firstcol = cardzzz(facedup)
        if facedup[firstrow][firstcol]:
            continue
        board[firstrow][firstcol] = cards[firstrow * 4 + firstcol]
        show(board)
        secondrow, secondcol = cardzzz(facedup)
        if facedup[secondrow][secondcol] or (secondrow == firstrow and secondcol == firstcol):
            print("Invalid position.")
            board[firstrow][firstcol] = "*"
            continue
        board[secondrow][secondcol] = cards[secondrow * 4 + secondcol]
        if cards[firstrow * 4 + firstcol] == cards[secondrow * 4 + secondcol]:
            print("Pair match!")
            facedup[firstrow][firstcol] = facedup[secondrow][secondcol] = True
            pairsfound += 1
        else:
            print("Pair does not match. Try again!")
            board[firstrow][firstcol] = board[secondrow][secondcol] = "*"

    print("Enter any key to continue...")
def yaaaaaaay():
    play()

yaaaaaaay()


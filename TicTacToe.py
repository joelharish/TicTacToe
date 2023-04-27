import random

# Loop the board space for input

board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def isWinner(boardW, letterW):
    return (boardW[7] == letterW and boardW[8] == letterW and boardW[9] == letterW) or (
            boardW[4] == letterW and boardW[5] == letterW and boardW[6] == letterW) or (
            boardW[1] == letterW and boardW[2] == letterW and boardW[3] == letterW) or (
            boardW[1] == letterW and boardW[4] == letterW and boardW[7] == letterW) or (
            boardW[2] == letterW and boardW[5] == letterW and boardW[8] == letterW) or (
            boardW[3] == letterW and boardW[6] == letterW and boardW[9] == letterW) or (
            boardW[1] == letterW and boardW[5] == letterW and boardW[9] == letterW) or (
            boardW[3] == letterW and boardW[5] == letterW and boardW[7] == letterW)


def playerMove():
    run = True
    while run:
        move = input("Enter a number with in 1 to 9 : ")
        try:
            move = int(move)
            if move > 0 and move <= 9:
                if spaceIsFree(move):
                    run = False
                    insertLetter('x', move)
                else:
                    print("Sorry this space is not empty")
            else:
                print("Please tpe a number with in the range")
        except:
            print("Please enter a number")


def compMove():
    # AI for playing Tic tac toe

    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    cornersOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    return move


def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("Wellcome to tic tac toe game")
    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'o')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry computer won this time")
            break
        if not (isWinner(board, 'x')):
            move = compMove()
            if move == 0:
                print("Tie")
            else:
                insertLetter('o', move)
                print(f"Computer placed an 'o' in position {move}")
                printBoard(board)
        else:
            print("Good job, you won this time :)")
            break
    if isBoardFull(board):
        print("Tie")


main()
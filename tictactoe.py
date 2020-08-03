# This should be the first line in your program
board = [' ' for x in range(10)]
# board is now: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def insertBoard(letter, pos):
    board[pos] = letter


def spaceIsFree(pos):
    return board[pos] == ' '
# This function will return a True or False value


def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def playerMove():
    def playerMove():
    run = True
    while run:  # Keep looping until we get a valid move
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:  # makes sure we type in a number between 1-9
                # check if the move we choose is valid (no other letter is there already)
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('This position is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def selectRandom(li):
    pass


def compMove():
    pass


def isBoardFull(board):
    def isBoardFull(board):
    if board.count(' ') > 1:  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True


def printBoard():
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def main():
    def main():
        # Main game loop
    print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.')
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard()
        else:
            print('O\'s win this time...')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                insertBoard('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard()
        else:
            print('X\'s win, good job!')
            break

    if isBoardFull(board):
        print('Game is a tie! No more spaces left to move.')

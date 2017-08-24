class Game:
    token = " * "
    streak = 0
    victory = False
    board = [[None for i in range(7)]for j in range(6)]

    def __init__(self):
        for i in range(6):
            for j in range(7):
               self.board[i][j] = " "

    def showBoard(self):
        a = " "
        for i in range(5,0):
            for j in range(7):
                a += " | " + self.board[i][j]
        print(a)

class test:

    def main():
        g = Game()
        g.showBoard()
    main()

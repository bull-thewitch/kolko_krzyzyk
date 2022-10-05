class Tic:

    def __init__(self):
        self.new_game()

    def new_game(self):
        self.next_sign = "O"
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.winner = ""
        self.counter = 0

    def new_move(self, y, x):
        if ((y >= 0 and y <= 2) and (x >= 0 and x <= 2)) and self.board[y][x] == " ":
            self.board[y][x] = self.next_sign
            self.counter += 1
            if self.is_winner(y, x) == True:
                self.winner = self.next_sign
                return
            if self.next_sign == "O":
                self.next_sign = "X"
            else:
                self.next_sign = "O"
        else:
            print("sorry, error")

    def is_winner(self, y, x):
        if self.board[y][0] == self.board[y][1] and self.board[y][1] == self.board[y][2]:
            return True
        if self.board[0][x] == self.board[1][x] and self.board[1][x] == self.board[2][x]:
            return True
        if x == y:
            if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
                return True
        if x + y == 2:
            if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
                return True
        

    def __str__(self):
        res = ""
        for y in range(3):
            for x in range(3):
                res = res + self.board[y][x]
                if x < 2:
                    res = res + "|"
            if y < 2: 
                res = res + "\n-----"
            res = res + "\n"
        
        if self.winner != "":
            res = res + "Wygrał " + self.winner + "\n"
        elif self.counter == 9:
            res = res + "Remis\n"
        return res

c = Tic()
print(c)
while c.winner == "" and c.counter < 9:
    x = int(input("Podaj x dla {}: ".format(c.next_sign)))
    y = int(input("Podaj y dla {}: ".format(c.next_sign)))
    c.new_move(y, x)
    print(c)


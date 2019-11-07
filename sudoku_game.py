import copy
import math


class SudokuFather():

    def __init__(self, length, quadrant):
        self.board = []
        self.base_numbers = []
        self.length = length
        self.error_message = ''
        self.board_region = ''
        self.board_column = ''
        self.quadrant = quadrant
        self.is_playing = True
        self.displayed_board = []

    def set_board(self, board):
    
        self.board = board
        self.set_base_numbers()
    
    def check_base_number(self, row, column):
        if (row, column) in self.base_numbers:
            return False
        else:
            return True
    
    def set_base_numbers(self):
        self.base_numbers = []
        for i in range(self.length):
            for j in range(len(self.board[i])):
                if (self.board[i][j] != "x"):
                    self.base_numbers.append((i, j))
    
    def win(self):
        count = 0
        for i in range(self.length):
            for j in range(len(self.board[i])):
                if (self.board[i][j] != "x"):
                    count += 0
                else:
                    count += 1
        if count != 0:
            return False
        else:
            return True
        
    
        

    def check_rows(self, tabla):
        
        for fil in tabla:
            for n in range(self.length):
                self.elem = fil.pop(n)
                if self.elem in fil and self.elem != "x":
                    return False
                fil.insert(n, self.elem)
        return True

   
    def validate_board(self):

    
        if not self.check_rows(self.board):
            return False

        
        self.tablaT = []
        for i in range(self.length):
            self.column = []
            for j in range(self.length):
                self.column.append(self.board[j][i])
            self.tablaT.append(self.column)

        if not self.check_rows(self.tablaT):
            return False

        
        self.region_list = []
        for i in range(0, self.length, self.quadrant):
            for j in range(0, self.length, self.quadrant):
                self.listaZ = []
                for x in range(self.quadrant):
                    self.listaZ.extend(self.board[i+x][j:j+self.quadrant])
                self.region_list.append(self.listaZ)

        if not self.check_rows(self.region_list):
            return False
        return True

    def get_Display_Board(self):
        self.displayed_board = ""
        for i in range(self.length):
            if i == self.quadrant or i == self.quadrant*2:
                for n in range(self.length):
                    self.displayed_board += "--"
                    if n == self.quadrant-1 or n == self.quadrant*2-1:
                        self.displayed_board += "+-"
                if n == self.quadrant-1 or n == self.quadrant*2-1:
                    self.displayed_board = self.displayed_board[:-3]
                self.displayed_board += "\n"
            for j in range(self.length):
                if j == self.quadrant or j == self.quadrant*2:
                    self.displayed_board += "| "
                self.displayed_board += self.board[i][j] + " "
            self.displayed_board += "\n"

        return self.displayed_board

    
    def insert_number(self, numero, x, y):
        self.error_message = ""
        self.tabla_temp = copy.deepcopy(self.board)
        self.board[x][y] = str(numero)

        if (not self.validate_board() or not self.check_base_number(x,y)):
            self.board = self.tabla_temp
            return "Ilegal Value, Or trying to Replace Base Number"
        
        return print(self.get_Display_Board())

  
    

class Sudoku9x9(SudokuFather):
    def __init__(self):
        super().__init__(9, 3)


class Sudoku4x4(SudokuFather):
    def __init__(self):
        super().__init__(4, 2)
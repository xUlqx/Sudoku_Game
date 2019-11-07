from board_api import BoardApi
from sudoku_game import Sudoku9x9, Sudoku4x4

class Interface:
    
    def __init__(self):
        self.board = []
        self.formatted_board = ''
        self.game_level = ''
        self.board_size = ''
        self.game_object = ''
        self.number = ''
        self.row = ''
        self.column = ''
        
    
    def game_menu(self):

        game_level = ''
        board_size = ""

        print("**************************")
        print("Welcome To The Sudoku Game")
        print("**************************")

        while game_level not in ('1', '2', '3'):
            game_level = input("Select the Game Level:\n1: Easy\n2: Normal\n3: Hard\n**************************\nAnswer: ")
            if game_level not in ('1', '2', '3'):
                print("Please answer with '1', '2' or '3'\n ")

        while board_size not in ('4', '9'):
            board_size = input("\n**************************\nSelect the Board Size: '4' or '9'\n**************************\nAnswer: ").lower()
            if board_size not in ('4', '9'):
                print("Please answer with '4' or '9'\n ")

        if board_size == "9":
            self.board_size = 9
            self.game_object = Sudoku9x9()

        elif board_size == "4":
            self.board_size = 4
            self.game_object = Sudoku4x4()
        
    def game_started(self):
        
        board_api = BoardApi(self.game_level, self.board_size)
        board = board_api.get_new_board()     
        self.game_object.set_board(board)
        print("\n**************************")
        print("      Game Started!")
        print("**************************\n")
    
    def playing(self):
        #self.game_object.play(self.number, self.row, self.column)
        while not self.game_object.win():
            #print(self.game_object.get_Display_Board())
            self.player_inputs()
            #self.game_object.is_playing = self.game_object.win()
            #if self.game_object.error_message != '':
               # print("\nError:\number" + self.game_object.error_message)
            
            #self.game_object.play(self.number, self.row, self.column)
            
        print(self.game_object.get_Display_Board())
        print("Congratulations! You Win!")

    def player_inputs(self):
        print(self.game_object.get_Display_Board())
        self.number = input("Insert Number: ")
        self.row = input("Insert Row:  ")
        self.column = input("Insert Column:   ")

        if self.check_valid_inputs(self.number, self.row, self.column):
            return self.game_object.insert_number(self.number, int(self.row)-1, int(self.column)-1)
        else:
            return print("\nPls Insert Valid Values")

    
    def check_valid_inputs(self, number, row, column):
        try:
            if int(row) > self.board_size or int(row) < 1:
                return False
            elif int(column) > self.board_size or int(column) < 1:
                return False
            elif number != "x":
                if int(number) > 0 and int(number) < self.board_size+1:
                    return True
            else:
                return True
        except Exception:
            return False
        
        


            
if __name__ == "__main__":
    player = Interface()
    player.game_menu()
    player.game_started()
    player.playing()
   
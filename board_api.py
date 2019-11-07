import requests

class BoardApi():
    def __init__(self, level=1, size=9):
        self.board = [

                ['x' for _ in range(int(size))] for _ in range(int(size))
               
                ]

        if level not in [1, 2, 3]:
            level = 1

        url = "http://www.cs.utep.edu/cheon/ws/sudoku/new/?level=" + str(level) + "&size=" + str(size)

        self.res = requests.get(url)

    def get_new_board(self, mock_response=None):

        if mock_response:
            self.res = mock_response
        res = self.res.json()
        for val in res["squares"]:
            x = val['x']
            y = val['y']
            value = val['value']
            self.board[x][y] = str(value)
        return self.board

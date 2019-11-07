FROM python:3

RUN git clone https://github.com/xUlqx/Sudoku_Game
WORKDIR /Sudoku_Game

RUN pip install -r requirements.txt

CMD [ "python3", "final_tests.py" ] && [ "python3", "sudoku_interface.py" ]

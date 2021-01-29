class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

        def print_board(self):
            for row in [self.board[1*3:(i+1)*3]]:
                print('| ' + ' | '.join(row)+ ' | ')
    
        @staticmethod
        def print_board_nums():
            number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
            for now in number_board:
                print('| ' + ' | '.join(row)+ ' | ')


        def available_moves(self):
            return[i for i, spot in enumerate(self.board) if spot == ' ']
            #moves = []
            #for(i,spot) in enumerate(self.board):
            #    ['x', 'x', 'o'] --> [(0, 'x'), (2,'o')]
            #    if spot == ' ':
            #        moves.append(i)
            #    return moves
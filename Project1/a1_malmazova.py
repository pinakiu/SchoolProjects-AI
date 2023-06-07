'''
Mahri Almazova
Pinaki Upadhyay 
06/07/2023
Project 1
'''
import math
import time
import random


class HumanPlayer():
    def __init__(self, ):
        self.letter = 'X'

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class ComputerPlayer():
    def __init__(self):
        self.letter = 'O'

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter, -math.inf, math.inf)['position'] #when calling minimax, pass in alpha and beta
        return square

    def minimax(self, state, player, alpha, beta): #added alpha beta as parameters 
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # Base cases for terminal states
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}
            for possible_move in state.available_moves(): 
                #simulate each move by making a copy of the board and trying the move
                state.make_move(possible_move, player)
                sim_score = self.minimax(state, other_player, alpha, beta)

                # make sure to undo the move
                state.board[possible_move] = ' '
                state.current_winner = None

                #save score of possible move into dict
                sim_score['position'] = possible_move
                if sim_score['score'] > best['score']:
                    best = sim_score

                # Alpha-beta pruning - check if current best is greater than beta
                alpha = max(alpha, best['score'])
                if alpha >= beta:
                    break

            return best
        else:
            best = {'position': None, 'score': math.inf}
            for possible_move in state.available_moves():

                state.make_move(possible_move, player)
                sim_score = self.minimax(state, other_player, alpha, beta)

                state.board[possible_move] = ' '
                state.current_winner = None

                sim_score['position'] = possible_move
                if sim_score['score'] < best['score']:
                    best = sim_score

                # Alpha-beta pruning
                beta = min(beta, best['score'])
                if beta <= alpha:
                    break

            return best
    
class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def reset(self):
        self.board = self.make_board()
        self.current_winner = None
        
    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
    

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(letter + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

def new_game(t):
    valid_entry = ['y','n']
    next_round = input("Would you like to start a new game? (Y/N)\n=> ")
    while not next_round.isalpha() or next_round.lower() not in valid_entry:
        next_round = input("Invalid entry. Please enter Y/N\n=> ")
    if next_round.lower() == 'y':
        t.reset()
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    print("Welcome to the Tic Tac Toe Game!")
    print("You will be playing against the computer")
    new_round = True
    x_player = HumanPlayer()
    o_player = ComputerPlayer()
    t = TicTacToe()
    while(new_round):
        play(t, x_player, o_player, print_game=True)
        new_round = new_game(t)

            
   
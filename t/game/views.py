from django.shortcuts import render
from . import utils
import json
from django.http import JsonResponse



def tictactoe(request):
    game = utils.TicTacToe()  # Initialize the TicTacToe game
    x_player = utils.HumanPlayer()
    o_player = utils.ComputerPlayer()
    letter = 'X'
    if request.method == 'POST':
        while game.empty_squares():
            if letter == 'X':
                print('x')
                move = request.POST.get('hidden_square')
                print(move)
            else:
                print('y')
                letter = 'O'
                move = o_player.get_move()
                
            if game.make_move(move,letter):
                letter = 'O' if letter == 'X' else 'X'


        # Call the play method of the TicTacToe object to handle the move
        # utils.web_play(game,x_player,o_player, x_move)

        # Check if game is over and determine the winner or draw
        # game_over, winner = game.check_game_over()

        # Render the updated game board
        # return render(request, 'game.html', {'board': game.board, 'game_over': game_over, 'winner': winner})
        return JsonResponse({'cellId': move, 'move': letter})
    else:
        # Render the initial game board
        return render(request, 'game.html', {'board': game.board, 'game_over': False, 'winner': None})





# from django.shortcuts import render
# import time 


# def tictactoe(request):
#     if request.method == 'POST':
#         move = request.POST.get('move')
#         row, col = map(int, move.split(','))
        
#         # Call your Python code to handle the move and update the game state
#         letter = 'X'
#         while game.empty_squares():
#             if letter == 'O':
#                 square = o_player.get_move(game)
#             else:
#                 square = x_player.get_move(game)
#             if game.make_move(square, letter):

#                 if print_game:
#                     print(letter + ' makes a move to square {}'.format(square))
#                     game.print_board()
#                     print('')

#                 if game.current_winner:
#                     if print_game:
#                         print(letter + ' wins!')
#                     return letter  # ends the loop and exits the game
#                 letter = 'O' if letter == 'X' else 'X'  # switches player

#             time.sleep(.8)
#         # Sample code to update the game board (replace it with your logic)
#         board = [['', '', ''], ['', '', ''], ['', '', '']]
#         board[row][col] = 'X'  # Assuming 'X' is the current player
#         # End of sample code
        
#         # Check if game is over and determine the winner or draw
        
#         # Render the updated game board
#         return render(request, 'game.html', {'board': board})
#     else:
#         return render(request, 'game.html', {'board': [['', '', ''], ['', '', ''], ['', '', '']]})

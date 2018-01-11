"""
Muneeb Ansari
Tic Tac Toe - PvP
"""
import random


def construct_board(the_board):
    """Build the game board."""
    print('\n   |   |')
    print(' ' + the_board[1] + ' | ' + the_board[2] + ' | ' + the_board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + the_board[4] + ' | ' + the_board[5] + ' | ' + the_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + the_board[7] + ' | ' + the_board[8] + ' | ' + the_board[9])
    print('   |   |\n')


def free_space(the_board, pos):
    """Return True if the position <pos> on game board <the_board> is
    unoccupied.
    """
    return the_board[pos] == ' '


def winner_across(the_board, char):
    """Retrun True if the game has been won by horizontal placement."""
    return ((the_board[1] == the_board[2] == the_board[3] == char) or
            (the_board[4] == the_board[5] == the_board[6] == char) or
            (the_board[7] == the_board[8] == the_board[9] == char))


def winner_down(the_board, char):
    """Retrun True if the game has been won by vertical placement."""
    return ((the_board[1] == the_board[4] == the_board[7] == char) or
            (the_board[2] == the_board[5] == the_board[8] == char) or
            (the_board[3] == the_board[6] == the_board[9] == char))


def winner_diagonal(the_board, char):
    """Retrun True if the game has been won by diagonal placement."""
    return ((the_board[1] == the_board[5] == the_board[9] == char) or
            (the_board[3] == the_board[5] == the_board[7] == char))


def game_winner(the_board, char):
    """Return True if the game has been won."""
    return (winner_across(board, char) or winner_diagonal(the_board, char) or
            winner_down(the_board, char))


def check_draw(the_board):
    """Return True if the game ends in a draw."""
    draw = True
    for i in range(1, 9):
        if free_space(the_board, i):
            draw = False
    return draw


def character_selection(char_selected):
    """Return character pair corresponding to character selected."""
    # Player 1 selection in pos. 1, player 2 selection pos. 2
    return ('x', 'o') if char_selected.lower() == 'x' else ('o', 'x')


def move(the_board, pos, char):
    """Make move on game board with character <char> in position <pos>."""
    board[pos] = char
    construct_board(the_board)


def go_first():
    """Return which player makes the first move."""
    rand_val = random.randint(0, 1)
    return 'P1' if rand_val == 0 else "P2"


def valid_move_number(curr_move):
    """Check if move is a valid move number"""
    return curr_move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def select_character(char):
    """Return character pair"""
    return character_selection(char)


def rematch():
    """Return True if rematch is requested."""
    player_response = input('Would you like a rematch? (Yes/No) \n').lower()
    while not (player_response == "yes" or player_response == "no"):
        player_response = input(
            "Please enter 'yes' for a rematch or 'no' to exit \n").lower()
    return player_response == 'yes'


def game_stats(num_games, p1_wins, p2_wins, num_drawn):
    """Display game statistics."""
    print("-------- STATISTICS --------\n")
    print("Games Played: " + str(num_games))
    print("Player 1 Wins: " + str(p1_wins))
    print("Player 2 Wins: " + str(p2_wins))
    print("Tied Games: " + str(num_drawn))
    print("----------------------------\n")


def game_header():
    """Display game header."""
    print('**************************** PYTHON: CONSOLE '
          'TIC-TAC-TOE ***************************')
    print('********************************** MUNEEB ANSARI '
          '***********************************')
    print('*************************************** PvP '
          '****************************************')
    print('')


if __name__ == "__main__":

    game_header()

    player1_wins, player2_wins, games_played, games_drawn = 0, 0, 0, 0
    while True:
        # Game Set-up
        board = [' ' for _ in range(10)]

        character = input("\nPick 'x' or 'o': ")
        while not (character.lower() == 'x' or character.lower() == 'o'):
            character = input("Invalid, pick 'x' or 'o':")

        player1_char = character_selection(character)[0]
        player2_char = character_selection(character)[1]

        print('\nPlayer 1 picked: ' + player1_char)
        print('Player 2 defaults: ' + player2_char)

        construct_board(board)
        first = go_first()
        game_on = True

        while game_on:
            if first == 'P1':

                current_move = input("Player 1, make your move:")
                # Check validity of move
                while not valid_move_number(current_move) or \
                        not free_space(board, int(current_move)):
                    current_move = input("Invalid move / space not available, "
                                         "Player 1,  try again:")

                # Make move
                move(board, int(current_move), player1_char)

                # Check if player wins
                if game_winner(board, player1_char):
                    print("PLAYER 1 is the WINNER \n")
                    games_played = 0
                    player1_wins += 1
                    game_stats(games_played, player1_wins, player2_wins,
                               games_drawn)
                    game_on = False
                else:
                    if check_draw(board):
                        print("GAME ENDS IN DRAW \n")
                        games_played += 1
                        games_drawn += 1
                        game_stats(games_played, player1_wins, player2_wins,
                                   games_drawn)
                        game_on = False
                first = 'P2'
            else:

                current_move = input("Player 2, make your move:")
                # Check validity of move
                while not valid_move_number(current_move) or not \
                        free_space(board, int(current_move)):

                    current_move = input("Invalid move / space not available, "
                                         "Player 2,  try again:")

                # Make move
                move(board, int(current_move), player2_char)

                # Check if player wins
                if game_winner(board, player2_char):
                    print("PLAYER 2 is the WINNER \n")
                    games_played += 1
                    player2_wins += 1
                    game_stats(games_played, player1_wins, player2_wins,
                               games_drawn)
                    game_on = False
                else:
                    if check_draw(board):
                        print("GAME ENDS IN DRAW \n")
                        games_played += 1
                        games_drawn += 1
                        game_stats(games_played, player1_wins, player2_wins,
                                   games_drawn)
                        game_on = False
                first = 'P1'

        if not rematch():
            break

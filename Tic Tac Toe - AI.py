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


def move_no_print(the_board, pos, char):
    """Does not print move on game board"""
    the_board[pos] = char


def go_first():
    """Return which player makes the first move."""
    rand_val = random.randint(0, 1)
    return 'P1' if rand_val == 0 else "P2"


def switch_turns(current_turn):
    """Switch to other player's turn"""
    return 'C' if current_turn == "P1" else 'P1'


def valid_move_number(curr_move):
    """Check if move is a valid move number"""
    return curr_move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def rematch():
    """Return True if rematch is requested."""
    player_response = input('Would you like a rematch? (Yes/No) \n').lower()
    while not (player_response == "yes" or player_response == "no"):
        player_response = input(
            "Please enter 'yes' for a rematch or 'no' to exit \n").lower()
    return player_response == 'yes'


def get_comp_move(the_board, char_player, char_comp):
    """Return the computer's move based on current state of board."""
    # Strategy for computer AI refrenced from
    # https://en.wikipedia.org/wiki/Tic-tac-toe

    # Take Middle if available
    if free_space(the_board, 5):
        move(the_board, 5, char_comp)
    else:
        # Make winning move
        for i in range(1, 10):
            board_copy = the_board[:]
            if free_space(board_copy, i):
                move_no_print(board_copy, i, char_comp)
                if game_winner(board_copy, char_comp):
                    return move(the_board, i, char_comp)

        # Block player's win
        for i in range(1, 10):
            board_copy = the_board[:]
            if free_space(board_copy, i):
                move_no_print(board_copy, i, char_player)
                if game_winner(board_copy, char_player):
                    return move(the_board, i, char_comp)

        # Attempt to create a left fork
        if board[1] == board[9] == comp_char and free_space(board, 7):
            return move(board, 7, comp_char)

        # Attemp to create a right fork
        elif board[3] == board[7] == comp_char and free_space(board, 9):
            return move(board, 9, comp_char)

        # play in the open spot
        else:

            for i in range(1, 10):
                if free_space(board, i):
                    move(board, i, char_comp)
                    break


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
    print('*************************************** Player Vs. Compter '
          '****************************************')
    print('')


if __name__ == "__main__":

    game_header()
    computer_wins, player_wins, games_played, games_drawn = 0, 0, 0, 0

    while True:
        board = [' ' for _ in range(10)]

        character = input("\nPick 'x' or 'o': ")
        while not (character.lower() == 'x' or character.lower() == 'o'):
            character = input("Invalid, pick 'x' or 'o':")

        player1_char = character_selection(character)[0]
        comp_char = character_selection(character)[1]

        print('\nPlayer 1 picked: ' + player1_char)
        print('Computer defaults: ' + comp_char)

        construct_board(board)
        first = go_first()
        game_on = True

        while game_on:
            if first == 'P1':
                current_move = input("Player 1, make your move:")
                while not valid_move_number(current_move) or not \
                        free_space(board, int(current_move)):
                    current_move = input("Invalid move / space not available, "
                                         "Player 1,  try again:")

                move(board, int(current_move), player1_char)

                if game_winner(board, player1_char):
                    print("PLAYER 1 is the WINNER! \n")
                    games_played = 0
                    player_wins += 1
                    game_stats(games_played, computer_wins, player_wins,
                               games_drawn)
                    game_on = False
                else:
                    if check_draw(board):
                        print("GAME ENDS IN DRAW \n")
                        games_played += 1
                        games_drawn += 1
                        game_stats(games_played, computer_wins, player_wins,
                                   games_drawn)
                        game_on = False
                first = switch_turns(first)
            else:

                get_comp_move(board, player1_char, comp_char)

                if game_winner(board, comp_char):
                    print("Computer is the WINNER! \n")
                    games_played += 1
                    computer_wins += 1
                    game_stats(games_played, computer_wins, player_wins,
                               games_drawn)
                    game_on = False
                else:
                    if check_draw(board):
                        print("GAME ENDS IN DRAW \n")
                        games_played += 1
                        games_drawn += 1
                        game_stats(games_played, computer_wins, player_wins,
                                   games_drawn)
                        game_on = False
                first = switch_turns(first)

        if not rematch():
            break

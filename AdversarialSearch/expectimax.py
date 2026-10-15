from game import utility, legal_moves, play_move, other_player


def expectimax(board, player):
    # TODO: geef de eindscore terug als het spel afgelopen is.
    # TODO: X kiest het maximum van de kindwaarden.
    # TODO: O kiest elke toegestane zet met dezelfde kans: neem het gemiddelde.
    u = utility(board)
    if u is not None:
        return u

    def mim(cs, ns, p):
        if cs is None:
            return ns
        return (min if p == 'O' else max)(cs, ns)

    highest_score = None
    sum_score = None
    moves = legal_moves(board)
    for move in moves:
        new_board = play_move(board, move, player)
        new_score = expectimax(new_board, other_player(player))
        if highest_score is None or new_score > highest_score:
            highest_score = new_score
        if sum_score is None:
            sum_score = new_score
        else:
            sum_score += new_score

    avg = (None if sum_score is None else sum_score / len(moves))
    return (highest_score if player == 'X' else avg)


if __name__ == '__main__':
    board = ('X', 'X', '.', 'O', 'O', '.', '.', '.', '.')
    value = expectimax(board, 'X')

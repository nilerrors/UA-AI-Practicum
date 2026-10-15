from game import utility, legal_moves, play_move, other_player


def minimax(board, player):
    u = utility(board)
    if u is not None:
        return u

    def mim(cs, ns, p):
        if cs is None:
            return ns
        return (min if p == 'O' else max)(cs, ns)

    current_score = None
    for move in legal_moves(board):
        new_board = play_move(board, move, player)
        current_score = mim(current_score, minimax(new_board, other_player(player)), player)

    return current_score


if __name__ == '__main__':
    board = ('X', 'X', '.', 'O', 'O', '.', '.', '.', '.')
    value = minimax(board, 'X')

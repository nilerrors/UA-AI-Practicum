from game import utility, legal_moves, play_move, other_player


def alphabeta(board, player, alpha=float('-inf'), beta=float('inf')):
    # TODO: werk alpha bij voor X en beta voor O.
    u = utility(board)
    if u is not None:
        return u


    def ab(a, b, ns, p):
        if p == 'O':
            if a is None:
                return a, b, False
            if ns <= a: return a, b, True
            b = min(b, ns)
        else:
            if b is None:
                return a, b, False
            if ns >= b: return a, b, True
            a = max(a, ns)
        return a, b, False


    def mim(cs, ns, p):
        if cs is None:
            return ns
        return (min if p == 'O' else max)(cs, ns)

    a, b, current_score = None, None, None
    for move in legal_moves(board):
        new_board = play_move(board, move, player)
        new_score = alphabeta(new_board, other_player(player), a, b)
        a, b, ret = ab(a, b, new_score, player)
        if ret:
            return current_score
        current_score = mim(current_score, new_score, player)

    return current_score


if __name__ == '__main__':
    board = ('X', 'X', '.', 'O', 'O', '.', '.', '.', '.')
    value = alphabeta(board, 'X')

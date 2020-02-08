def solve(queen_count, permutator):
    """N-Queens solver.

    Args:
        queen_count: the number of queens to solve for. This is also the
            board size.

    Yields:
        Solutions to the problem. Each yielded value is looks like
        (3, 8, 2, 1, 4, ..., 6) where each number is the column position for the
        queen, and the index into the tuple indicates the row.
    """
    # From http://code.activestate.com/recipes/576647/
    # Changed to accept permutator function.
    cols = range(queen_count)
    for vec in permutator(cols):
        if (queen_count == len(set(vec[i] + i for i in cols))
                        == len(set(vec[i] - i for i in cols))):
            yield vec


def bench(queen_count, permutator):
    list(solve(queen_count, permutator))

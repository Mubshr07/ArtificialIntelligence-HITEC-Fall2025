import math

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': 4,
    'I': 2,
    'J': -3,
    'K': -6,
    'L': 7,
    'M': 0,
    'N': 5,
    'O': 8
}

def alpha_beta(node, alpha, beta, maximizing):
    if isinstance(tree[node], int):
        return tree[node]

    if maximizing:
        best = -math.inf
        for child in tree[node]:
            val = alpha_beta(child, alpha, beta, False)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for child in tree[node]:
            val = alpha_beta(child, alpha, beta, True)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


result = alpha_beta('A', -math.inf, math.inf, True)
print("Optimal value at root A:", result)

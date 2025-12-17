import math


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O']
}


values = {
    'H': 4, 'I': 2,
    'J': -3, 'K': -6,
    'L': 7, 'M': 0,
    'N': 5, 'O': 8
}

def alpha_beta(node, alpha, beta, is_max):
   
    if node not in tree:
        return values[node]

    if is_max:  
        best = -math.inf
        for child in tree[node]:
            best = max(best, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, best)
            if beta <= alpha:
                break  
        return best

    else:  
        best = math.inf
        for child in tree[node]:
            best = min(best, alpha_beta(child, alpha, beta, True))
            beta = min(beta, best)
            if beta <= alpha:
                break 
        return best


result = alpha_beta('A', -math.inf, math.inf, True)
print("Best value at root:", result)

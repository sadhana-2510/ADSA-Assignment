def matrix_chain_multiplication(dimensions):
    n = len(dimensions)
    
    # Create a table to store the minimum number of scalar multiplications
    # and the optimal split point for each subproblem.
    m = [[0] * n for _ in range(n)]
    split_points = [[0] * n for _ in range(n)]

    # Initialize the table for chains of length 2 to n.
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dimensions[i - 1][0] * dimensions[k][1] * dimensions[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    split_points[i][j] = k

    return m, split_points

def print_optimal_parenthesization(split_points, i, j):
    if i == j:
        print(f'Matrix {i}', end='')
    else:
        print('(', end='')
        print_optimal_parenthesization(split_points, i, split_points[i][j])
        print_optimal_parenthesization(split_points, split_points[i][j] + 1, j)
        print(')', end='')

# Example input
matrices = [(2, 3), (3, 4), (4, 2)]

# Solve the problem and print the results
m, split_points = matrix_chain_multiplication(matrices)
print("Optimal Parenthesization:", end=' ')
print_optimal_parenthesization(split_points, 1, len(matrices) - 1)
print("\nMinimum Scalar Multiplications:", m[1][len(matrices) - 1])

def matrix_chain_order(dims):
    """
    Matrix Chain Multiplication using Dynamic Programming
    """

    n = len(dims) - 1

    # m[i][j] = minimum multiplication cost
    m = [[0] * (n + 1) for _ in range(n + 1)]

    # s[i][j] = optimal split position
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):

                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + dims[i - 1] * dims[k] * dims[j]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):

    if i == j:
        return f"A{i}"

    k = s[i][j]

    left = print_optimal_parens(s, i, k)
    right = print_optimal_parens(s, k + 1, j)

    return f"({left} x {right})"


def print_dp_table(m, n):

    print("\nDP Cost Table m[i][j]:")
    print()

    # Header
    print(f"{'':>6}", end="")

    for j in range(1, n + 1):
        print(f"{j}A{'':>8}", end="")

    print()

    # Table rows
    for i in range(1, n + 1):

        print(f"A{i:<5}", end="")

        for j in range(1, n + 1):

            if j < i:
                print(f"{'---':>9}", end="")
            else:
                print(f"{m[i][j]:>9}", end="")

        print()


# --------------------------------------------------
# Matrix dimensions
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60
# A4 = 60 x 10
# --------------------------------------------------

dims = [10, 30, 5, 60, 10]

n = len(dims) - 1


print("Matrix Dimensions:")

for i in range(n):
    print(f" A{i + 1}: {dims[i]} x {dims[i + 1]}")


# --------------------------------------------------
# Matrix Chain Order
# --------------------------------------------------

m, s = matrix_chain_order(dims)

print(f"\nMinimum scalar multiplications: {m[1][n]}")

print(
    f"Optimal parenthesization: "
    f"{print_optimal_parens(s, 1, n)}"
)


# --------------------------------------------------
# DP Table
# --------------------------------------------------

print_dp_table(m, n)

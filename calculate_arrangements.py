def calculate_arrangements(N):
    if N <= 1:
        return 1
    return N * calculate_arrangements(N - 1)

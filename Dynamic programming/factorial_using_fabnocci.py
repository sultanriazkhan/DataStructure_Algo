def factorial(n, memo):
    if n<=1:
        return 1
    if memo[n]!=-1:
        return memo[n]
    memo[n] = n*factorial(n-1, memo)
    return memo[n]

if __name__ == "__main__":
    n = 6
    memo = [-1] * (n + 1)
    print(factorial(n, memo))
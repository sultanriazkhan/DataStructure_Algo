def sum_problem_sol(n, memo):
    if n == 0:
        return 0
    if memo[n]!=-2:
        return memo[n]
    memo[n]=n+sum_problem_sol(n-1, memo)
    return memo[n]
if __name__== "__main__":
    n=4
    memo=[-2]*(n+1)
    print(sum_problem_sol(n, memo))

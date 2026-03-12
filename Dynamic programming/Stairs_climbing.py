def stairs_climbing_prob(n, memo):
    if n<=1:
        return 1
    if memo[n]!=-1:
        return memo[n]
    memo[n]=stairs_climbing_prob(n-1, memo)+stairs_climbing_prob(n-2, memo)
    return memo[n]
if __name__ == "__main__":
    n=6
    memo=[-1]*(n+1)
    print(stairs_climbing_prob(n, memo))
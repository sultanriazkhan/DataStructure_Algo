def coin_change(amount, coins, memo):
    if amount == 0:
        return 0
    if amount <0:
        return float('inf')
    if amount in memo:
        return memo[amount]
    ans= float('inf')
    for coin in coins:
        ans= min(ans , 1+coin_change(amount-coin, coins, memo))
    memo[amount]=ans
    return ans
def coin_change_problem(amount, coins):
    memo={}
    res= coin_change(amount, coins, memo)
    return res if res!=float('inf') else -1
if __name__ == "__main__":
    amount=11
    coins=[1,2,5]
    print(coin_change_problem(amount, coins))
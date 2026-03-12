def least_csq(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store lengths of longest common subsequence
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The length of the longest common subsequence is in the bottom-right cell
    lcs_length = dp[m][n]

    # The length of the least common subsequence is the sum of lengths minus twice the LCS length
    least_cs_length = m + n - 2 * lcs_length

    return least_cs_length
if __name__ == "__main__":
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(least_csq(str1, str2))
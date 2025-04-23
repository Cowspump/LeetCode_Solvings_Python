class Solution:
    def generatematrix(self, n: int) -> list[list[int]]:

        ans = [[0 for num in range(n)] for _ in range(n)]

        l_border = 0
        r_border = n - 1

        top_border = 0
        bottom_border = n - 1

        cur = 1

        while cur <= n ** 2:

            for j in range(l_border, r_border + 1):
                ans[top_border][j] = cur
                cur += 1

            top_border += 1

            for i in range(top_border, bottom_border + 1):
                ans[i][r_border] = cur
                cur += 1
            r_border -= 1

            for j in range(r_border, l_border - 1, -1):
                ans[bottom_border][j] = cur
                cur += 1
            bottom_border -= 1

            for i in range(bottom_border, top_border - 1, -1):
                ans[i][l_border] = cur
                cur += 1
            l_border += 1

        return ans



solve = Solution()
print(solve.generatematrix(3))

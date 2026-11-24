class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = []
        for i in range(len(temperatures)):
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    ans.append(j-i)
                    break

            if len(ans)<= i:
                ans.append(0)

        return ans

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []
        stack = []

        for i in range(len(temperatures)-1, -1, -1):

            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()

            if stack:
                res.append(stack[-1][1] - i)
            else:
                res.append(0)

            stack.append([temperatures[i], i])

        return res[::-1]
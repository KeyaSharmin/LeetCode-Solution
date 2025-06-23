class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def fn(x):
            n = len(x) // 2
            for i in range(n, len(x)):
                if int(x[i]) + 1 < k:
                    x[i] = x[~i] = str(int(x[i])+1)
                    for j in range(n, i):
                        x[j] = x[~j] = "0"
                    return x
            return ["1"] + ["0"] * (len(x) - 1) + ["1"]
        x = ["0"]
        ans = 0
        for _ in range(n):
            while True:
                x = fn(x)
                # print(x)
                val = int("".join(x), k)
                if str(val)[::-1] == str(val):
                    print(x, val)
                    break
            ans += val
        return ans

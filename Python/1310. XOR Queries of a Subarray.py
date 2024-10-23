class Solution(object):
    def xorQueries(self, arr, queries):
        prefix = []
        xor = 0
        ans = []
        for ele in arr:
            xor = xor ^ ele
            prefix.append(xor)
        # print(prefix)
        for left, right in queries:
            if left != 0:
                xor = prefix[left - 1] ^ prefix[right]
            else:
                xor = prefix[right]
            ans.append(xor)
        return ans
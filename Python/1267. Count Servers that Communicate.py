class Solution:
  def countServers(self, G: List[List[int]]) -> int:
    count = 0
    for r in range(len(G)):
      s = sum(G[r])
      if s > 1:
        count += s
      elif s == 1:
        column = G[r].index(1)
        if sum(G[r][column] for r in range(len(G))) > 1:
          count += 1
       
    return count

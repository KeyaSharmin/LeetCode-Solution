from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Step 1: Sort the skill array
        skill.sort()
        
        total_skill = skill[0] + skill[-1]  # Required sum for each pair
        chemistry_sum = 0

        # Step 2: Pair players using two pointers
        for i in range(len(skill) // 2):
            
            if skill[i] + skill[-i - 1] != total_skill:
                return -1  
            chemistry_sum += skill[i] * skill[-i - 1]

        return chemistry_sum 
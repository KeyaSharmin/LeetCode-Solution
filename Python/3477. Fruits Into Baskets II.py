class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = len(fruits)

        for i, fruit in enumerate(fruits):
            for basket in baskets:
                if basket >= fruit:
                    baskets.remove(basket)
                    unplaced -=1
                    break
        return unplaced

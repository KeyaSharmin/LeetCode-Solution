class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        smeeting = sorted(meetings, key=lambda x: x[0])
        today = 0
        for b, e in smeeting:
            if e <= today: continue
            elif b > today: days -= e - b + 1
            else: days -= e - today
            today = e
        return days

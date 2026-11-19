class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idx = {s: i for i, s in enumerate(list1)}
        min_sum = float('inf')
        res = []
        
        for j, s in enumerate(list2):
            if s in idx:
                total = idx[s] + j
                if total < min_sum:
                    min_sum = total
                    res = [s]
                elif total == min_sum:
                    res.append(s)
                    
        return res
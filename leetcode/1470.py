class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x,y = nums[:n],nums[n:]
        res = []
        while x or y:
            res.append(x.pop(0))
            res.append(y.pop(0))
        return res
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c = 0
        for x in hours:
            if x >= target:
                c += 1
        return c
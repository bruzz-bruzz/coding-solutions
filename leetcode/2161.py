class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        a,b = [],[]
        for x in nums:
            if x < pivot:
                a.append(x)class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        a,b,c = [],[],[]
        for x in nums:
            if x < pivot:
                a.append(x)
            elif x > pivot:
                b.append(x)
            else:
                c.append(x)
        return a + c + b
            elif x > pivot:
                b.append(x)
        return a + [pivot] + b
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:"X",
            40:"XL",
            50:"L",
            90:"XC",
            100:"C",
            400:"CD",
            500:"D",
            900:"CM",
            1000:"M"
        }
        res = ''
        num = list(str(num))
        p = 1
        while num:
            pop = int(num.pop()) * p
            if pop in d.keys():
                res = d[pop] + res
            else:
                low,high = p, p * 10
                fin = ''
                mid = high // 2
                if pop > mid:
                    fin = d[mid]
                    pop -= mid
                while pop > 0:
                    res = d[low] + res
                    pop -= low
                if fin:
                    res = fin + res
            p *= 10
        return res
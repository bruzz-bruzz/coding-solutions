class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        for x in range(len(date)):
            date[x] = bin(int(date[x]))[2:]
        return '-'.join(date)
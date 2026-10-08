class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for x in range(len(image)):
            image[x] = [x for x in reversed(image[x])]
            for y in range(len(image[x])):
                if image[x][y] == 0:
                    image[x][y] = 1
                else:
                    image[x][y] = 0
        return image
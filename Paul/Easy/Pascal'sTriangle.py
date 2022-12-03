class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1]]
        for rowPos in range(numRows-1):
            tmp = [0] + tri[-1] + [0]
            row = list()
            for i in range(len(tri[-1])+1):
                row += [tmp[i] + tmp[i+1]]
            tri+= [row]
        return tri
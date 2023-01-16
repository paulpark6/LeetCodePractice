class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        if numRows == 1:
            return triangle
        for r in range(numRows-1):
            row = r + 1
            f_row = [0] + triangle[r] + [0]
            a_row = list()
            f_len = len(f_row)
            for i in range(f_len-1):
                a_row.append(f_row[i] + f_row[i+1])
            triangle.append(a_row)
        return triangle

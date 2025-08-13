class Solution:
    def spiralMatrix(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        print(f"matrix dimension: {m, n}")

        srow, scol = 0, 0
        erow, ecol = m - 1, n - 1
        result = []

        while srow <= erow and scol <= ecol:
            # Top row
            for i in range(scol, ecol + 1):
                result.append(matrix[srow][i])
                print(result)

            # Right column
            for i in range(srow + 1, erow + 1):
                result.append(matrix[i][ecol])
                print(result)

            # Bottom row
            if srow < erow:
                for i in range(ecol - 1, scol - 1, -1):
                    result.append(matrix[erow][i])
                    print(result)

            # Left column
            if scol < ecol:
                for i in range(erow - 1, srow, -1):
                    result.append(matrix[i][scol])
                    print(result)

            srow += 1
            erow -= 1
            scol += 1
            ecol -= 1

        return result


# test
sol = Solution()
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

print(sol.spiralMatrix(matrix))

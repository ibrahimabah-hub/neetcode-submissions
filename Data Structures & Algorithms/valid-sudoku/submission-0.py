class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        column = {}
        box = {}
        for i in range(len(board)):
            row[i] = set()
            column[i] = set()
            box[i] = set()

        box_num = 0
        for y in range(len(board)):
            if y == 3 or y == 6:
                box_num +=3
                print(["_"]*11)
            row_vals = []
            for x in range(len(board[y])):
                if x == 3 or x == 6:
                    box_num+=1
                    row_vals.append("|")
                val = board[y][x]
                row_vals.append(val)
                if val == ".":
                    continue
                if val not in row[y]:
                    row[y].add(val)
                else:
                    print(f"{val} duplicate found in row {y}")
                    return False
                if val not in column[x]:
                    column[x].add(val)
                else:
                    print(f"{val} duplicate found in column {x}")
                    return False
                if val not in box[box_num]:
                    box[box_num].add(val)
                else:
                    print(f"{val} duplicate found in box {box_num}")
                    return False
            print(row_vals)
            box_num-=2
        return True
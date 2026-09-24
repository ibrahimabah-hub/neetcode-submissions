class Solution:
    def exist(self, board: List[List[str]], words: str) -> bool:
        
        
        def dfs(y, x, word, seen):
            if not word:
                #print(seen)
                return True
            else:
                status = False
            
            if y>0:
                if [y-1,x] not in seen and board[y-1][x]==word[0]:
                    #print(word)
                    seen.append([y-1,x])
                    #print(seen)
                    status = dfs(y-1, x, word[1:], seen) or status
                    seen.remove([y-1,x])
            if y<len(board)-1:
                if [y+1,x] not in seen and board[y+1][x]==word[0]:
                    #print(word)
                    seen.append([y+1,x])
                    #print(seen)
                    status = status or dfs(y+1, x, word[1:], seen)
                    seen.remove([y+1,x])
            if x>0:
                if [y,x-1] not in seen and board[y][x-1]==word[0]:
                    #print(word)
                    seen.append([y,x-1])
                    #print(seen)
                    status = status or dfs(y, x-1, word[1:], seen)
                    seen.remove([y,x-1])
            if x<len(board[0])-1:
                if [y,x+1] not in seen and board[y][x+1]==word[0]:
                    #print(word)
                    seen.append([y,x+1])
                    #print(seen)
                    status = status or dfs(y, x+1, word[1:], seen)
                    seen.remove([y,x+1])

            return status





        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x]== words[0]:
                    
                    if dfs(y, x, words[1:], [[y,x]]):
                        return True
    
        return False

        

        
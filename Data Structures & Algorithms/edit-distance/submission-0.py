class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cashe = [[float("inf")]*(len(word2) + 1)for i in range(len(word1)+1)]

        for j in range(len(word2)+1):
            cashe[len(word1)][j] = len(word2) - j
        for i in range(len(word1)+1):
            cashe[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    cashe[i][j] = cashe[i+1][j+1]
                else:
                    cashe[i][j] = 1 + min(cashe[i+1][j],cashe[i][j+1],cashe[i+1][j+1])
        return cashe[0][0]
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = []
        colors_freq = {}
        balls = {}
        counter = 0
        
        for i,j in queries:
            if j not in colors_freq:
                colors_freq[j] = 1
                counter += 1
            else:
                colors_freq[j] += 1
                if colors_freq[j] == 1:
                    counter += 1
            
            if i in balls:
                colors_freq[balls[i]] -= 1
                if colors_freq[balls[i]] == 0:
                    counter -= 1
            
            res.append(counter)
            balls[i] = j

        return res
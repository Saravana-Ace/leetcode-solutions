class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def convert_and_check(num):
            check = []
            while num != 0:
                rem = num%k
                num = num//k
                check.append(rem)
            return check == check[::-1]
        
        l = 1
        res = []

        while len(res) < n:
            r = l * 10
            for j in [1,0]:
                for i in range(l, r):
                    if len(res) == n: break
                    
                    copy = str(i)
                    p = copy[:-1] + copy[::-1] if j == 1 else copy + copy[::-1]

                    if convert_and_check(int(p)):
                        res.append(int(p))
            
            l = r
        return sum(res)
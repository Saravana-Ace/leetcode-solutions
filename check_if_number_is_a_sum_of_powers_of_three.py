#solution 1 - greedy/brute force
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers = {i:3**i for i in range(15)}

        def get_index(n):
            for j in powers.keys():
                if n == 1:
                    print(j)
                if n < powers[j]:
                    return j-1
            return j

        j = get_index(n)
        check = set()
        
        while n > 0 and j >= 0:
            if powers[j] in check:
                return False
            n -= powers[j]
            check.add(powers[j])
            j = get_index(n)

        if not n: return True
        return False
    
# solution 2 - math, if remainder is 2 then you can't have a distinct sum
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n!=0:
            rem = n%3
            if rem==2:
                return False
            n = n//3
        return True
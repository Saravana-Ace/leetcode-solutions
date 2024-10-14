class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq_arr = [0 for i in range(k)]

        for n in arr:
            rem = n%k
            comp = k-rem if k-rem != k else 0
            if freq_arr[comp]:
                freq_arr[comp] -= 1
            else:
                freq_arr[rem] += 1

        return sum(freq_arr) == 0
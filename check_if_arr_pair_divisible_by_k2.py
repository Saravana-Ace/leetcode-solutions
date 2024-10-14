# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         freq_arr = [0 for i in range(k)]

#         for n in arr:
#             rem = n%k
#             comp = k-rem if k-rem != k else 0
#             if freq_arr[comp]:
#                 freq_arr[comp] -= 1
#             else:
#                 freq_arr[rem] += 1

#         return sum(freq_arr) == 0

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq_arr = [0 for i in range(k)]

        for n in arr:
            freq_arr[n%k] += 1
        
        if freq_arr[0] % 2 == 1: return 0

        for n in range(1, (k//2)+1):
            if freq_arr[n%k] != freq_arr[k-(n%k)]: return 0
        
        return 1
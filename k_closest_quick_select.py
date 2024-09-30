class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = [(sqrt(point[0]**2 + point[1]**2), point) for point in points]

        def quickselect(left, right, dist, k):
            pivot_pt = partition(dist, left, right)

            if pivot_pt == k - 1:
                return [dist[i][1] for i in range(k)]
            elif pivot_pt > k - 1:
                return quickselect(left, pivot_pt - 1, dist, k)
            else:
                return quickselect(pivot_pt + 1, right, dist, k)

        def partition(arr, left, right):
            pivot_value = arr[right]
            i = left
            
            for j in range(left, right):
                if arr[j][0] < pivot_value[0]:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            
            arr[i], arr[right] = arr[right], arr[i]
            return i

        return quickselect(0, len(dist) - 1, dist, k)
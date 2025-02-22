# solution 1: iterative approach, parse numbers and dash count first
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        numbers = list(map(int, re.findall(r'\d+', traversal)))
        dash_num = [0]
        last_known_dash_num = {}
        addresses = [TreeNode(n, None, None) for n in numbers]

        i = 1
        num_dashes = 0
        while i < len(traversal):
            if traversal[i].isdigit():
                dash_num.append(num_dashes)
                while i < len(traversal) and traversal[i].isdigit():
                    i += 1
                num_dashes = 0
            else:
                num_dashes += 1
                i += 1
            
        
        for i in range(1, len(numbers)):
            if dash_num[i] > dash_num[i-1]:
                last_known_dash_num[dash_num[i]] = i

                if addresses[i-1].left == None:
                    addresses[i-1].left = addresses[i]
                else:
                    addresses[i-1].right = addresses[i]
            else:
                parent = addresses[last_known_dash_num[dash_num[i]] - 1]
                parent.right = addresses[i]
                last_known_dash_num[dash_num[i]] = i
                
        return addresses[0]
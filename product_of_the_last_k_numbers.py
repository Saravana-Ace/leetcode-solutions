class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.cum_product = []
        self.latest_zero_index = -1

    def add(self, num: int) -> None:
        if num == 0:
            self.latest_zero_index = len(self.nums)
        
        self.nums.append(num)
            
        if self.cum_product:
            temp = self.cum_product[-1]*num
            if temp != 0:
                self.cum_product.append(temp)
            else:
                self.cum_product.append(num)
        else:
            self.cum_product.append(num)

    def getProduct(self, k: int) -> int:

        if len(self.cum_product) > 1:
            i = len(self.cum_product)-k-1

            if self.latest_zero_index > i: return 0

            temp = self.cum_product[i]

            if temp == 0 or i < 0:
                temp = 1

            return self.cum_product[-1]//temp
        else:
            return self.cum_product[0]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
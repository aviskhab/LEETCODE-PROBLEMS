
class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset prefix products after zero
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix)

        # If k numbers cross a zero, product is 0
        if k >= n:
            return 0

        return self.prefix[-1] // self.prefix[-k-1]

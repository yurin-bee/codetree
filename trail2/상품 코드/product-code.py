product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class products:
    def __init__(self, n="codetree", c=50):
        self.n = n
        self.c = c
        print(f"product {self.c} is {self.n}")

p1 = products()
p2 = products(product_name, product_code)

# 파이썬 구조체 예시
from dataclasses import dataclass

class Product_Struct:
    name: str = None
    weight: int = None
    price: int = None

product = Product_Struct()
product.name = input("Input product's name: >>")
product.weight = int(input("Input product's weight: >>"))
product.price = product.weight * 3

print("$3 per gram")
print(product.name,"'s price: >> $",product.price)
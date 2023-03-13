A = int(input())
B = int(input())
B2 = B
while B2 > 0:
    print(A*(B2%10))
    B2//=10

print(A*B)
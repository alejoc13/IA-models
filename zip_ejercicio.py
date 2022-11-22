
#uso de zip con comprension de listas
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]

L3 = [x1+x2 for(x1,x2) in zip(L1,L2) if x1>10 and x2<5]
print(L3)

import math

su = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

max_su = max(su)
print("max_su : ", max_su)

for i in su:
    if i*i < max_su:
        print(i)
        for j in su:
            if j > i and j % i == 0:
                print("i : ", i, " / j :", j)

                su.remove(j)
print(su)
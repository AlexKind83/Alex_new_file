
# 1 Способ
a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]

for i in range(len(a)):
    # print(a.count(a[i]))
    b = a.count(a[i])
    # print(b, end=' ')
    if b % 2 == 0:
        # print(b)
        continue
    else:
        print(a[i], end=' ')
print()


# 2 Способ
for i in a:
    b = a.count(i)
    if b % 2 == 0:
        continue
    else:
        print(i, end=' ')

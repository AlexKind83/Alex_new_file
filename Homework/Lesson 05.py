# 1 Способ
a = [int(input('-> ')) for _ in range(int(input('n = ')))]
n = 0
s = 0
for i in range(len(a)):
    if a[i] > 0:
        n += 1
        s += a[i]
    else:
        print(end='')
print("\nСреднее арифметическое: ", s / n)


# 2 Способ
a = [int(input('-> ')) for _ in range(int(input('\nn = ')))]
n = 0
s = 0
for i in a:
    if i > 0:
        n += 1
        s += i
    else:
        print(end='')
print("\nСреднее арифметическое: ", s / n)

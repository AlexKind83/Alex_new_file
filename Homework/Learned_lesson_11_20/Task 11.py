a = set(input("Введите строку: "))
count = 0

for i in a:
    set1 = set("ЁЕёеЙйИиУуЫыАаОоЭэЯяЮю")
    set2 = set("AaEeIiOoUuYy")
    b = set1 | set2
    if i in b:
        count += 1
        s = a & b
print("Количество гласных равно:", count)

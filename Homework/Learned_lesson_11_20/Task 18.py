str_ = "I am learning Python. hello, WORLD!"

str_index_1 = str_.index('h')
str_index_2 = str_.index('h', str_index_1 + 1)
str_new = str_[str_index_1: str_index_2 + 1]
str_revers = str_new[::-1]
print(str_.replace(str_new, str_revers))


# print(str_index_1)
# print(str_index_2)
# print(str_new)
# print(str_revers)

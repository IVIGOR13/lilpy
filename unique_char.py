# Finding the number of unique characters in a string
# Нахождение количества уникальных символов в строке
print([len([1 for i in arr if len([1 for j in arr if j == i]) == 1]) for arr in [list(input())]][0])

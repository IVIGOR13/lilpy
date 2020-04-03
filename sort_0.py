# Sort an array of numbers without repeating elements
# Сортировка массива чисел без повторяющихся элементов
print([[[arr[arr1.index(q)] for q in range(len(arr1))] for arr1 in [[len([1 for j in range(len(arr)) if i!=j and arr[j] < arr[i]]) for i in range(len(arr))]]]for arr in [list(map(int, input().split(' ')))]][0][0])

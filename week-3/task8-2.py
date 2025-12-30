# процедура замены элементов
def swap_first_last(arr):
    arr[0], arr[-1] = arr[-1], arr[0]


m = int(input("Введите длину массива: "))

A = []

print("Введите элементы массива:")
for i in range(m):
    A.append(int(input()))

print("Исходный массив:", A)

swap_first_last(A)

print("Новый массив:", A)


def rectangle_area(a, b):
    return a * b

def right_triangle_area(a, b):
    return 0.5 * a * b



X = float(input("Введите X: "))
Y = float(input("Введите Y: "))
Z = float(input("Введите Z: "))
T = float(input("Введите T: "))


rect = rectangle_area(X, Y)


tri = right_triangle_area(Z, T)


S = rect + tri

print("Площадь четырёхугольника =", S)

# площадь прямоугольника
def rectangle_area(a, b):
    return a * b


# площадь прямоугольного треугольника
def right_triangle_area(a, b):
    return 0.5 * a * b


# ввод данных
X = float(input("Введите X: "))
Y = float(input("Введите Y: "))
Z = float(input("Введите Z: "))
T = float(input("Введите T: "))

# часть с прямым углом
rect = rectangle_area(X, Y)

# часть в виде треугольника
tri = right_triangle_area(Z, T)

# общая площадь
S = rect + tri

print("Площадь четырёхугольника =", S)

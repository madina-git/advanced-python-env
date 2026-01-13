f = input("Фигура (круг/квадрат/прямоугольник) ")

if f == "круг":
    r = float(input("радиус: "))
    s = 3.14 * r * r
    print("площадь =", s)

elif f == "квадрат":
    a = float(input("сторона: "))
    s = a * a
    print("площадь =", s)

elif f == "прямоугольник":
    a = float(input("a: "))
    b = float(input("b: "))
    s = a * b
    print("площадь =", s)

else:
    print("нет такой фигуры")


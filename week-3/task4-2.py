# процедура (функция), которая проверяет точку
def inside_circle(x, y, a, b, R):
    if (x - a)**2 + (y - b)**2 < R**2:
        return True
    else:
        return False


# центр круга и радиус
a = float(input("Введите x центра круга: "))
b = float(input("Введите y центра круга: "))
R = float(input("Введите R: "))

# точки
p1, p2 = map(float, input("Введите координаты точки P: ").split())
f1, f2 = map(float, input("Введите координаты точки F: ").split())
l1, l2 = map(float, input("Введите координаты точки L: ").split())

count = 0

# проверяем каждую точку
if inside_circle(p1, p2, a, b, R):
    count += 1

if inside_circle(f1, f2, a, b, R):
    count += 1

if inside_circle(l1, l2, a, b, R):
    count += 1

print("Точек внутри круга:", count)

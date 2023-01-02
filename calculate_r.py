import math


def calculate_r(x, y):
    n = len(x)  # population
    x_sqrd = [d ** 2 for d in x] 
    y_sqrd = [d ** 2 for d in y]
    x_E, y_E = sum(x), sum(y)
    x_sqrd_E, y_sqrd_E = sum(x_sqrd), sum(y_sqrd)
    xy = [x1*y1 for x1, y1 in zip(x, y)]
    xy_E = sum(xy)
    r = ((n*xy_E) - (x_E*y_E)) / (math.sqrt((n * x_sqrd_E) - x_E ** 2) * math.sqrt((n * y_sqrd_E) - y_E ** 2))
    return "{:.3f}".format(r)


x = [70, 115, 105, 82, 93, 125, 88]
y = [3, 45, 21, 7, 16, 62, 12]

print(calculate_r(x, y))

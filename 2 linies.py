import matplotlib.pyplot as plt


#Метод Брезенхема
def bresenham(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy > dx
    
    if slope:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    error = dx / 2
    ystep = 1 if y1 < y2 else -1
    y = y1
    
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if slope else (x, y)
        points.append(coord)
        error -= dy
        if error < 0:
            y += ystep
            error += dx
    
    return points

# Example usage:
x1, y1 = map(int, input("Enter the coordinates of the first point: ").split())
x2, y2 = map(int, input("Enter the coordinates of the second point: ").split())

points = bresenham(x1, y1, x2, y2)
x, y = zip(*points)
plt.plot(x, y)
plt.show()

#Реализация методом ЦДА

def dda(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = dx / steps
    yinc = dy / steps
    
    x = x1
    y = y1
    
    points = []
    for i in range(steps):
        coord = (int(round(x)), int(round(y)))
        points.append(coord)
        x += xinc
        y += yinc
    
    return points

# Example usage:
x1, y1 = map(int, input("Enter the coordinates of the first point: ").split())
x2, y2 = map(int, input("Enter the coordinates of the second point: ").split())

points = dda(x1, y1, x2, y2)
x, y = zip(*points)
plt.plot(x, y)
plt.show()
import numpy as np
import cv2

# сделали изображение серым и более размытым
image = cv2.imread("C:/Users/korys/Desktop/books.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
cv2.imwrite("C:/Users/korys/Desktop/gray1.png", gray)

# контуры
edged = cv2.Canny(gray, 10, 250)
cv2.imwrite("C:/Users/korys/Desktop/edged1.png", edged)

# закрытие контуров
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
cv2.imwrite("C:/Users/korys/Desktop/closed1.png", closed)

# ищем контуры
cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[0]
total = 0

# цикл по контурам, сглаживаем, считаем вершины
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    if len(approx) == 8:
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
        total += 1

print("Я нашёл {0} магнитов на этой картинке".format(total))
cv2.imwrite("C:/Users/korys/Desktop/result1.png", image)
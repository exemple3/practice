import cv2
import numpy as np

image = cv2.imread("test2.jpg")
cv2.imshow("original", image)
cv2.waitKey(0)
# загрузка и отображение изображения

blurred_image = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("blurred", blurred_image)
cv2.waitKey(0)
# размытие изображения (чтобы убрать шумы)

hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", hsv_image)
cv2.waitKey(0)
# преобразование в hsv (лучше подходит для цвета)

hsv_min = np.array((90, 50, 50), np.uint8)
hsv_max = np.array((130, 255, 255), np.uint8)
# задание цветовых рамок для синего цвета

blue_mask = cv2.inRange(hsv_image, hsv_min, hsv_max)
cv2.imshow("blue_mask", blue_mask)
cv2.waitKey(0)
# создание черно-белой маски

contours, hierarchy = cv2.findContours(blue_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
# поиск контуров и сортировка по площади (по убыв.)

for i, contour in enumerate(sorted_contours):
    # выбор контура
    if cv2.contourArea(contour) > 100:
        # проверка площади контура
        x, y, w, h = cv2.boundingRect(contour)
        # поиск прямоуг. с контуром
        print(f"{x}, {y}, {w}, {h}")
        center_x = int(x + w/2)
        center_y = int(y + h/2)
        cv2.circle(image, (center_x, center_y), 10, (0, 0, 255), -1)
        # поиск центра
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # точка в центре



cv2.imshow('result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


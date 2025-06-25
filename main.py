import cv2
import numpy as np

# We indicate the full path to the file (image) we are working with or
# the name of the file (image) if the file is saved in the project folder
image = cv2.imread("test2.jpg")

# Create a window. Output image. Signing the window Читает изображение
cv2.imshow("original", image)

# Wait for the button to be pressed to move to the next command
cv2.waitKey(0)

# Open CV  library can do various things with the image

# Open CV adds blur to the image to suppress noise
blurred_image = cv2.GaussianBlur(image, (11, 11), 0)

# Create a window. Output image. Signing the window
cv2.imshow("blurred", blurred_image)

# Wait for the button to be pressed to move to the next command
cv2.waitKey(0)

# Changing the color palette (RGB convet HSV)
hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

# Create a window. Output image. Signing the window Компьютер лучше читает
cv2.imshow("hsv", hsv_image)

# Wait for the button to be pressed to move to the next command
cv2.waitKey(0)

#границы для зеленого цвета
hsv_min = np.array((36, 25, 25), np.uint8)  # Bottom border of green color
hsv_max = np.array((70, 255, 255), np.uint8)  # Green upper border

# накладываем границы на изображение
green_mask = cv2.inRange(hsv_image, hsv_min, hsv_max)

# Create a window. Output image. Signing the window
cv2.imshow("mask", green_mask)

# Wait for the button to be pressed to move to the next command
cv2.waitKey(0)

#  вернет 2 массива
contours, hierarchy = cv2.findContours(green_mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Sort all found contours in descending order
sorted_contur = sorted(contours, key=cv2.contourArea, reverse=True)

#Determine the coordinates of the contour (upper left corner) and its dimensions
x, y, w, h, = cv2.boundingRect(sorted_contur[0])

print(x, y, w, h)

# Draw a point using coordinates
cv2.circle(image,(x,y),8,(255,0,0),-1)

# Draw a point in the center of the object inscribed in the square
cv2.circle(image,(int (x+w/2),int (y+h/2)),8, (255,0,0), 3)
cv2.drawContours(image, sorted_contur, -1, (255, 0, 0), 2, cv2.LINE_AA, hierarchy, 1)

#determine the coordinates of the second contour
x, y, w, h, = cv2.boundingRect(sorted_contur[1])
print(x, y, w, h)

#draw the second outline into a square
cv2.rectangle(image, (x,y), (int(x+w), int(y+h)),(0,0,255),3)





# Create a window. Output image. Signing the window
cv2.imshow('contours', image)
# Wait for the button to be pressed to move to the next command
cv2.waitKey(0)


import cv2 as cv
import numpy as np

'''
file_path = input("Enter image or video path: \n")
photo = cv.imread(f"{file_path}")

def resize(file, scale):
    width = int(file.shape[1] * scale)
    height = int(file.shape[0] * scale)
    dimensions = (width, height)
    return (
'''
photo = cv.imread("C:/Users/dizam/OneDrive/Pictures/IMG_4724.jpg", cv.IMREAD_GRAYSCALE)
'''

width = int(photo.shape[1] * scale)
height = int(photo.shape[0] * scale)
'''

scale = 0.25
photo_rescale = cv.resize(photo, None, fx=scale, fy=scale, interpolation=cv.INTER_AREA)

# Apply Sobel operator
sobel_x = cv.Sobel(photo_rescale, cv.CV_64F, 1, 0, ksize=3)  # Horizontal edges
sobel_y = cv.Sobel(photo_rescale, cv.CV_64F, 0, 1, ksize=3)  # Vertical edges

# Compute gradient magnitude
gradient_magnitude = cv.magnitude(sobel_x, sobel_y)

# Convert to uint8
gradient_magnitude = cv.convertScaleAbs(gradient_magnitude)


# Display result
# cv.imshow("Sobel Edge Detection", gradient_magnitude)

#cv.imshow("Photo", photo)
#cv.imshow("Resized Photo", photo_rescale)

invert_sobel = cv.bitwise_not(gradient_magnitude)
#cv.imshow("Inverted Sobel", invert_sobel)

# Canny

blur = cv.GaussianBlur(photo_rescale, (7, 7), 0)
#cv.imshow("Blurred Sobel", blur)

canny = cv.Canny(blur, 85, 125)

# Dilation
kernel_dilation = np.ones((1,2), np.uint8)
dilate = cv.dilate(canny, kernel_dilation, iterations=3)

invert_canny = cv.bitwise_not(canny)
cv.imshow("Canny Edges", invert_canny)

invert_dilate = cv.bitwise_not(dilate)
cv.imshow("Canny Dilated", invert_dilate)

cv.imwrite("profile-photo1.jpg", invert_dilate)

cv.waitKey(0)
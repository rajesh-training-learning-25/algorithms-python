# import necessary libraries
import cv2
import numpy as np

# read the image using opencv
imgInput = cv2.imread("./image_data/lena.jpg")

# set the width and height of the output image in px
# width, height = 718, 718

height = imgInput.shape[0]
width = imgInput.shape[1]

# set the initial coordinates of the four points
pts1 = np.float32([[0, height], [width, height], [width, 0], [0, 0]])

# set the final coordinates of the four points
pts2 = np.float32([[142, 142], [362, 32], [418, 358], [127, 461]])

# get the projective transformation matrix
trnsMatrix = cv2.getPerspectiveTransform(pts1, pts2)


# apply the projective transformation
imgOutput = cv2.warpPerspective(imgInput, trnsMatrix, (width, height))

# display the original and the final image
cv2.imshow("Original Image", imgInput)
cv2.imshow("Final Image", imgOutput)

# end the program on pressing some key
cv2.waitKey(0)
cv2.destroyAllWindows()

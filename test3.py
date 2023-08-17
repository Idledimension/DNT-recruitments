import cv2
import numpy as np

def trace_image_with_edge_detection(image):

  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  edges = cv2.Canny(image_gray, 100, 200)

  binary_image = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)[1]

  return binary_image

if __name__ == "__main__":
  image = cv2.imread("thugduck.jpeg.jpg")

  binary_image = trace_image_with_edge_detection(image)

  cv2.imshow("Image", binary_image)
  cv2.imwrite("outline.jpg", binary_image)
  cv2.waitKey(0)
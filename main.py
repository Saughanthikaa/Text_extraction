import cv2
from tamilnadu import tamil_data


path = r'C:\Users\priya\PycharmProjects\project_1\image\tamilnadu.jpeg'
image = cv2.imread(path, 0)
thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


tamil_data(image)

import pytesseract
import cv2


def tamil_data(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    x, y, w, h = 100, 550, 300, 58
    ROI = thresh[y:y + h, x:x + w]
    data = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print(data)

    cv2.imshow('thresh', thresh)
    cv2.imshow('ROI', ROI)
    cv2.waitKey()

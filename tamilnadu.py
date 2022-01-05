import pytesseract
import cv2


def tamil_data(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'
    thresh = 255 - cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    x, y, w, h = 100, 550, 300, 58
    ROI = thresh[y:y + h, x:x + w]
    data = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("NAME :",data)

    x, y, w, h = 1000, 1100, 120, 58
    ROI = thresh[y:y + h, x:x + w]
    tamil = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("TAMIL :",tamil)

    x, y, w, h = 1030, 1145, 98, 50
    ROI = thresh[y:y + h, x:x + w]
    English = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("ENGLISH :",English)

    x, y, w, h = 1030, 1180, 98, 58
    ROI = thresh[y:y + h, x:x + w]
    Physics = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("PHYSICS :",Physics)

    x, y, w, h = 1030, 1220, 98, 58
    ROI = thresh[y:y + h, x:x + w]
    chemistry = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("CHEMISTRY :",chemistry)

    x, y, w, h = 1030, 1257, 98, 58
    ROI = thresh[y:y + h, x:x + w]
    cs = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("COMPUTER SCIENCE :",cs)

    x, y, w, h = 1035, 1310, 93, 48
    ROI = thresh[y:y + h, x:x + w]
    maths = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("MATHEMATICS :",maths)

    x, y, w, h = 700, 1350, 108, 50
    ROI = thresh[y:y + h, x:x + w]
    total = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("TOTAL :", total)

    x, y, w, h = 1200, 1580, 200, 55
    ROI = thresh[y:y + h, x:x + w]
    moi = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("MEDIUM OF INSTRUCTION :",moi)

    x, y, w, h = 550, 1580, 300, 55
    ROI = thresh[y:y + h, x:x + w]
    regno = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6')
    print("REGISTER NUMBER :",regno)

    cv2.imshow('thresh', thresh)
    cv2.imshow('ROI', ROI)
    cv2.waitKey()

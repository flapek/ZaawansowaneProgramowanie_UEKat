import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Users\\filap\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
)


def read_image(path: str):
    return cv2.imread(path)


def prepare_image(path: str):
    img = cv2.cvtColor(read_image(path), cv2.COLOR_BGR2GRAY)
    return cv2.adaptiveThreshold(
        cv2.bilateralFilter(img, 9, 75, 75),
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        2,
    )


def read_text_from_image(path: str) -> str:
    return pytesseract.image_to_string(
        prepare_image(path),
    )


def show_texts(paths):
    [
        print("-------------------------------\n" + read_text_from_image(path))
        for path in paths
    ]


show_texts(
    [
        r"data\\sample1.png",
        r"data\\sample2.png",
        r"data\\sample3.png",
        r"data\\sample4.png",
        r"data\\sample5.png",
    ]
)

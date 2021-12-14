import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\\Users\\filap\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
)


def read_text_from_image(path: str) -> str:
    img_cv = cv2.imread(path)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


def show_texts(paths):
    [
        print(
            "-------------------------------\n" + read_text_from_image(path)
        )
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

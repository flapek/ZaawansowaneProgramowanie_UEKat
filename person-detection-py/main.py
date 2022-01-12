import cv2
from const import HOGCV
from argsParser import argsParser
from humanDetector import humanDetector


if __name__ == "__main__":
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    args = argsParser()
    humanDetector(args)

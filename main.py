from argsParser import argsParser
from Detector import *

if __name__ == "__main__":
    args = argsParser()
    Detector(args).run()

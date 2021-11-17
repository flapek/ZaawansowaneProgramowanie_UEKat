from io import TextIOWrapper

PATH = "C:\\Users\\filap\\Documents\\GitHub\\ZaawansowaneProgramowanie_UEKat\\data\\"


def read_file(filename: str) -> TextIOWrapper:
    file = open(f"{PATH}{filename}", "r", encoding="UTF8", newline="\n")
    return file

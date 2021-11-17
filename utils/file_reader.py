from io import TextIOWrapper
from pathlib import Path
import os.path


def read_file(filename: str) -> TextIOWrapper:
    path = Path(__file__).parent.parent
    print(path)
    file = open(
        os.path.join(path, "data", filename),
        "r",
        encoding="UTF8",
        newline="\n",
    )
    return file

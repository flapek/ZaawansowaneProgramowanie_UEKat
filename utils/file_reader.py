from io import TextIOWrapper
from pathlib import Path
import os.path


def read_file(filename: str) -> TextIOWrapper:
    return open(
        os.path.join(Path(__file__).parent.parent, "data", filename),
        "r",
        encoding="UTF8",
        newline="\n",
    )

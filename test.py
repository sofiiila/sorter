import logging
import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join(Path(__file__).resolve().parent, "sorters"))
sys.path.append(os.path.join(Path(__file__).resolve().parent, "tests"))


def log():
    pass


DOUBLE_DASH_ARGS = {"log": log}

if __name__ == "__main__":
    raw_args = sys.argv
    args = []

    if "--log" not in raw_args:
        logging.disable()

    for arg in raw_args:
        if arg.startswith("--"):
            func = DOUBLE_DASH_ARGS.get(arg.replace("--", ""))

            if func is not None:
                func()
        else:
            args.append(arg)

    if len(args) == 1:
        pytest.main(["-s", "-v", "--ignore=db"])
    elif len(args) == 2:
        if args[1].startswith("-"):
            marker = f'not {args[1].replace("-", "")}'
        else:
            marker = args[1]
        pytest.main(["-s", "-v", "-k", marker, "--ignore=db"])
    else:
        raise pytest.UsageError("Некорректное количество аргументов")

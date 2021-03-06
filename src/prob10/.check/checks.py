import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'tools'))
from mylibs import chk_template
from random import randint

__author__ = "Jung-Lin Yang"
__copyright__ = "Copyright (C) 2022, STUST EECS"
__version__ = "0.1"


def index(dat):
    s = ""
    for i in range(10):
        if i in dat:
            s += f"{dat.index(i)} "
        else:
            s += "-1 "
    return s

def expected():
    dat = [randint(1, 15) for _ in range(randint(10,20))]
    idat = " ".join([str(_) for _ in dat])
    print(f"Test Data : {idat}")
    return idat, index(dat) 


chk_template.expected = expected

if __name__ == "__main__":
    # print(f"cur = {sys.argv[0]}")
    root = sys.argv[0].replace(".check\checks.py", "")
    root = root.replace(".check/checks.py", "")
    loops = 10
    if len(sys.argv) == 2:
        loops = int(sys.argv[1])
    chk_template.main(root, 0, loops)

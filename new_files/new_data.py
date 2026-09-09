#fmt: off

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # to get the data from a root folder to sub folder we have to write this

from employees import employees_data

for item in employees_data:
    print(item)


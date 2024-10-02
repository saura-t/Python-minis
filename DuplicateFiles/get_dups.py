import os
import random
import string
import numpy as np
from pathlib import Path
from PIL import Image
from hashlib import md5
from collections import defaultdict

loc = str(input("Enter directory path:"))
input_dir = os.path.normpath(loc)

files = list(Path(input_dir).rglob("*.*"))

with open(files[0], "rb") as original:
    original_md5 = md5(original.read()).hexdigest()

hashmap = defaultdict(list)
for file in files:
    with open(file, "rb") as original:
        key_md5 = md5(original.read()).hexdigest()
    hashmap[key_md5].append(file)

for key in hashmap:
    if len(hashmap[key]) > 1:
        print(f"Copies for file: {key} are {len(hashmap[key])} at: ")
        for val in hashmap[key]:
            print(f"{val}, ")
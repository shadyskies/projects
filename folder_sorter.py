#!/usr/bin/env python3

import os
import sys
from shutil import copy


PATH = "../../../../../Downloads"
folders = ["Docs","Torrents","Songs","Pictures","ISO's","Packages","Misc"]

print(os.listdir(PATH))
files = [i for i in os.listdir(PATH) if not os.path.isdir(i)]
files_extensions = [i.split(".")[-1] for i in os.listdir(PATH) if not os.path.isdir(i)]

print(files)
print(files_extensions)
#!/usr/bin/env python

import os

for f in os.listdir("repos"):
    os.system("cd repos/" + f + "; git pull")

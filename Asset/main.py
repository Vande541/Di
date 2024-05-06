import os

DIR = os.getcwd()
for f in os.listdir(DIR):
    if f.endswith("jpg") or f.endswith("png"):
        os.remove(f)
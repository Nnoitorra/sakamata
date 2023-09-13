import lib
import os


work_dir = r''


for root, dirs, files in os.walk(work_dir):
    for names in files:
        yt_id = lib.get_id(names)
        with open("ids.txt", "a") as f:
            f.write(yt_id)
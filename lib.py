import re
import shutil
import os


def get_id(name):
    re_id = re.compile(r"((?<=\()[^\"&?\/\s]{11}(?=\)))")
    ytid = re_id.search(name)
    return ytid


def exit():
    exit_in = input("Press Enter to exit...")
    if exit_in == "":
        quit()


def move_file(work_dir, dest_dir):
    all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    src_folder = os.path.join(work_dir, latest_subdir)
    dest_folder = os.path.join(dest_dir, latest_subdir)
    try:
        shutil.move(src_folder, dest_dir)
    except:
        shutil.copytree(src_folder, dest_folder, dirs_exist_ok=True)
        shutil.rmtree(src_folder)


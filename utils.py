import sys
import os
import pyperclip
import subprocess

work_dir = r''
dest_dir = r''

def dlp():
    link = pyperclip.paste()
    os.chdir(work_dir)
    subprocess.run([sys.executable, '-m', 'yt_dlp', link])
    try:
        lib.move_file(work_dir, dest_dir)
    except ValueError:
        lib.exit()

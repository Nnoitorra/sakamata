import pyperclip
import subprocess
import os
import sys
import lib


work_dir = r'F:\Downloads\yt-dlp'
dest_dir = r'D:\Downloads\yt-dlp'


def main():
    link = pyperclip.paste()
    os.chdir(work_dir)
    subprocess.run([sys.executable, '-m', 'yt_dlp', link])
    try:
        lib.move_file(work_dir, dest_dir)
    except ValueError:
        lib.exit()


main()
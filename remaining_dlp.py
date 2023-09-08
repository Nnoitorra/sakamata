import subprocess
import sys
import os
import lib


work_dir = r''
dest_dir = r''


def main():
    with open('remaining.txt') as f:
        lines = f.readlines()
        os.chdir(work_dir)
        for line in lines:
            subprocess.run([sys.executable, '-m', 'yt_dlp', line])
            try:
                lib.move_file(work_dir, dest_dir)
            except ValueError:
                continue
    lib.exit()


main()

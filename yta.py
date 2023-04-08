import pyperclip
import subprocess
import os
import lib


work_dir = r'F:\Downloads\ytarchive'
dest_dir = r'D:\Downloads\ytarchive'
yta_args = [
    '--vp9',
    '--thumbnail',
    '--add-metadata',
    '--threads',
    '4',
    '-c',
    'cookies.txt',
    '--output',
    '%(channel)s/%(release_date,upload_date)s - %(title)s(%(id)s)',
    '-r',
    '15'
]


def main():
    link = pyperclip.paste()
    os.chdir(work_dir)
    subprocess.run(['ytarchive', *yta_args, link, 'best'])
    try:
        lib.move_file(work_dir, dest_dir)
    except ValueError:
        lib.exit()


main()
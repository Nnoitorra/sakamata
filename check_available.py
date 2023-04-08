import os
import subprocess
import sys
import json
import lib


yt_dlp_args = [
    '--ignore-config',
    '--skip-download',
    '-j'
]

root_dir = r'\\LucasNAS\Archives\ytarchive\videos'
file_list = []


def main():
    for root, dirs, files in os.walk(root_dir):
        for names in files:
            file_name = os.path.join(root, names)
            yt_id = lib.get_id(names)
            try:
                check = subprocess.check_output([sys.executable, '-m', 'yt_dlp', *yt_dlp_args, yt_id.group()])
            except subprocess.CalledProcessError as err:
                print(f"{names} https://www.youtube.com/watch?v={yt_id.group()} is not available.")
                continue
            result = json.loads(check)
            if "live_chat" not in result["subtitles"]:
                print(f'{names} https://www.youtube.com/watch?v={yt_id.group()} has been edited.')
                continue
            else:
                print(f'{names} seems to be unedited')
                file_list.append(file_name)
                continue
    if len(file_list) != 0:
        delete_all = input("Do you want to delete the unedited videos (y/N)? ").lower()
        if delete_all == "y":
            for videos in file_list:
                os.remove(videos)
    else:
        lib.exit()


main()
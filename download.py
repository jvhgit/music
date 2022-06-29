# imports
from pytube import YouTube
import os
import subprocess
print("Enter the destination (leave blank for current directory)")
bestand_locatie = str(input())

print("Enter file threshold (leave blank for 1mb)")
thres = str(input())
thres = int(thres) if len(thres) > 0 else 1

while True:
    # url input from user
    url = str(input("Enter the URL of the video you want to download: \nAvailable: YouTube urls (single tracks) and SoundCloud urls (single tracks and playlists) \n\t>> "))
    if "soundcloud" in url:
        try:
            subprocess.run(["scdl", "-l",  url, "--path", bestand_locatie])
        except Exception as e:
            print(e)
            continue
    elif "youtube" in url:
        try:
            yt = YouTube(url)

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()
            # download the file
            out_file = video.download(output_path=bestand_locatie)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            # print(new_file)
            os.rename(out_file, new_file)

            file_size = os.path.getsize(new_file) / 1000000
            if file_size < thres:
                print(f"Threshold is not met -> file deleted. Try another version.")
                os.remove(bestand_locatie + new_file)
            # result of success
            print(yt.title + " has been successfully downloaded from Youtube.")
        except FileExistsError:
            print("File already exist -> skipped.")
            continue

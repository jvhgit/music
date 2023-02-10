from sclib import SoundcloudAPI, Track, Playlist
import sys
from pytube import YouTube
import os
from sclib.sync import UnsupportedFormatError
import re
music_type = {
    "DRUMBASS" : "C:\\Users\\jhaal\\Music\\Feestje\\drumbass\\",
    "TECHNO" : "C:\\Users\\jhaal\\Music\\Feestje\\techno\\",
    "REST" : "C:\\Users\\jhaal\\Music\\Feestje\\rest\\",
    "REQUEST" : "C:\\Users\\jhaal\\Music\\Feestje\\request\\"
}

print("Enter DRUMBASS/TECHNO/REST/REQUEST")
FOLDER = str(input())
bestand_locatie = music_type[FOLDER]
print(bestand_locatie)


print("Enter file threshold (leave blank for 1mb)")
thres = str(input())
thres = int(thres) if len(thres) > 0 else 1

while True:
    # url input from user
    url = str(input("Enter the URL of the video you want to download: \n>> "))
    print(f"This is the {FOLDER} prompt!")

    if "soundcloud" in url:
        if "playlist+:" in url:
            try:
                api = SoundcloudAPI()
                playlist_url = url.split('+:')[-1]
                playlist = api.resolve(playlist_url)
                print(playlist)
                assert type(playlist) is Playlist
                num = len(playlist.tracks)
                i = 0
                for track in playlist.tracks:
                    i += 1
                    print(f"Track {i} / {num}")
                    try:
                        filename = f'./{track.artist} - {track.title}.mp3'
                        with open(bestand_locatie + filename, 'wb+') as fp:
                            track.write_mp3_to(fp)
                        print(f"\t{filename} downloaded.")
                        print(f"This is the {FOLDER} prompt!")
                    except (UnsupportedFormatError, FileNotFoundError, OSError) as e:
                        print(f"\t{filename} -> This file is not supported.")
                        continue

            except UnsupportedFormatError:
                continue
        else:
            api = SoundcloudAPI()

            track = api.resolve(url)

            assert type(track) is Track

            filename = f'{track.artist} - {track.title}.mp3'

            with open(bestand_locatie + filename, 'wb+') as fp:
                track.write_mp3_to(fp)
            
            file_size = os.path.getsize(bestand_locatie + filename) / 1000000

            if file_size < thres:
                print(f"Threshold is not met -> file deleted. Try another version.")
                os.remove(bestand_locatie + filename)
            else:
                print(filename + "  has been successfully downloaded from Soundcloud.")

    elif "youtube" in url:
        try:
            yt = YouTube(url)

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            # download the file
            out_file = video.download(output_path=bestand_locatie)
            print(sys.getsizeof(yt))
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            file_size = os.path.getsize(new_file) / 1000000
            if file_size < thres:
                print(f"Threshold is not met -> file deleted. Try another version.")
                os.remove(new_file)
            # result of success
            print(yt.title + " has been successfully downloaded from Youtube.")
            # print("Something went wrong - try again.")
        except FileExistsError:
            print("File already exist -> skipped.")
            continue
from sclib import SoundcloudAPI, Track, Playlist
import sys
from pytube import YouTube
import os

music_type = {
  "drumbass" : "/mnt/h/Mijn Drive/Muziek/drumbass",
  "techno" : "/mnt/h/Mijn Drive/Muziek/techno",
  "rest" : "/mnt/h/Mijn Drive/Muziek/rest",
  "request" : "/mnt/h/Mijn Drive/Muziek/request"
}

FOLDER = str(sys.argv[1])
bestand_locatie = music_type[FOLDER]
thres = 1

url = sys.argv[2]

if "soundcloud" in url:
  if "playlist+:" in url:
    api = SoundcloudAPI()
    playlist_url = url.split('+:')[-1]
    playlist = api.resolve(playlist_url)
    assert type(playlist) is Playlist
    num = len(playlist.tracks)
    i = 0
    for track in playlist.tracks:
      i += 1
      print(f"Track {i} / {num}")
      filename = f'./{track.artist} - {track.title}.mp3'
      with open(bestand_locatie + filename, 'wb+') as fp:
        track.write_mp3_to(fp)
        print(f"\t{filename} downloaded.")
        
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
  yt = YouTube(url)

  video = yt.streams.filter(only_audio=True).first()

  out_file = video.download(output_path=bestand_locatie)
  base, ext = os.path.splitext(out_file)
  new_file = base + '.mp3'
  os.rename(out_file, new_file)

  file_size = os.path.getsize(new_file) / 1000000
  if file_size < thres:
      print(f"Threshold is not met -> file deleted. Try another version.")
      os.remove(new_file)
  print(yt.title + " has been successfully downloaded from Youtube.")
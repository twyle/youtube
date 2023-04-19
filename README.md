# youtube
A python library that wraps around the YouTube V3 API. You can use it find, manage and analyze YouTube resources including Videos, Playlists, Channels and Comments.

## Installation

```sh
pip install youtube@git+https://github.com/twyle/youtube
```

## Get started
To get started, you need a verified Google Account and Google API keys with the correct permissions.

To get a particular video using the videos' id:
1. Create an instance of the YouTube API:
```sh
from youtube import YouTube

youtube = YouTube()
```
2. Authenticate yourself using the secrets file downloaded from Google Developer console:
```sh
from youtube import YouTube

youtube = YouTube()
client_secrets_file = '/home/lyle/Downloads/secrets.json'
youtube.authenticate_from_client_secrets_file(client_secrets_file)
```
3. Use the video id to find the video:
```python
video = video = youtube.find_video_by_id('vEQ8CXFWLZU')
```
4. To find a channel by id:
```python
channel = youtube.find_channel_by_id('UC8butISFwT-Wl7EV0hUK0BQ')
```
from youtube import YouTube
from itertools import chain

youtube = YouTube()
client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube.authenticate_from_client_secrets_file(client_secrets_file)

# channel = youtube.find_channel_by_id('UC8butISFwT-Wl7EV0hUK0BQ')
# video = youtube.find_video_by_id('vEQ8CXFWLZU')
query = 'Python programming'
video_iterator = youtube.get_iterator(query)
v1 = next(video_iterator)
v2 = next(video_iterator)
v3 = next(video_iterator)

# video_collection = video_iterator.get_videos()
# POSTGRES_HOST='localhost' 
# POSTGRES_PORT=5432 
# POSTGRES_USER='lyle' 
# POSTGRES_PASSWORD='lyle'
# POSTGRES_DB='python-learning-app'
# video_collection.save_to_database(POSTGRES_HOST, POSTGRES_PORT, 
#                         POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)
# search_client = youtube.get_search_client(query)
# prev_token, next_token, v1 = search_client.search_videos()
# prev_token, next_token, v2 = search_client.search_videos(next_page_token=next_token)
# prev_token, next_token, v3 = search_client.search_videos(next_page_token=next_token)
videos = list(chain(v1,v2,v3))

if __name__ == '__main__':
    print(len(videos))
    for video in videos:
        print(video)
    # video.to_json()
    # video.to_csv()
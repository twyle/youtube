from youtube import YouTube

youtube = YouTube()
client_secrets_file = '/home/lyle/Downloads/python_learning_site.json'
youtube.authenticate_from_client_secrets_file(client_secrets_file)

channel = youtube.find_channel_by_id('UC8butISFwT-Wl7EV0hUK0BQ')

if __name__ == '__main__':
    print(channel)
class YouTubeVideoDetails:
    def __init__(self, id: str, channelId: str, title: str, channelTitle: str, 
                 description: str, thumbnails: str, tags: list[str], duration: str, licensedContent: bool):
        self.__id = id
        self.__channel_id = channelId
        self.__title = title
        self.__channel_title = channelTitle
        self.__description = description
        self.__thumbnails = thumbnails
        self.__tags = tags
        self.__duration = duration
        self.__licensed_content = licensedContent
        
    def get_video_details(self):
        video_details = {
            'id': self.__id,
            'channel_id': self.__channel_id,
            'title': self.__title,
            'channel_title': self.__channel_title,
            'description': self.__description,
            'thumbnail': self.get_video_thumbnail(),
            'tags': self.__tags,
            'duration': self.__duration,
            'licensed_content': self.__licensed_content
        }
        return video_details
    
    def get_video_thumbnail(self):
        thumbnail = ''
        if self.__thumbnails:
            if self.__thumbnails.get('standard'):
                thumbnail = self.__thumbnails.get('standard').get('url')
            elif self.__thumbnails.get('medium'):
                thumbnail = self.__thumbnails.get('medium').get('url')
            elif self.__thumbnails.get('high'):
                thumbnail = self.__thumbnails.get('high').get('url')
            elif self.__thumbnails.get('default'):
                thumbnail = self.__thumbnails.get('default').get('url')
            elif self.__thumbnails.get('maxres'):
                thumbnail = self.__thumbnails.get('maxres').get('url')
        return thumbnail
    
    def get_video_title(self):
        return self.__title
    
    def get_video_id(self):
        return self.__id
    
    def get_video_description(self):
        return self.__description
    
    def get_video_duration(self):
        pass
    
    def get_video_tags(self):
        if self.__tags:
            return self.__tags
        return []
    
    def get_channel_id(self):
        return self.__channel_id
    
    def get_channel_title(self):
        return self.__channel_title
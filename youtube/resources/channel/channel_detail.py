class YouTubeChannelDetails:
    def __init__(self, id: str, title: str, description: str, customUrl: str, 
                 publishedAt: str, thumbnails: str):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__custom_url = customUrl
        self.__publishedAt = publishedAt
        self.__thumbnails = thumbnails
        
    def get_channel_details(self):
        channel_details = {
            'id': self.__id,
            'title': self.__title,
            'description': self.__description,
            'custom_url': self.__custom_url ,
            'thumbnail': self.get_channel_thumbnail()
        }
        return channel_details
    
    def get_channel_thumbnail(self):
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
    
    def get_channel_title(self):
        return self.__title
    
    def get_channel_description(self):
        return self.__description
    
    def get_channel_id(self):
        return self.__id
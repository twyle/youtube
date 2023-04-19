from .channel_stat import YouTubeChannelStats
from .channel_detail import YouTubeChannelDetails

class YouTubeChannel:
    def __init__(self, details, statistics):
        self.__details = YouTubeChannelDetails(**details)
        self.__statistics = YouTubeChannelStats(**statistics)
        
    def get_channel_id(self):
        return self.__details.get_channel_id()
    
    def get_channel_title(self):
        return self.__details.get_channel_title()
        
    def get_channel_thumbnail(self):
        return self.__details.get_channel_thumbnail()
    
    def get_channel_details(self):
        return self.__details.get_channel_details()
    
    def get_channel_stats(self):
        return self.__statistics.get_channel_stats()
    
    def get_formatted_channel_stats(self):
        return self.__statistics.get_formatted_channel_stats()
    
    def __repr__(self) -> str:
        return f"YouTubeChannel(id={self.get_channel_id()}, channel_title={self.get_channel_title()})"
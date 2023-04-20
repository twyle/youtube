from .search import Search

class VideoSearch:    
    def __init__(self, youtube_client, query_string):
        self.__youtube_client = youtube_client
        self.__query_string = query_string
        self.__search = None
    
    def get_videos(self):
        if self.__search:
            return self.__search.get_videos().get_youtube_videos()
        return []
    
    
    def get_iterator(self):
        if not self.__search:
            self.__search = Search(self.__youtube_client, self.__query_string)
        return self.__search
    
    def search_videos(self, next_page_token='', previous_page_token=''):
        if not self.__search:
            self.__search = Search(self.__youtube_client, self.__query_string)
        return self.__search.search_videos(next_page_token, previous_page_token)
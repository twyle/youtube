class Stat:
    def __init__(self, stat_value: int):
        self.__stat_value = stat_value
        self.__formatted_value = self.__format_stat()
        
    def __format_stat(self):
        formatted_stat = str(self.__stat_value)
        if self.__stat_value >= 1_000 and self.__stat_value < 1_000_000:
            formatted_stat = round((self.__stat_value/1000))
            formatted_stat = f'{formatted_stat}k'
        elif self.__stat_value >= 1_000_000 and self.__stat_value < 1_000_000_000:
            formatted_stat = round((self.__stat_value/1_000_000))
            formatted_stat = f'{formatted_stat}M'
        elif self.__stat_value >= 1_000_000_000:
            formatted_stat = round((self.__stat_value/1_000_000_000))
            formatted_stat = f'{formatted_stat}B'
        return formatted_stat
    
    def get_stat(self):
        return self.__stat_value
    
    def get_formatted_stat(self):
        return self.__formatted_value
            
    def __repr__(self):
        return f"Stat(stat_value={self.__stat_value})"
    
    def __str__(self):
        return self.__formatted_value
class Timedate:

    def __init__(self, iso_date: str):


        self.set_date_ints([int(element) for element in self.date_string.split('-')])
        self.set_time_ints([int(element) for element in self.time_string.split(':')])

        self.set_dict_from_ints()
        
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int):
        
        self.set_date_ints(year, month, day)
        self.set_time_ints(hour, minute, second)

        self.set_dict_from_ints()
    
    def set_timedate_string(self, iso_date: str):
        
        self.timedate_string = iso_date.split('.')[0]

    def set_date_string(self):
        timedate_split = self.timedate_string.split('T')

        self.date_string = timedate_split[0]
    
    def set_time_string(self):
        timedate_split = self.timedate_string.split('T')

        self.time_string = timedate_split[1]

    def set_date_ints(self, year: int, month: int, day: int):

        if month <= 0 or day <= 0:
            raise ValueError("Invalid integer input")

        self.date_array = [year, month, day]

    def set_time_ints(self, hour: int, minute: int, second: int):

        if hour < 0 or minute < 0 or second < 0:
            raise ValueError("Invalid integer input")

        self.time_array = [hour, minute, second]

    def set_dict_from_ints(self):
        
        self.timedate = {
            "year":   self.date_array[0],
            "month":  self.date_array[1],
            "day":    self.date_array[2],
            "hour":   self.time_array[0],
            "minute": self.time_array[1],
            "second": self.time_array[2]
        }
    
    def set_dict_from_string(self, iso_date: str):

    def get_date(self) -> list(int):
        return self.date_array
    
    def get_time(self) -> list(int):
        return self.time_array

    def get_timedate(self) -> dict:
        return self.timedate

    def __eq__(self, other):
        return self.timedate == other.timedate
    
    def __gt__(self, other: Timedate):
        if self.timedate['second'] < other.timedate['second']:
            if self.timedate['minute'] < other.timedate['minute']:
                if self.timedate['hour'] < other.timedate['hour']:
                    if self.timedate['day'] < other.timedate['day']:
                        if self.timedate['month'] < other.timedate['month']:
                            if self.timedate['year'] > other.timedate['year']:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __le__(self, other):
        return not self.__gt__(self, other)
    
    def __lt__(self, other: Timedate):
        if self.timedate['second'] > other.timedate['seconds']:
            if self.timedate['minute'] > other.timedate['minutes']:
                if self.timedate['second'] > other.timedate['seconds']:
                    if self.timedate['day'] > other.timedate['day']:
                        if self.timedate['month'] > other.timedate['month']:
                            if self.timedate['year'] < other.timedate['year']:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    
    def __ge__(self, other):
        return not self.__lt__(self, other)
    
    def __str__(self):
        return self.timedate_string


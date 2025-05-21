class Timedate:

    def set_timedate_string(self, iso_date: str):
        self.timedate_string = iso_date.split('.')[0]
        self._set_date_string_from_timedate_string()
        self._set_time_string_from_timedate_string()
        self._set_date_ints_from_string()
        self._set_time_ints_from_string()
        self._set_dict_from_ints()
    
    def _set_date_string_from_timedate_string(self):
        self.date_string = self.timedate_string.split('T')[0]
    
    def _set_time_string_from_timedate_string(self):
        self.time_string = self.timedate_string.split('T')[1]

    def _set_date_ints_from_string(self):
        date_split = self.date_string.split('-')

        self._set_date_ints(int(date_split[0]), int(date_split[1]), int(date_split[2]))
    
    def _set_time_ints_from_string(self):
        time_split = self.time_string.split(':')

        self._set_time_ints(int(time_split[0]), int(time_split[1]), int(time_split[2]))

    def _set_date_ints(self, year: int, month: int, day: int):

        # if month <= 0 or day <= 0:
        #     raise ValueError("Invalid integer input")

        self.date_array = [year, month, day]

    def _set_time_ints(self, hour: int, minute: int, second: int):

        # if hour < 0 or minute < 0 or second < 0:
        #     raise ValueError("Invalid integer input")

        self.time_array = [hour, minute, second]

    def _set_dict_from_ints(self):
        
        self.timedate = {
            "year":   self.date_array[0],
            "month":  self.date_array[1],
            "day":    self.date_array[2],
            "hour":   self.time_array[0],
            "minute": self.time_array[1],
            "second": self.time_array[2]
        }
    
    def set_timedate_ints(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:

        self._set_date_ints(year, month, day)
        self._set_time_ints(hour, minute, second)
        self._set_dict_from_ints()
        self._set_date_string_from_ints()
        self._set_time_string_from_ints()
        self._set_timedate_string_from_strings()
        
    def _set_date_string_from_ints(self) -> None:
        self.date_string = f"{self.date_array[0]}-{self.date_array[1]:0>2}-{self.date_array[2]:0>2}"
    
    def _set_time_string_from_ints(self) -> None:
        self.time_string = f"{self.time_array[0]:0>2}:{self.time_array[1]:0>2}:{self.time_array[2]:0>2}"

    def _set_timedate_string_from_strings(self) -> None:
        self.timedate_string = f"{self.date_string}T{self.time_string}"



    def get_date_ints(self) -> list(int):
        return self.date_array
    
    def get_time_ints(self) -> list(int):
        return self.time_array

    def get_timedate_dict(self) -> dict:
        return self.timedate

    def get_date_string(self) -> str:
        return self.date_string
    
    def get_time_string(self) -> str:
        return self.time_string
    
    def get_timedate_string(self) -> str:
        return self.timedate_string



    def __eq__(self, other):
        return self.timedate == other.timedate
    
    def __gt__(self, other: Timedate):
        if self.timedate['year'] > other.timedate['year']:
            return True
        elif self.timedate['year'] < other.timedate['year']:
            return False
        else:
            if self.timedate['month'] > other.timedate['month']:
                return True
            elif self.timedate['month'] < other.timedate['month']:
                return False
            else:
                if self.timedate['day'] > other.timedate['day']:
                    return True
                elif self.timedate['day'] < other.timedate['day']:
                    return False
                else:
                    if self.timedate['hour'] > other.timedate['hour']:
                        return True
                    elif self.timedate['hour'] < other.timedate['hour']:
                        return False
                    else:
                        if self.timedate['minute'] > other.timedate['minute']:
                            return True
                        elif self.timedate['minute'] < other.timedate['minute']:
                            return False
                        else:
                            if self.timedate['second'] > other.timedate['second']:
                                return True
                            elif self.timedate['second'] < other.timedate['second']:
                                return False
                            else:
                                return False
    
    def __le__(self, other):
        return not self.__gt__(other)
    
    def __lt__(self, other: Timedate):
        if self.timedate['year'] < other.timedate['year']:
            return True
        elif self.timedate['year'] > other.timedate['year']:
            return False
        else:
            if self.timedate['month'] < other.timedate['month']:
                return True
            elif self.timedate['month'] > other.timedate['month']:
                return False
            else:
                if self.timedate['day'] < other.timedate['day']:
                    return True
                elif self.timedate['day'] > other.timedate['day']:
                    return False
                else:
                    if self.timedate['hour'] < other.timedate['hour']:
                        return True
                    elif self.timedate['hour'] > other.timedate['hour']:
                        return False
                    else:
                        if self.timedate['minute'] < other.timedate['minute']:
                            return True
                        elif self.timedate['minute'] > other.timedate['minute']:
                            return False
                        else:
                            if self.timedate['second'] < other.timedate['second']:
                                return True
                            elif self.timedate['second'] > other.timedate['second']:
                                return False
                            else:
                                return False

    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __str__(self):
        return self.timedate_string

    def add_hour(self, hour: int) -> Timedate:
        hour_sum = self.get_time_ints()[0] + hour

        if hour_sum >= 24:
            hour_sum -= 24
        elif hour_sum < 0:
            hour_sum += 24

        temp = Timedate()
        temp.set_timedate_ints(
            self.get_date_ints()[0],
            self.get_date_ints()[1],
            self.get_date_ints()[2],
            hour_sum,
            self.get_time_ints()[1],
            self.get_time_ints()[2]
        )

        return temp
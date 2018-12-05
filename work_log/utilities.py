from datetime import datetime
from datetime import timedelta


class Utility:
    """Utility class handles string-> datetime -> string operations

    methods are:str2date, str2time, date2string

    """

    def str2date(self, string):
        """executes string to datetime object conversion

           takes string as argument returns value:datetime object
        """
        while True:
            try:
                # String to datetime:
                string_to_date = datetime.strptime(string, '%m/%d/%Y')
                return string_to_date
                break
            # except if string does not match valid date:
            except ValueError:
                print('This is not a valid date')
                string = input("please input a valid date: ")
                try:
                    # message this does not seem to be a valid date or date not
                    string_to_date = datetime.strptime(string, '%m/%d/%Y')
                    return string_to_date
                    break
                except ValueError:
                        continue

    def str2time(self, string):
        """executes string to datetime.timedelta object

           takes string as object returns a timedelta obect

        """
        while True:
            try:
                # String to timedelta:
                minutes_to_duration = timedelta(minutes=int(string))
                return minutes_to_duration
                break
            # except if string is a invalid format for timedelta conversion
            except ValueError:
                print('This is not a valid duration')
                string = input("please input a numberstring ")
                try:
                    # message this does not seem to be a valid date or date not
                    minutes_to_duration = datetime.strptime(string, '%H/%M')
                    return minutes_to_duration
                    break
                except ValueError:
                        continue

    # convert string to datetime object
    # return object
    def date2string(self, dateobject):

        """date2string: datetime to string conversion return a string"""
        datestring = dateobject.strftime('%m/%d/%Y')
        return datestring

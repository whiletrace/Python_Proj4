from peewee import *

from utilities import Utility

db = SqliteDatabase("/log.db")


class BaseModel(Model):
    class Meta:
        database = db  # this model uses "log.db"


class Log(BaseModel):
    """WorkLog executes writing and reading entry to file

    methods are: logwrite, logread, search_by_date, search_by_string
    search_by_pattern class variable self.entries which is a call
    to logread method instance variables: entries
    """
    employee_name = CharField(max_length=100, unique=True)
    date = DateTimeField()
    project_name = CharField(max_length=25, unique=False)
    duration = DateTimeField()
    optional_notes = CharField(max_length=255)


def logwrite(entries):
    db.connect()
    db.create_tables([Log], safe=True)
    """executes the writing of user input to csv file

        consumes instance varibles: useri, datalist from
        which is passed to method as input argument
    """

    # create a write file
    for entry in entries:
        Log.create(**entry)


'''
def logread(self, csv_file):
        """logread reads in data from csv file creates entry objects"""

        # empty list
        entries = []
        # context manager pattern for
        with open('entries.csv', newline='') as csvfile:
            fieldnames = ['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)
            # be able to iterate over entry from filefile = open('entries.csv')
            file = open('entries.csv')
            utility = Utility()
            # converts key date and key:duration values to datetime/timedelta
            for row in reader:
                for key, value in row.items():
                    if key == 'date':
                        # convert to datetime for search and pattern matching
                        row[key] = utility.str2date(value)
                    elif key == 'duration':
                        row[key] = utility.str2time(value)

                # from csv file create entry objects append to list entries
                entries.append(Entry(**row))

        # output entries
        return entries
'''
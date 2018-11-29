import pdb
from peewee import *

from utilities import Utility

db = SqliteDatabase("log.db")


class BaseModel(Model):
    class Meta:
        database = db  # this model uses "log.db"


def initialization():
    db.connect()
    db.create_tables([Log], safe=True)



class Log(BaseModel):
    """WorkLog executes writing and reading entry to file

    methods are: logwrite, logread, search_by_date, search_by_string
    search_by_pattern class variable self.entries which is a call
    to logread method instance variables: entries
    """
    employee_name = CharField(max_length=100)
    date = DateField(formats='%m/%d/%Y')
    project_name = CharField(max_length=25, unique=False)
    duration = TimeField(formats='%H/%M')
    optional_notes = CharField(max_length=255)


def logwrite(entries):
    pdb.set_trace()
    """executes the writing of user input to LOg.db

        consumes instance varibles: useri, datalist from
        which is passed to method as entries argument
    """
    

    # create a write file
    for entry in entries:
        Log.create(**entry)


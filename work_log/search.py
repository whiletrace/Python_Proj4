
import pdb

from log import db
from log import Log
from utilities import Utility


class Inspector(object):
    """docstring for Inspector"""
    def __init__(self):
        super(Inspector, self).__init__()

    def search_by_date(self, obj):
        pdb.set_trace()

        """ Handles logic for search by date

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results = []
        utility = Utility()

        query = Log.select().dicts().where(Log.date == obj)
        # iterate through all entries

        for row in query:
            results.append(row)
            # if entries match user given date

        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            # setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print('''

                  \nemployee: {}

                  \ndate: {}

                  \nproject: {}

                  \nduration: {}

                  \nnotes: {}
                  \n________________________
                '''.format(
                            entry.get('employee_name'), entry.get('date'), entry.get('project_name'),
                            entry.get('duration'), entry.get('optional_notes')
                           )
                  )


    # search by duration:
    def search_by_duration(self, obj):
        """ Handles logic for search by duration

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results = []
        utility = Utility()

        query = Log.select().dicts().where(Log.duration == obj)
        # iterate through all entries

        for row in query:
            results.append(row)
            # if entries match user given date

        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            # setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print('''

                  \nemployee: {}

                  \ndate: {}

                  \nproject: {}

                  \nduration: {}

                  \nnotes: {}
                  \n________________________
                '''.format(
                            entry.get('employee_name'), entry.get('date'), entry.get('project_name'),
                            entry.get('duration'), entry.get('optional_notes')
                           )
                  )

    # search by exact string:
    def search_by_string(self, string):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results = []
        query = Log.select().dicts().where(Log.project_name.contains(string) | Log.optional_notes.contains(string))
        # iterate through all entries
        for row in query:
            results.append(row)
            # if entries match user given date

        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            # setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print('''

                  \nemployee: {}

                  \ndate: {}

                  \nproject: {}

                  \nduration: {}

                  \nnotes: {}
                  \n________________________
                '''.format(
                            entry.get('employee_name'), entry.get('date'), entry.get('project_name'),
                            entry.get('duration'), entry.get('optional_notes')
                           )
                  )

    def search_by_employee(self, string):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results = []
        query = Log.select().dicts().where(Log.employee_name == string)
        # iterate through all entries
        for row in query:
            results.append(row)
            # if entries match user given date

        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            # setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print('''

                  \nemployee: {}

                  \ndate: {}

                  \nproject: {}

                  \nduration: {}

                  \nnotes: {}
                  \n________________________
                '''.format(
                            entry.get('employee_name'), entry.get('date'), entry.get('project_name'),
                            entry.get('duration'), entry.get('optional_notes')
                           )
                  )

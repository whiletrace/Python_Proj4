import pdb

from log import db
from log import Log
from utilities import Utility


class Inspector(object):
    """docstring for Inspector"""
    def __init__(self):
        super(Inspector, self).__init__()

    def search_by_date(self, obj ):
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

        for row in query :
            results.append(row)
            # if entries match user given date
            
        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            # setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print(''''
                  
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

        
'''
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

        # iterate through all entries
        for entry in self.logread('entries.csv'):
            # if entries match user given date
            if obj == getattr(entry, 'duration'):
                results.append(entry)
        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print(entry)

        return results

    # search by exact string:
    def search_by_string(self, string):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results = []
        utility = Utility()
        # iterate through all entries
        for entry in self.logread('entries.csv'):
            # if string is present in the entry
            # append entry to list results
            if string in entry.project_name or string in entry.optional_notes:
                results.append(entry)
        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print(entry)

        return results

    # search by pattern:
    def search_by_pattern(self, user_input):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """

        results = []
        pattern = re.compile(user_input)
        utility = Utility()

        # iterate through entries
        for entry in self.logread('entries.csv'):
            match = pattern.search(entry.project_name or entry.optional_notes)
            # if entry matches a regex pattern
            if match:
                # appends relevant entries to list results
                results.append(entry)
        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry, 'date')))
            print(entry)
        return results
'''
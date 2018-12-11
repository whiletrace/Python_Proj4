from log import Log


class Inspector(object):
    """Inspector handles search logic for querying the database"""
    def __init__(self):
        super(Inspector, self).__init__()

    def search_by_date(self, obj):

        """ Handles logic for search by date

            instance variable: results returns a list of entries
            query: queries the datebase
            that are appended from row in query
            each result in results is formatted and printed to screen
        """
        results = []

        query = Log.select().dicts().where(Log.date == obj)
        # iterate through all entries

        for row in query:
            results.append(row)

        if len(results) == 0:
            raise ValueError
        else:
            # formats and prints query results to screen
            for entry in results[:]:

                print(''' employee: {}   date: {}   project: {}   duration: {}   notes: {}
                      \n___________________________________________________________________________
                    '''.format(
                                entry.get('employee_name'),
                                entry.get('date'),
                                entry.get('project_name'),
                                entry.get('duration'),
                                entry.get('optional_notes')
                               )
                      )

# if now matching entries

    # search by duration:
    def search_by_duration(self, obj):
        """ Handles logic for search by duration

            instance variable: results returns a list of entries
            query: queries the datebase
            that are appended from row in query
            each result in results is formatted and printed to screen
        """
        results = []

        query = Log.select().dicts().where(Log.duration == obj)
        # iterate through all entries

        for row in query:
            results.append(row)
            # if entries match user given date

        if len(results) == 0:
            raise ValueError
        else:
            # prints matching entry
            for entry in results[:]:

                 print(''' employee: {}   date: {}   project: {}   duration: {}   notes: {}
                      \n___________________________________________________________________________
                    '''.format(
                                entry.get('employee_name'),
                                entry.get('date'),
                                entry.get('project_name'),
                                entry.get('duration'),
                                entry.get('optional_notes')
                               )
                      )

    # search by exact string:
    def search_by_string(self, string):

        """ Handles logic for exact search

            instance variable: results returns a list of entries
            query: queries the datebase
            that are appended from row in query
            each result in results is formatted and printed to screen
        """
        results = []
        query = Log.select().dicts().where(
                                           Log.project_name.contains(string) |
                                           Log.optional_notes.contains(string)
                                           )
        # iterate through all entries
        for row in query:
            results.append(row)
            # if entries match user given date

        if len(results) == 0:
            raise ValueError
        else:
            # prints matching entry
            for entry in results[:]:

                print(''' employee: {}   date: {}   project: {}   duration: {}   notes: {}
                      \n___________________________________________________________________________
                    '''.format(
                                entry.get('employee_name'),
                                entry.get('date'),
                                entry.get('project_name'),
                                entry.get('duration'),
                                entry.get('optional_notes')
                               )
                      )

    def search_by_employee(self, string):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            query: queries the datebase
            that are appended from row in query
            each result in results is formatted and printed to screen
        """
        results = []
        query = Log.select().dicts().where(Log.employee_name == string)
        # iterate through all entries
        for row in query:
            results.append(row)

        if len(results) == 0:
            raise ValueError
        else:
            # prints matching entry
            for entry in results[:]:

                 print(''' employee: {}   date: {}   project: {}   duration: {}   notes: {}
                      \n___________________________________________________________________________
                    '''.format(
                                entry.get('employee_name'),
                                entry.get('date'),
                                entry.get('project_name'),
                                entry.get('duration'),
                                entry.get('optional_notes')
                               )
                      )

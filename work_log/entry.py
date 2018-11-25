class Entry(object):
    
    """ represents a single entry in WorkLog"""
    
    def __init__(self, **kwargs):
        """ 
        initialization of entry object

        attributes are set by keyword arguments this is recieved 
        from WorkLog.Logwrite(), atrributes that will be initialized
        date, duration, project_name, option_notes date: value+ datetime
        object, duration = timedelta, project_name and option_notes
        are strings
        """
        #sets attribute based on key words
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        """sets print formatting for each entry object"""
        return '''\ndate: {}

                  \nproject: {}

                  \nduration: {}

                  \nnotes: {}
                  \n________________________
                '''.format(
                             self.date, self.project_name,
                            self.duration, self.optional_notes
                           )

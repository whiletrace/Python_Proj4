import collections
import csv
from datetime import datetime, timedelta
from datetime import timedelta
import re

from entry import Entry
from utilities import Utility



class WorkLog(object):
    """WorkLog executes writing and reading entry to file 
    
    methods are: logwrite, logread, search_by_date, search_by_string
    search_by_pattern class variable self.entries which is a call 
    to logread method instance variables: entries
    """
    def __init__(self, csv_file = None):
        super(WorkLog, self).__init__()
        
        

    def logwrite(self, input):
        """executes the writing of user input to csv file

            consumes instance varibles: useri, datalist from 
            which is passed to method as input argument
        """
        
        # create a write file
        with open('entries.csv', 'a', newline = '') as csvfile:
            # create an entry from user input(Menu)
            fieldnames =['date','project_name','duration','optional_notes']
            writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
            
            for entry in input:
                #conversion of named tuple to ordered dict
                writer.writerow(entry._asdict())
                


    def logread(self,csv_file):
        """logread reads in data from csv file creates entry objects"""
       
        # empty list
        entries = []
        # context manager pattern for 
        with open('entries.csv', newline = '') as csvfile:
            fieldnames =['date', 'project_name', 'duration', 'optional_notes']
            reader = csv.DictReader(csvfile, fieldnames = fieldnames)
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

    
        
    def search_by_date(self, obj):
        """ Handles logic for search by date

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
            if obj == getattr(entry,'date'):
                results.append(entry)
        # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
        
        return results
                
   

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
            if obj == getattr(entry,'duration'):
                results.append(entry)
         # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
        
        return results

    # search by exact string:
    def search_by_string(self,string):
        """ Handles logic for exact search

            instance variable: results returns a list of entries
            that are appended from self.entries class variable
            which calls Worklog.logread() that methods return
            value is a list entry ojects
        """
        results =[]
        utility = Utility()
        # iterate through all entries
        for entry in self.logread('entries.csv'):
            # if string is present in the entry
            # append entry to list results
            if string in entry.project_name or string in entry.optional_notes:
                results.append(entry)
         # converts datetime objects to string for formatting for display
        for entry in results[:]:
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)

        return results
        
        

    # search by pattern:
    def search_by_pattern(self,user_input):
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
            setattr(entry, 'date', utility.date2string(getattr(entry,'date')))
            print(entry)
        return results




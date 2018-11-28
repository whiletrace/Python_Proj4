import collections
import os
import re

from log import logwrite
from menu import Menu
from search import Inspector
from utilities import Utility


def clear():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


class Main:

    """
Main class gathers and procecsses user input

methods of Main: userchoice1, user_entry_data, user_search.
instance vaiables: useri

"""
                    
    def __init__(self):
        super(Main, self).__init__()

    def userchoice1(self):
        """
        grabs and validates user choice

        Initialize menu object to display menu items variable menu1 prompts for
        and stores user input while loop runs until user provides a valid input
        based upon input the method calls: either self.user_entry_data method
        or will call an instance of menu.submenu() which is a method of
        Menu class and user will

        """
        # grab and store user input
        menu = Menu()
        menu.main()
        while True:
            menu1 = input(
                            'please choose '
                            'option a), or '
                            'option b) '
                         )
            # tests for a valid resonse
            # if user provides valid response loop will break
            if menu1.lower() not in ('a', 'b'):
                print("Not an appropriate choice.")
            else:
                break
        # based upon user input call method
        if menu1 == 'a':

            self.user_entry_data()
        elif menu1 == 'b':
            menu.submenu()
            self.user_search()

    # if create sub
    def user_entry_data(self):
        """
        user_entry_data collects and processes user data for log entry

        while loops and if else statments guide user through dataentry
        data is collected and stored in variable inputs date, duration,
        project_name, and optional_notes variables are used to construct named
        tupple: instance variable useri. which is appended to instance variable
        datalist afterall user data for entry creation is gathered return
        value of method is instance variable datalist.

        """

        # instance variables: store and pass data to
        clear()
        datalist = []
        useri = collections.namedtuple(
                                       'useri', [
                                               'employee_name',
                                               'date',
                                               'project_name',
                                               'duration',
                                               'optional_notes'
                                                ]
                                       )
        # single letter varible holds booleon value
        a = True
        # start of user input loop
        while a:
            # entry date grab input
            while True:
                employee_name = input(
                                      'please enter employee name : '
                                     )
                break
            while True:
                date = input(
                             'please input a date for'
                             'the entry in the format mm/dd/yyyy: '
                             )
                # tests input against  regex pattern if pattern pails test
                pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
                match = pattern.fullmatch(date)
                # if not a match error i
                if not match:
                        print('this is not an appropriate format')
                # if match  a Utility object is instantiated
                # date variable passed to Utility.date2string which tests
                # string to see if its a valid date
                # and while loop is broken
                else:
                    utility = Utility()
                    date = utility.str2date(date)

                    break
            # entry duration grab input
            while True:
                duration = input(
                                 'please input the duration '
                                 'of the task in minutes: '

                                )
                # tests input against regex pattern if pattern  test
                durpattern = re.compile("(\d+)")
                durmatch = durpattern.fullmatch(duration)
                # if pattern fails test
                if not durmatch:
                    print('this is not an appropriate format')
                # if pattern passes loop breaks and values stored
                else:
                    utility = Utility()
                    duration = utility.str2time(duration)
                    break

            # project name grab input
            project_name = input("please give your project a name: ")
            # optional notes grab input
            optional_notes = input("please add notes(optional):")

            # construsction of named tupple: holds all user input from
            user_data = useri(employee_name, date, project_name, duration, optional_notes)
            # user_data appended to list datalist
            datalist.append(user_data._asdict())

            # option create another entry or retunt main menu
            print('\na) create a new entry\nb) return to main menu')
            choice = input('please type your choice: ')
            # if another entry continue statement is run and user
            # will be prompted for data again
            if choice == 'a':
                clear()
                continue
            # if main menu
            else:
                # try to instantiate a worklog objec
                # pass instance vaiable to WorkLog.logwrite
                try:

                    logwrite(datalist)
                    # confirmation of entry creation
                    clear()
                    print('\n Thankyou your entry has been created')
                    '\n'
                    self.userchoice1()
                # Exception if there is a issue with entry creation
                except ValueError:
                    print('I am sorry but the entry was not saved')
                # finally statement instantiates a new Menu()
                # calls Menu.main() method
                # redirects user to main menu options


    def user_search(self):
        """
        user_search gathers and stores user input related to search entries

        handles user data gathering and storage for search by date, duration
        regex pattern and exact match. once data is gathered and stored
        a WorkLog object is instantiated and the data passed to the relevant
        search method of worklog object

        """
        while True:
            # prompt choose search method
            search_option = input('please choose a search option: ')
            # if user provides a invalid response to prompt
            if search_option not in ('a', 'b', 'c', 'd', 'e'):
                print('this is not an available option')
            # if response valid loop will break
            else:
                break

        # if date prompt for date get input
        if search_option == 'a':
            clear()
            # begin loop for entry search by date data collection

            while True:

                date = input(
                               'please input a date to search '
                               'in the format mm/dd/yyyy: '
                            )
                # tests input against  regex pattern
                pattern = re.compile("(\d{2}\/\d{2}\/\d{4})")
                match = pattern.fullmatch(date)
                # if pattern fails test
                # messsage will prompt until correct format recieved
                if not match:
                        print('this is not an appropriate format')
                        continue
                # if usre input valid
                elif match:
                    # Utility object instantiated
                    utility = Utility()
                    # string -> datetime object
                    str2date = utility.str2date(date)
                    # Worklog object instantiated
                    search = Inspector()
                    # call to WorkLog.search_by_date mentod
                    # method handles search logic/ display of relevant entry
                    clear()
                    print('here are the matching entries: ')
                    "\n"
                    search_results = search.search_by_date(str2date)
                # if now matching entries
                if len(search_results) == 0:
                    # message no entries
                    print('could not find a matching entry')
                    # the prompt for user input begins again
                    continue
                # if match loop breaks and search_by_date will display
                else:

                    self.userchoice1()

        # if duration prompt for duration get input
        elif search_option == 'b':
            # begin loop for entry search by duration data collection
            while True:

                duration = input(
                                   'please input the duration of the task '
                                   'that you want to search: '
                                )
                # tests input against  regex pattern
                durpattern = re.compile("(\d+)")
                durmatch = durpattern.fullmatch(duration)

                # if pattern fails test
                # messsage will prompt until correct format recieved
                if not durmatch:
                    print('this is not an appropriate format')
                    continue
                # if user input valid
                elif durmatch:
                    # Utility object instantiated
                    utility = Utility()
                    # string -> timedelta
                    str2time = utility.str2time(duration)
                    # Worklog object instantiated
                    worklog_initiate = WorkLog()
                    # call to WorkLog.search_by_duration
                    # method handles search logic/ display of relevant entry
                    clear()
                    print('here are the matching entries: ')
                    "\n"
                    search_results = worklog_initiate.search_by_duration(str2time)
                # if now matching entries
                if len(search_results) == 0:
                    # message no entries
                    print('could not find a matching entry')
                    # the prompt for user input begins again
                    continue
                # if match loop breaks and search_by_date will display
                else:

                    self.userchoice1()

        # if string  prompt for string get input
        elif search_option == 'c':
            while True:
                string = input(
                                'please type string and we'
                                'will search against it: '
                                )
                # Worklog object instantiated
                worklog_initiate = WorkLog()
                # call to WorkLog.search_by_duration
                # method handles search logic/ display of relevant entry
                clear()
                print('here are the matching entries: ')
                "\n"
                search_results = worklog_initiate.search_by_string(string)
                # if now matching entries
                if len(search_results) == 0:
                    # message no entries
                    print('could not find a matching entry')
                    # the prompt for user input begins again
                    continue
                # if match loop breaks and search_by_date will display
                else:

                    self.userchoice1()

        elif search_option == 'd':
            while True:
                string = input(
                                'please type employee name to search for: '
                                )
                # Worklog object instantiated
                search = Inspector()
                # call to WorkLog.search_by_duration
                # method handles search logic/ display of relevant entry
                clear()
                print('here are the matching entries: ')
                "\n"
                search_results = search.search_by_employee(string)
                # if now matching entries
                if len(search_results) == 0:
                    # message no entries
                    print('could not find a matching entry')
                    # the prompt for user input begins again
                    continue
                # if match loop breaks and search_by_date will display
                else:

                    self.userchoice1()

# initiation of Application
if __name__ == '__main__':

    a = Main()
    a.userchoice1()

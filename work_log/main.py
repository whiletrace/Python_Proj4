import collections
import os
import re


from log import logwrite
from log import initialization
from menu import Menu
from search import Inspector
from utilities import Utility


def clear():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_empoyee():

    """ employee name get input"""
    # start of user input loop
    while True:
        employee_name = input(
                              'please enter employee name : '
                             )
        clear()
        return employee_name


def get_date():
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
            clear()
            return date

            # entry duration grab input


def get_duration():
    """duration grab input"""
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
            clear()
            return duration


def get_projectname():
    """projectname grab input"""
    project_name = input("please give your project a name: ")
    clear()
    return project_name

# project name grab input


def get_optional_notes():
    """optional notes grab input"""
    optional_notes = input("please add notes(optional):")
    clear()
    return optional_notes


def userchoice1():
    """
    grabs and validates user choice which determines

    Initialize menu object to display menu items variable menu1 prompts for
    and stores user input while loop runs until user provides a valid input
    based upon input the method calls: stores returns input for to passeed
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
        if menu1 == 'a':
            return menu1

        if menu1 == 'b':
            return menu1


def new_entry_or_menu():
    while True:
        print('\na) create a new entry\nb) return to main menu')
        entryorMain = input('please type your choice: ')
        if entryorMain not in ['a', 'b']:
            print('That was not a vaild choice')
            continue
        else:
            if entryorMain == 'a':
                clear()
                return entryorMain
            else:
                clear()
                return entryorMain


def data_collection():
    employee = get_empoyee()
    date = get_date()
    project_name = get_projectname()
    duration = get_duration()
    optional_notes = get_optional_notes()
    return employee, date, project_name, duration, optional_notes


def data_2db():
    clear()
    main = Main()
    main.user_entry_data(*data_collection())


def search_initiation():
    main = Main()
    main.user_search()


def submenu():
    clear()
    menu = Menu()
    menu.submenu()


def app():
    while True:
        main_m_input = userchoice1()
        if main_m_input == 'a':
            data_2db()
            while True:
                another_entry_hmm = new_entry_or_menu()
                if another_entry_hmm == 'a':
                    data_2db()
                else:
                    break
        elif main_m_input == 'b':
            submenu()
            search_initiation()


class Main:

    """
    Main class gathers and procecsses user input

    methods of Main: user_entry_data, user_search.
    instance vaiables: useri

    """

    def __init__(self):
        super(Main, self).__init__()

    # if create sub
    def user_entry_data(self, *function):
        """
        user_entry_data collects and processes user data for log entry

        data is collected and stored is passed by user_entry_data() employee
        name,date, duration, project_name, and optional_notes variables are
        used toconstruct named tupple: instance variable useri. which is
        appended to instance variabledatalist afterall user data for entry
        creation is gathered returnvalue of method is instance variable
        datalist which holds ordereddictdatalist is consumed by logwrite and is
        written to the database.

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
        user_data = useri(*function)

        # user_data appended to list datalist
        datalist.append(user_data._asdict())
        print(datalist)
        # option create another entry or retunt main menu

        # if another entry continue statement is run and user
        # will be prompted for data again

        # if main menu

        # try to instantiate a worklog objec
        # pass instance vaiable to WorkLog.logwrite
        try:

            logwrite(datalist)
            # confirmation of entry creation
            clear()
            print('\n Thankyou your entry has been created')
            '\n'

        # Exception if there is a issue with entry creation
        except ValueError:
            print('I am sorry but the entry was not saved')
        # finally statement instantiates a new Menu()
        # calls Menu.main() method
        # redirects user to main menu options

# single letter varible holds booleon value

            # construsction of named tupple: holds all user input from

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
                pattern=re.compile("(\d{2}\/\d{2}\/\d{4})")
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
                    try:
                        clear()
                        "\n"
                        print('here are the matching entries: \n')
                        search_results = search.search_by_date(str2date)
                        app()
                    except ValueError:
                        print('It looks like there is no matching results')
                        app()

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
                    search = Inspector()
                    # call to WorkLog.search_by_duration
                    # method handles search logic/ display of relevant entry
                    try:
                        clear()
                        "\n"
                        print('here are the matching entries: \n')
                        search_results = search.search_by_duration(str2time)
                        app()
                    except ValueError:
                        print('It looks like there is no matching results')
                        app()
        # if string  prompt for string get input
        elif search_option == 'c':
            while True:
                string = input(
                                'please type string and we'
                                'will search against it: '
                                )
                # Worklog object instantiated
                search = Inspector()
                # call to WorkLog.search_by_duration
                # method handles search logic/ display of relevant entry
                try:
                    clear()
                    "\n"
                    print('here are the matching entries: ')
                    search_results = search.search_by_string(string)
                    # if now matching entries
                    app()
                except ValueError:
                    print('It looks like there is no matching results')
                    app()

        elif search_option == 'd':
            while True:
                string = input(
                                'please type employee name to search for: '
                                )
                # Worklog object instantiated
                search = Inspector()
                # call to WorkLog.search_by_duration
                # method handles search logic/ display of relevant entry
                try:
                    clear()
                    "\n"
                    print('here are the matching entries: \n')
                    search_results = search.search_by_employee(string)
                    app()
                except ValueError:
                    print('It looks like there is no matching results')
                    app()
        elif search_option == 'e':
            clear()
            app()


# initiation of Application
if __name__ == '__main__':
    initialization()
    app()

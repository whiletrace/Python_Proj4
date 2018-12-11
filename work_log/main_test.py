import unittest
from unittest.mock import patch


import main
import menu
import utilities


@patch('builtins.print')
class MenuTests(unittest.TestCase):
    """ Test for Menu class"""
    def test_menu_instantiation(self, Mockprint):
        testmenu = menu.Menu()
        self.assertIsInstance(testmenu, menu.Menu)

    def test_menu_main(self, Mockprint):
        """ test that if Menu.main() Print is called"""
        testmenu = menu.Menu()
        testmenu.main()
        Mockprint.assert_called()

    def test_menu_submenu(self, Mockprint):
        """ test that if Menu.submenu() Print is called"""
        testmenu = menu.Menu()
        testmenu.submenu()
        Mockprint.assert_called_once()


@patch('builtins.input')
class MainTests(unittest.TestCase):

    def test_clear(self, Mockinput):
        """testing clear function calls os.system"""
        with patch('main.os') as Mocked_os:
            main.clear()
            Mocked_os.system.assert_called_once()

    def test_get_employee(self, Mockinput):
        """testing to see whether user can enter a str"""
        user_input = ['trace harris']
        Mockinput.side_effect = user_input
        expected_input = main.get_empoyee()
        self.assertEquals(expected_input, 'trace harris')

    def test_projectname(self, Mockinput):
        """testing to see whether this returns a string"""
        user_input = ['project']
        Mockinput.side_effect = user_input
        expected_input = main.get_projectname()
        self.assertEquals(expected_input, 'project')

    def test_get_optional_notes(self, Mockinput):
        """testing to see whether this returns a string"""
        user_input = ['a string']
        Mockinput.side_effect = user_input
        expected_input = main.get_optional_notes()
        self.assertEquals(expected_input, 'a string')

    def test_get_employ(self, Mockinput):
        """when executing function Input is called once"""
        main.get_empoyee()
        Mockinput.assert_called_once()

    def test_test_input_get_date(self, Mockinput):
        """when a string is entered in a correct format a datetime object"""
        user_Input = ['12/23/1999']
        Mockinput.side_effect = user_Input

        expected_input = main.get_date()
        self.assertEquals(expected_input, utilities.datetime(
                                                             1999, 12,
                                                             23, 0,
                                                             0
                                                             ))

    def test_get_duration(self, Mockinput):
        """when a string is entered in a correct format a timedelta """
        user_Input = ['123']
        Mockinput.side_effect = user_Input
        expected_input = main.get_duration()
        self.assertEquals(expected_input, utilities.timedelta(seconds=7380))

    def test_userchoice1(self, Mockinput):
        """test whether func will accept valid response 'a' """
        user_input = ['a', 'c']
        Mockinput.side_effect = user_input
        test_func = main.userchoice1()
        self.assertEqual(test_func, 'a')

    def test_userchoice2(self, Mockinput):
        """test whether func will accept valid response 'b' """
        user_input = ['b', 'c']
        Mockinput.side_effect = user_input
        test_func = main.userchoice1()
        self.assertEqual(test_func, 'b')

    def test_new_entry_or_menu(self, Mockinput):
        """test whether func will accept valid response 'a' """
        user_input = ['a', 'c']
        Mockinput.side_effect = user_input
        test_func = main.new_entry_or_menu()
        self.assertEqual(test_func, 'a')

    def test_new_entry_or_menu2(self, Mockinput):
        """test whether func will accept valid response 'b' """
        user_input = ['b', 'c']
        Mockinput.side_effect = user_input
        test_func = main.new_entry_or_menu()
        self.assertEqual(test_func, 'b')


if __name__ == '__main__':
    unittest.main()

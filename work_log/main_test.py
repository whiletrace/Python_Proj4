import unittest
import pdb
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import Mock
import datetime
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
        user_Input = ['12/23/1999']
        Mockinput.side_effect = user_Input

        expected_input = main.get_date()
        self.assertEquals(expected_input, utilities.datetime(
                                                             1999, 12,
                                                             23, 0,
                                                             0
                                                             ))

    def test_get_duration(self, Mockinput):
        user_Input = ['123']
        Mockinput.side_effect = user_Input
        expected_input = main.get_duration()
        self.assertEquals(expected_input, utilities.timedelta(seconds=7380))


if __name__ == '__main__':
    unittest.main()

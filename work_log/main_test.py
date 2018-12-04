
import builtins
import unittest
from unittest.mock import patch

import main
import menu


@patch('builtins.print')
class MenuTests(unittest.TestCase):

    def test_menu_instantiation(self, Mockprint):
        testmenu = menu.Menu()
        self.assertIsInstance(testmenu, menu.Menu)

    def test_menu_main(self, Mockprint):
        testmenu = menu.Menu()
        testmenu.main()
        Mockprint.assert_called()

    def test_menu_submenu(self, Mockprint):
        testmenu = menu.Menu()
        testmenu.submenu()
        Mockprint.assert_called_once()


@patch('builtins.input', return_value='first last')
class MainTests(unittest.TestCase):

    def test_clear(self, Mockinput):
        with patch('main.os') as Mocked_os:
            main.clear()
            Mocked_os.system.assert_called_once()

    def test_get_employee(self, Mockinput):
        expected_input = main.get_empoyee()
        self.assertEquals(expected_input, 'first last')

    def test_projectname(self, Mockinput):
        expected_input = main.get_projectname()
        self.assertEquals(expected_input, 'first last')

    def test_get_optional_notes(self, Mockinput):
        expected_input = main.get_optional_notes()
        self.assertEquals(expected_input, 'first last')

    def test_get_employ(self, Mockinput, return_value='first last'):
        main.get_empoyee()
        Mockinput.assert_called_once()


if __name__ == '__main__':
    unittest.main()

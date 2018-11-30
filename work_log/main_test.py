import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import main
import menu
import pdb


@patch('__main__.main.Main', autospec=True)
class MainTests(unittest.TestCase):

    def test_main(self, Main):

        self.assertIs(Main, main.Main)

    def test_main_call(self, Main):
        a = Main()
        Main.assert_called_once()

    def test_userchoice1(self, Main):
        Main.userchoice1()
        Main.userchoice1.assert_called_once()

    @patch.object(main.Menu, 'main')
    def test_menucall(self, main_mock, Main):

        main.Menu.main()
        main_mock.assert_called_once()

    @patch.object(main.Menu, 'main')
    def test_menucall(self, main_mock, Main):

        main.Menu.main()
        self.assertIsNotInstance(main_mock, main.Menu)

if __name__ == '__main__':
    unittest.main()

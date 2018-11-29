import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import main

import menu


class MainTests(unittest.TestCase):
    def test_userchoice1(self):
        maintest = main.Main()
        menutest = menu.Menu()
        menutest.main = MagicMock()
        maintest.userchoice1 = MagicMock(side_effect=menutest.main)
        maintest.userchoice1()
        menutest.main.assert_called_once()



if __name__ == '__main__':
    unittest.main()

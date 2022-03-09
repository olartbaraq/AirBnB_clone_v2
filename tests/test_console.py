#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
from contextlib import redirect_stdout
import inspect
import io
import pep8
import unittest
HBNBCommand = console.HBNBCommand

class TestConsoleCommands(unittest.TestCase):
    """Class to test functionality of console commands"""
    @classmethod
    def test_do_create(self):
        """Test do_create method of console"""
        with redirect_stdout(self.output):
            self.cmdcon.onecmd('create')
            self.assertEqual(self.output.getvalue(),
                             "** class name missing **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create blah')
            self.assertEqual(self.output.getvalue(),
                             "** class doesn't exist **\n")
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State')
            self.assertEqual(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')
            self.output.seek(0)
            self.output.truncate()
            self.cmdcon.onecmd('create State name="Californnia"')
            self.assertRegex(self.output.getvalue(),
                             '[a-z0-9]{8}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{4}-'
                             '[a-z0-9]{12}')

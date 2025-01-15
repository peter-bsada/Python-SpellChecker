#!/usr/bin/env python3
# coding=utf8

""" Module for unittests """

import unittest
from spellchecker import SpellChecker

class Testcase(unittest.TestCase):
    """
    My test class
    """

    def test_checkWordTrue(self):
        """
        Check if the world are in the tree. If correct = True.
        """
        sp = SpellChecker()
        sp.insert("hetrow")
        sp.insert("boat")
        sp.insert("car")
        self.assertTrue(sp.check("car"))

    def test_checkWordFalse(self):
        """
        Check if the world are in the tree. If not correct = False.
        """
        sp = SpellChecker()
        sp.insert("hetrow")
        sp.insert("boat")
        sp.insert("car")
        self.assertFalse(sp.check("cars"))

    def test_searchword(self):
        """
        Check if the world are in the tree. If not correct = False.
        """
        sp = SpellChecker()
        sp.insert("hello")
        sp.insert("helloed")
        sp.insert("helloes")
        sp.insert("helloing")
        sp.insert("hellop")
        self.assertEqual(sp.search("hello")[:3], ["hello", "helloed", "helloes"])

    def test_changeFileDictionary(self):
        """
        Check if the world are in the tree. If not correct = False.
        """
        sp = SpellChecker()
        with open("dictionary.txt") as filehandle:
            words = filehandle.read()
            words = ''.join((x for x in words if not x.isdigit()))
            words = words.replace(' .', '')
            words = words.split("\n")

        self.assertEqual(sp.file(), words)

    def test_changeFileFrequency(self):
        """
        Check if the world are in the tree. If not correct = False.
        """
        sp = SpellChecker()
        with open("frequency.txt") as filehandle:
            words = filehandle.read()
            words = ''.join((x for x in words if not x.isdigit()))
            words = words.replace(' .', '')
            words = words.split("\n")

        self.assertEqual(sp.file("frequency.txt"), words)

    def test_removeWord(self):
        """
        Check if the world are in the tree. If correct = True.
        """
        sp = SpellChecker()
        sp.insert("hetrow")
        sp.insert("boat")
        sp.insert("car")
        sp.remove_word(sp.root,"car")
        self.assertFalse(sp.check("car"))


if __name__ == '__main__':
    unittest.main(verbosity=3)

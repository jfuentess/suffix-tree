""" Test the to_dot ()  method. """

# pylint: disable=missing-docstring

import unittest

from suffix_tree import Tree

class TestFind (unittest.TestCase):

    def test_parentheses (self):
        # tree = Tree ({ 'A' : 'aaaaa' })
        # tree = Tree ({ 'A' : 'ababcabcdabdeaef' })
        tree = Tree ({ 'A' : 'abracadabra' })
        # tree = Tree ({ 'A' : 'xabxac', 'B' : 'awyawxawxz' })
        # tree = Tree ({ 'A' : 'xabxac', 'B' : 'awyawxacxz' })
        # tree = Tree ({
        #     'A' : 'a',
        #     'B' : 'ab',
        #     'C' : 'abc',
        #     'D' : 'abcd',
        #     'E' : 'abcde',
        # })
        # tree = Tree ({
        #     'A' : 'abcde',
        #     'B' : 'bcde',
        #     'C' : 'cde',
        #     'D' : 'de',
        #     'E' : 'e',
        # })
        par = tree.parentheses()

        print(par)
        

if __name__ == '__main__':
    unittest.main ()


import unittest
from unittest.mock import patch, mock_open
from math import isclose, sqrt

from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr

tk = TkDrawer()


class TestPolyedr1(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""
        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)


class TestPolyedr2(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0 75.0 45.0 30.0
6 8 24
1.0 0.0 0.0
-1.0 0.0 0.0
0.0 1.0 0.0
0.0 -1.0 0.0
0.0 0.0 1.0
0.0 0.0 -1.0
3 1 3 5
3 1 5 4
3 1 4 6
3 1 6 3
3 2 3 5
3 2 5 4
3 2 4 6
3 2 6 3
"""
        fake_file_path = 'data/octahedron.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 6)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 8)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 24)
